"""
공공데이터포털 목록개방현황 CSV → RDF 변환기

CSV 원본: 공공데이터활용지원센터_공공데이터포털 목록개방현황
출력: JSON-LD, Turtle
"""

import csv
import json
import re
import sys
from pathlib import Path
from rdflib import Graph, Literal, URIRef, BNode
from rdflib.namespace import RDF, RDFS, XSD, DCTERMS, FOAF, SKOS

# 네임스페이스는 shared/namespaces.py를 통해 사용 (CLAUDE.md 규칙)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))
from shared.namespaces import (
    AIRD, DCAT, VCARD, SCHEMA, ADMS, DQV, DATA_GO_KR,
    bind_common_prefixes,
)

# --- 정규화 테이블 ---

FREQUENCY_MAP = {
    "일간": "http://publications.europa.eu/resource/authority/frequency/DAILY",
    "주간": "http://publications.europa.eu/resource/authority/frequency/WEEKLY",
    "월간": "http://publications.europa.eu/resource/authority/frequency/MONTHLY",
    "분기": "http://publications.europa.eu/resource/authority/frequency/QUARTERLY",
    "반기": "http://publications.europa.eu/resource/authority/frequency/ANNUAL_2",
    "연간": "http://publications.europa.eu/resource/authority/frequency/ANNUAL",
    "수시": "http://publications.europa.eu/resource/authority/frequency/IRREG",
}

LICENSE_MAP = {
    "0": f"{DATA_GO_KR}/license/kogl/type-0",
    "1": f"{DATA_GO_KR}/license/kogl/type-1",
    "2": f"{DATA_GO_KR}/license/kogl/type-2",
    "3": f"{DATA_GO_KR}/license/kogl/type-3",
    "4": f"{DATA_GO_KR}/license/kogl/type-4",
}

FORMAT_TYPO = {
    "xlxs": "xlsx",
    "cvs": "csv",
}

MEDIA_TYPE_MAP = {
    "텍스트": "text",
    "이미지": "image",
    "동영상": "video",
    "소리": "audio",
    "멀티미디어": "multimedia",
    "기타": "etc",
}

# v2.0: 확장자 기반 IANA 미디어 타입 매핑
IANA_MEDIA_TYPE_MAP = {
    "csv": "text/csv",
    "json": "application/json",
    "xml": "application/xml",
    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "xls": "application/vnd.ms-excel",
    "pdf": "application/pdf",
    "hwp": "application/x-hwp",
    "hwpx": "application/hwp+zip",
    "zip": "application/zip",
    "html": "text/html",
    "txt": "text/plain",
    "doc": "application/msword",
    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "ppt": "application/vnd.ms-powerpoint",
    "pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "gif": "image/gif",
    "tif": "image/tiff",
    "tiff": "image/tiff",
    "shp": "application/x-shapefile",
    "geojson": "application/geo+json",
    "rdf": "application/rdf+xml",
}

# v2.0: IANA 대분류 (확장자 기반 mediaType과 매체유형 컬럼 교차 검증용)
MEDIA_CATEGORY_MAP = {
    "text": "텍스트",
    "application": "텍스트",
    "image": "이미지",
    "video": "동영상",
    "audio": "소리",
}

# v2.0: License 리소스 제목
LICENSE_TITLE_MAP = {
    "0": "공공누리 제0유형",
    "1": "공공누리 제1유형",
    "2": "공공누리 제2유형",
    "3": "공공누리 제3유형",
    "4": "공공누리 제4유형",
}

KOGL_OFFICIAL_BASE = "https://www.kogl.or.kr/info/license.do#type-"


# --- 전처리 함수 ---

def clean_null(value):
    """결측값 통일: '-', '' → None"""
    if value is None:
        return None
    stripped = value.strip()
    if stripped in ("", "-"):
        return None
    return stripped


def clean_phone(value):
    """전화번호 백틱 제거, 숫자만 추출"""
    if not value:
        return None
    return re.sub(r"[^0-9]", "", value)


def clean_html(value):
    """HTML 태그 제거"""
    if not value:
        return None
    text = re.sub(r"<[^>]+>", " ", value)
    text = re.sub(r"\s+", " ", text).strip()
    return text if text else None


def normalize_format(value):
    """확장자 소문자 정규화 + 오타 수정"""
    if not value:
        return None
    lower = value.strip().lower()
    return FORMAT_TYPO.get(lower, lower)


def parse_license(value):
    """이용허락범위 → (license_uri, has_third_party)"""
    if not value:
        return None, False

    has_third_party = "제3자 권리 포함" in value

    if "이용허락범위 제한 없음" in value:
        return LICENSE_MAP["1"], has_third_party

    match = re.search(r"제\s*(\d)\s*유형", value)
    if match:
        type_num = match.group(1)
        return LICENSE_MAP.get(type_num), has_third_party

    return None, has_third_party


def parse_cost(value):
    """비용부과유무 → boolean or None"""
    if not value:
        return None
    if value == "무료":
        return True
    if value == "유료":
        return False
    return None


def to_slug(text):
    """한글/영문 텍스트를 URI 안전한 slug로 변환"""
    if not text:
        return "unknown"
    slug = re.sub(r"[^\w가-힣]", "-", text)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug if slug else "unknown"


# --- 그래프 구축 ---

def build_graph(csv_path, limit=None):
    """CSV를 읽어 RDF 그래프를 구축한다."""
    g = Graph()
    bind_common_prefixes(g)

    # Catalog
    catalog_uri = URIRef(f"{DATA_GO_KR}/catalog")
    g.add((catalog_uri, RDF.type, DCAT.Catalog))
    g.add((catalog_uri, DCTERMS.title, Literal("공공데이터포털", lang="ko")))
    g.add((catalog_uri, DCTERMS.description,
           Literal("대한민국 공공데이터 포털 데이터 카탈로그", lang="ko")))

    # v2.0: Catalog → themeTaxonomy 연결
    # Theme ConceptScheme
    theme_scheme = URIRef(f"{DATA_GO_KR}/theme")
    g.add((theme_scheme, RDF.type, SKOS.ConceptScheme))
    g.add((theme_scheme, DCTERMS.title, Literal("공공데이터 분류체계", lang="ko")))

    # Dataset Type ConceptScheme
    type_scheme = URIRef(f"{DATA_GO_KR}/type")
    g.add((type_scheme, RDF.type, SKOS.ConceptScheme))
    g.add((type_scheme, DCTERMS.title, Literal("공공데이터 목록유형", lang="ko")))

    # v2.0: Catalog에 themeTaxonomy 연결
    g.add((catalog_uri, DCAT.themeTaxonomy, theme_scheme))
    g.add((catalog_uri, DCAT.themeTaxonomy, type_scheme))

    # License 중복 방지용 캐시
    licenses_created = set()

    # 중복 방지용 캐시
    orgs_created = set()
    themes_created = set()
    types_created = set()

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if limit and i >= limit:
                break

            dataset_id = clean_null(row.get("목록키"))
            if not dataset_id:
                continue

            dataset_uri = URIRef(f"{DATA_GO_KR}/dataset/{dataset_id}")

            # --- Dataset ---
            g.add((dataset_uri, RDF.type, DCAT.Dataset))
            g.add((catalog_uri, DCAT.dataset, dataset_uri))

            # 직접 속성
            g.add((dataset_uri, DCTERMS.identifier, Literal(dataset_id)))

            title = clean_null(row.get("목록명"))
            if title:
                g.add((dataset_uri, DCTERMS.title, Literal(title, lang="ko")))

            desc = clean_html(clean_null(row.get("설명")))
            if desc:
                g.add((dataset_uri, DCTERMS.description, Literal(desc, lang="ko")))

            comment = clean_null(row.get("기타 유의사항"))
            if comment:
                g.add((dataset_uri, RDFS.comment, Literal(comment, lang="ko")))

            issued = clean_null(row.get("등록일"))
            if issued:
                g.add((dataset_uri, DCTERMS.issued,
                       Literal(issued, datatype=XSD.date)))

            modified = clean_null(row.get("수정일"))
            if modified:
                g.add((dataset_uri, DCTERMS.modified,
                       Literal(modified, datatype=XSD.date)))

            landing = clean_null(row.get("목록 URL"))
            if landing:
                g.add((dataset_uri, DCAT.landingPage, URIRef(landing)))

            next_update = clean_null(row.get("차기 등록 예정일"))
            if next_update:
                g.add((dataset_uri, AIRD.nextUpdateDate,
                       Literal(next_update, datatype=XSD.date)))

            legal_basis = clean_null(row.get("보유근거"))
            if legal_basis:
                g.add((dataset_uri, DCTERMS.references,
                       Literal(legal_basis, lang="ko")))

            collection = clean_null(row.get("수집방법"))
            if collection:
                g.add((dataset_uri, AIRD.collectionMethod,
                       Literal(collection, lang="ko")))

            # 국가중점여부
            national = clean_null(row.get("국가중점여부"))
            if national:
                g.add((dataset_uri, AIRD.isNationalCoreDataset,
                       Literal(national == "Y", datatype=XSD.boolean)))

            # 표준데이터여부 (v2.0: dct:conformsTo, Y인 경우만 생성)
            standard = clean_null(row.get("표준데이터여부"))
            if standard == "Y":
                std_uri = URIRef(f"{DATA_GO_KR}/standard/dataset")
                g.add((dataset_uri, DCTERMS.conformsTo, std_uri))
                g.add((std_uri, RDF.type, DCTERMS.Standard))
                g.add((std_uri, DCTERMS.title,
                       Literal("공공데이터 표준", lang="ko")))

            # 키워드 (쉼표 분리 → 다중 트리플)
            keywords = clean_null(row.get("키워드"))
            if keywords:
                for kw in keywords.split(","):
                    kw = kw.strip()
                    if kw:
                        g.add((dataset_uri, DCAT.keyword,
                               Literal(kw, lang="ko")))

            # --- 목록유형 (B-4) ---
            dtype = clean_null(row.get("목록유형"))
            if dtype:
                type_uri = URIRef(f"{DATA_GO_KR}/type/{dtype}")
                g.add((dataset_uri, DCTERMS.type, type_uri))
                if dtype not in types_created:
                    g.add((type_uri, RDF.type, SKOS.Concept))
                    g.add((type_uri, SKOS.prefLabel,
                           Literal(dtype, lang="ko")))
                    g.add((type_uri, SKOS.inScheme, type_scheme))
                    types_created.add(dtype)

            # --- 분류체계 (B-3) ---
            theme_raw = clean_null(row.get("분류체계"))
            if theme_raw and " - " in theme_raw:
                parts = theme_raw.split(" - ", 1)
                major_label = parts[0].strip()
                minor_label = parts[1].strip()
                major_slug = to_slug(major_label)
                minor_slug = to_slug(minor_label)

                major_uri = URIRef(f"{DATA_GO_KR}/theme/{major_slug}")
                minor_uri = URIRef(f"{DATA_GO_KR}/theme/{minor_slug}")

                # v2.0: 대분류 + 소분류 모두 dcat:theme으로 연결
                g.add((dataset_uri, DCAT.theme, minor_uri))
                g.add((dataset_uri, DCAT.theme, major_uri))

                if minor_slug not in themes_created:
                    g.add((minor_uri, RDF.type, SKOS.Concept))
                    g.add((minor_uri, SKOS.prefLabel,
                           Literal(minor_label, lang="ko")))
                    g.add((minor_uri, SKOS.broader, major_uri))
                    g.add((minor_uri, SKOS.inScheme, theme_scheme))
                    themes_created.add(minor_slug)

                if major_slug not in themes_created:
                    g.add((major_uri, RDF.type, SKOS.Concept))
                    g.add((major_uri, SKOS.prefLabel,
                           Literal(major_label, lang="ko")))
                    g.add((major_uri, SKOS.topConceptOf, theme_scheme))
                    g.add((major_uri, SKOS.inScheme, theme_scheme))
                    themes_created.add(major_slug)

            # --- 업데이트 주기 (B-5) ---
            freq = clean_null(row.get("업데이트 주기"))
            if freq and freq in FREQUENCY_MAP:
                g.add((dataset_uri, DCTERMS.accrualPeriodicity,
                       URIRef(FREQUENCY_MAP[freq])))

            # --- Publisher (B-1) ---
            org_code = clean_null(row.get("제공기관코드"))
            org_name = clean_null(row.get("제공기관"))
            if org_code:
                org_uri = URIRef(f"{DATA_GO_KR}/org/{org_code}")
                g.add((dataset_uri, DCTERMS.publisher, org_uri))
                if org_code not in orgs_created:
                    g.add((org_uri, RDF.type, FOAF.Organization))
                    g.add((org_uri, DCTERMS.identifier, Literal(org_code)))
                    if org_name:
                        g.add((org_uri, FOAF.name,
                               Literal(org_name, lang="ko")))
                    orgs_created.add(org_code)

            # --- ContactPoint (B-2) ---
            dept_name = clean_null(row.get("관리 부서명"))
            dept_phone = clean_phone(clean_null(row.get("관리부서 전화번호")))
            if dept_name or dept_phone:
                cp = BNode()
                g.add((dataset_uri, DCAT.contactPoint, cp))
                g.add((cp, RDF.type, VCARD.Kind))
                if dept_name:
                    g.add((cp, VCARD.fn, Literal(dept_name, lang="ko")))
                if dept_phone:
                    phone_uri = URIRef(f"tel:{dept_phone}")
                    g.add((cp, VCARD.hasTelephone, phone_uri))

            # --- 공간범위 (B-10) ---
            spatial = clean_null(row.get("공간범위"))
            if spatial:
                loc = BNode()
                g.add((dataset_uri, DCTERMS.spatial, loc))
                g.add((loc, RDF.type, DCTERMS.Location))
                g.add((loc, RDFS.label, Literal(spatial, lang="ko")))

            # --- 시간범위 (B-10) ---
            temporal = clean_null(row.get("시간범위"))
            if temporal:
                period = BNode()
                g.add((dataset_uri, DCTERMS.temporal, period))
                g.add((period, RDF.type, DCTERMS.PeriodOfTime))
                g.add((period, RDFS.label, Literal(temporal, lang="ko")))

            # --- 이용통계 (B-8) ---
            download_count = clean_null(row.get("다운로드_활용신청건수"))
            if download_count and download_count.isdigit():
                stat_dl = BNode()
                g.add((dataset_uri, SCHEMA.interactionStatistic, stat_dl))
                g.add((stat_dl, RDF.type, SCHEMA.InteractionCounter))
                g.add((stat_dl, SCHEMA.interactionType,
                       SCHEMA.DownloadAction))
                g.add((stat_dl, SCHEMA.userInteractionCount,
                       Literal(int(download_count), datatype=XSD.integer)))

            view_count = clean_null(row.get("조회수"))
            if view_count and view_count.isdigit():
                stat_view = BNode()
                g.add((dataset_uri, SCHEMA.interactionStatistic, stat_view))
                g.add((stat_view, RDF.type, SCHEMA.InteractionCounter))
                g.add((stat_view, SCHEMA.interactionType, SCHEMA.ViewAction))
                g.add((stat_view, SCHEMA.userInteractionCount,
                       Literal(int(view_count), datatype=XSD.integer)))

            # --- 데이터 한계 (B-9) ---
            quality_note = clean_null(row.get("데이터 한계"))
            if quality_note:
                qa = BNode()
                g.add((dataset_uri, DQV.hasQualityAnnotation, qa))
                g.add((qa, RDF.type, DQV.QualityAnnotation))
                g.add((qa, RDFS.comment, Literal(quality_note, lang="ko")))

            # --- Distribution ---
            dist_uri = URIRef(f"{DATA_GO_KR}/dataset/{dataset_id}/distribution")
            g.add((dist_uri, RDF.type, DCAT.Distribution))
            g.add((dataset_uri, DCAT.distribution, dist_uri))

            file_title = clean_null(row.get("파일데이터명"))
            if file_title:
                g.add((dist_uri, DCTERMS.title,
                       Literal(file_title, lang="ko")))

            # 확장자 (정규화) + v2.0 IANA 미디어 타입
            fmt = normalize_format(clean_null(row.get("확장자(데이터포맷)")))
            if fmt:
                g.add((dist_uri, DCTERMS.format, Literal(fmt)))
                # v2.0: 확장자 기반 IANA 미디어 타입 매핑
                iana_type = IANA_MEDIA_TYPE_MAP.get(fmt)
                if iana_type:
                    g.add((dist_uri, DCAT.mediaType, Literal(iana_type)))

            # v2.0: 매체유형 컬럼은 교차 검증용 (트리플 미생성)
            media = clean_null(row.get("매체유형"))
            if media and fmt and media in MEDIA_TYPE_MAP:
                iana_type = IANA_MEDIA_TYPE_MAP.get(fmt)
                if iana_type:
                    iana_category = iana_type.split("/")[0]
                    expected_media = MEDIA_CATEGORY_MAP.get(iana_category)
                    if expected_media and expected_media != media:
                        print(f"  [검증] {dataset_id}: 매체유형 '{media}' ≠ "
                              f"확장자 '{fmt}' 기반 분류 '{expected_media}'")

            # 전체행
            row_count = clean_null(row.get("전체행"))
            if row_count and row_count.isdigit():
                g.add((dist_uri, AIRD.rowCount,
                       Literal(int(row_count), datatype=XSD.integer)))

            # 이용허락범위 (B-6, v2.0 보강)
            license_raw = clean_null(row.get("이용허락범위"))
            license_uri, has_third_party = parse_license(license_raw)
            if license_uri:
                lic_ref = URIRef(license_uri)
                g.add((dist_uri, DCTERMS.license, lic_ref))
                # v2.0: License 리소스 상세 정보
                if license_uri not in licenses_created:
                    g.add((lic_ref, RDF.type, DCTERMS.LicenseDocument))
                    # license_uri에서 type 번호 추출
                    lic_type_num = license_uri.rsplit("-", 1)[-1]
                    lic_title = LICENSE_TITLE_MAP.get(lic_type_num)
                    if lic_title:
                        g.add((lic_ref, DCTERMS.title,
                               Literal(lic_title, lang="ko")))
                        g.add((lic_ref, RDFS.seeAlso,
                               URIRef(f"{KOGL_OFFICIAL_BASE}{lic_type_num}")))
                    licenses_created.add(license_uri)
            if has_third_party:
                g.add((dist_uri, AIRD.hasThirdPartyRights,
                       Literal(True, datatype=XSD.boolean)))

            # 비용부과유무 (B-7)
            cost_free = parse_cost(clean_null(row.get("비용부과유무")))
            if cost_free is not None:
                g.add((dist_uri, SCHEMA.isAccessibleForFree,
                       Literal(cost_free, datatype=XSD.boolean)))

            cost_desc = clean_null(row.get("비용부과기준 및 단위"))
            if cost_free is False and cost_desc:
                offer = BNode()
                g.add((dist_uri, SCHEMA.offers, offer))
                g.add((offer, RDF.type, SCHEMA.Offer))
                g.add((offer, SCHEMA.description,
                       Literal(cost_desc, lang="ko")))

            # 제공형태 (B-12)
            access_method = clean_null(row.get("제공형태"))
            if access_method:
                am_slug = to_slug(access_method)
                am_uri = URIRef(f"{DATA_GO_KR}/accessMethod/{am_slug}")
                g.add((dist_uri, AIRD.accessMethod, am_uri))
                # ConceptScheme은 반복 생성 방지 불필요 (동일 URI 중복 트리플은 무시됨)
                g.add((am_uri, RDF.type, SKOS.Concept))
                g.add((am_uri, SKOS.prefLabel,
                       Literal(access_method, lang="ko")))

            # --- DataService (API인 경우) (B-13) ---
            if dtype == "API":
                svc = BNode()
                g.add((dist_uri, DCAT.accessService, svc))
                g.add((svc, RDF.type, DCAT.DataService))

                api_type = clean_null(row.get("API 유형"))
                if api_type:
                    g.add((svc, DCTERMS.type, Literal(api_type)))

                traffic = clean_null(row.get("신청가능 트래픽"))
                if traffic:
                    g.add((svc, AIRD.trafficLimit,
                           Literal(traffic, lang="ko")))

                approval = clean_null(row.get("심의 유형"))
                if approval:
                    g.add((svc, AIRD.approvalType,
                           Literal(approval, lang="ko")))

    return g


# --- 출력 ---

def export_graph(g, output_dir, base_name="public_data_catalog", full=False):
    """그래프를 출력한다.

    full=True: 대규모 그래프용. N-Triples(빠른 직렬화) + JSON-LD 출력.
    full=False: 소규모(샘플). Turtle + JSON-LD 출력.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    paths = []

    if full:
        # N-Triples (대규모에서 빠름)
        nt_path = output_dir / f"{base_name}.nt"
        g.serialize(destination=str(nt_path), format="nt", encoding="utf-8")
        print(f"N-Triples: {nt_path} ({nt_path.stat().st_size:,} bytes)")
        paths.append(nt_path)
    else:
        # Turtle (소규모에서 가독성 좋음)
        ttl_path = output_dir / f"{base_name}.ttl"
        g.serialize(destination=str(ttl_path), format="turtle",
                    encoding="utf-8")
        print(f"Turtle: {ttl_path} ({ttl_path.stat().st_size:,} bytes)")
        paths.append(ttl_path)

    # JSON-LD
    jsonld_path = output_dir / f"{base_name}.jsonld"
    jsonld_str = g.serialize(format="json-ld", indent=2)
    jsonld_path.write_text(jsonld_str, encoding="utf-8")
    print(f"JSON-LD: {jsonld_path} ({jsonld_path.stat().st_size:,} bytes)")
    paths.append(jsonld_path)

    return paths


def main():
    project_root = Path(__file__).resolve().parent.parent  # tools/catalog-converter/
    csv_path = project_root / "data" / "public_data_catalog_20260228.csv"
    output_dir = project_root / "output"

    if not csv_path.exists():
        print(f"CSV 파일을 찾을 수 없습니다: {csv_path}")
        sys.exit(1)

    limit = None
    if len(sys.argv) > 1:
        try:
            limit = int(sys.argv[1])
            print(f"변환 제한: {limit}건")
        except ValueError:
            pass

    print(f"입력: {csv_path}")

    examples_dir = project_root / "examples"

    # 샘플 출력 (처음 10건, Turtle + JSON-LD)
    print("샘플(10건) 변환 중...")
    sample_g = build_graph(csv_path, limit=10)
    print(f"샘플 트리플 수: {len(sample_g):,}")
    export_graph(sample_g, examples_dir,
                 base_name="sample_10", full=False)

    # 샘플 출력 (처음 100건, Turtle + JSON-LD)
    print("샘플(100건) 변환 중...")
    sample100_g = build_graph(csv_path, limit=100)
    print(f"샘플(100건) 트리플 수: {len(sample100_g):,}")
    export_graph(sample100_g, examples_dir,
                 base_name="sample_100", full=False)

    # 전체 변환 (N-Triples + JSON-LD)
    print("전체 변환 중...")
    g = build_graph(csv_path, limit=limit)
    print(f"전체 트리플 수: {len(g):,}")
    export_graph(g, output_dir, full=True)

    print("완료.")


if __name__ == "__main__":
    main()
