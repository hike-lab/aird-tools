# 어휘 매핑 명세 v2.0

## 개요

공공데이터포털 목록개방현황 CSV(36개 컬럼)를 DCAT, Dublin Core, SKOS 등 표준 어휘와 AIRD 커스텀 어휘를 조합하여 RDF로 변환하기 위한 매핑 규격.

### v2.0 변경 이력 (v1.0 대비)

| 항목 | v1.0 | v2.0 | 사유 |
|------|------|------|------|
| `dcat:mediaType` 값 | `"text"`, `"image"` 등 단순 문자열 | 확장자 기반 IANA 미디어 타입 | DCAT 스펙 준수 |
| `aird:isStandardDataset` | `xsd:boolean` | `dct:conformsTo` + URI | 표준 어휘 활용 |
| `dcat:theme` | 소분류만 연결 | 대분류 + 소분류 모두 연결 | SPARQL 질의 편의 |
| License URI | 자체 URI만 | `rdfs:seeAlso`로 KOGL 공식 URI 연결 | 외부 연동성 |
| ContactPoint 타입 | `vcard:Organization` | `vcard:Kind` | DCAT-AP 권장 range 준수 |
| 키워드 | 문자열만 | 향후 `skos:Concept` 연결 확장 경로 명시 | AI/KG 활용 대비 |

---

## 사용 어휘 (Prefix)

| Prefix | URI | 용도 |
|--------|-----|------|
| `dcat` | `http://www.w3.org/ns/dcat#` | 데이터 카탈로그 코어 |
| `dct` | `http://purl.org/dc/terms/` | 범용 메타데이터 |
| `vcard` | `http://www.w3.org/2006/vcard/ns#` | 연락처 |
| `foaf` | `http://xmlns.com/foaf/0.1/` | 조직 |
| `schema` | `http://schema.org/` | 통계, 비용 |
| `adms` | `http://www.w3.org/ns/adms#` | 자산 설명 |
| `dqv` | `http://www.w3.org/ns/dqv#` | 데이터 품질 |
| `skos` | `http://www.w3.org/2004/02/skos/core#` | 통제어휘 |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` | 데이터타입 |
| `rdfs` | `http://www.w3.org/2000/01/rdf-schema#` | 스키마 |
| `aird` | `http://datahub.kr/ns/aird#` | AI-Ready Data 커스텀 어휘 |

---

## A. 직접 속성 매핑 (컬럼 → literal/URI 1:1)

| # | CSV 컬럼 | 대상 클래스 | RDF 속성 | 값 타입 | 비고 |
|---|----------|------------|----------|---------|------|
| 1 | 목록키 | `dcat:Dataset` | `dct:identifier` | `xsd:string` | |
| 3 | 목록명 | `dcat:Dataset` | `dct:title` | `rdf:langString` | `@ko` |
| 4 | 파일데이터명 | `dcat:Distribution` | `dct:title` | `rdf:langString` | `@ko` |
| 17 | 키워드 | `dcat:Dataset` | `dcat:keyword` | `rdf:langString` | 쉼표 분리 → 다중 트리플, `@ko`. 향후 `skos:Concept` 연결 확장 예정 |
| 19 | 등록일 | `dcat:Dataset` | `dct:issued` | `xsd:date` | |
| 20 | 수정일 | `dcat:Dataset` | `dct:modified` | `xsd:date` | |
| 23 | 설명 | `dcat:Dataset` | `dct:description` | `rdf:langString` | `@ko`, HTML 태그 제거 |
| 24 | 기타 유의사항 | `dcat:Dataset` | `rdfs:comment` | `rdf:langString` | `@ko` |
| 34 | 목록 URL | `dcat:Dataset` | `dcat:landingPage` | `xsd:anyURI` | |
| 10 | 보유근거 | `dcat:Dataset` | `dct:references` | `rdf:langString` | `@ko`, 법적 근거 |
| 11 | 수집방법 | `dcat:Dataset` | `aird:collectionMethod` | `rdf:langString` | `@ko`, 커스텀 속성 (`dct:source`는 "원본 리소스" 의미로 부적합) |
| 13 | 차기 등록 예정일 | `dcat:Dataset` | `aird:nextUpdateDate` | `xsd:date` | 커스텀 속성 |
| 15 | 전체행 | `dcat:Distribution` | `aird:rowCount` | `xsd:integer` | 커스텀 속성 |
| 35 | 국가중점여부 | `dcat:Dataset` | `aird:isNationalCoreDataset` | `xsd:boolean` | N→false, Y→true |

### A-변경. 표준데이터여부 (컬럼 #36)

**v1.0**: `aird:isStandardDataset` (boolean)

**v2.0**: `dct:conformsTo` (URI) — 표준 준수 여부를 의미적으로 더 정확하게 표현

```
(Y인 경우)
Dataset  --dct:conformsTo-->  <https://data.go.kr/standard/dataset>

<https://data.go.kr/standard/dataset>  a dct:Standard
  --dct:title-->  "공공데이터 표준"@ko
```

(N인 경우 해당 트리플 미생성)

---

## B. 중간 노드 생성 매핑

### B-1. Publisher (제공기관)

**컬럼**: #6 제공기관코드, #7 제공기관

```
Dataset  --dct:publisher-->  <https://data.go.kr/org/{제공기관코드}>  a foaf:Organization
  --dct:identifier-->  "{제공기관코드}"
  --foaf:name-->       "{제공기관}"@ko
```

URI 생성: `https://data.go.kr/org/{제공기관코드}` — 동일 기관코드는 하나의 리소스로 통합

### B-2. ContactPoint (관리부서)

**컬럼**: #8 관리 부서명, #9 관리부서 전화번호

```
Dataset  --dcat:contactPoint-->  _:cp  a vcard:Kind
  --vcard:fn-->              "{관리 부서명}"@ko
  --vcard:hasTelephone-->    <tel:{전화번호}>  a vcard:Voice
```

전화번호: 백틱 제거, `tel:` URI 스킴

### B-3. Theme (분류체계) — **v2.0 변경**

**컬럼**: #5 분류체계 — `"대분류 - 소분류"` 패턴 (100% 2파트)

```
Dataset  --dcat:theme-->  <https://data.go.kr/theme/{소분류slug}>
Dataset  --dcat:theme-->  <https://data.go.kr/theme/{대분류slug}>

<https://data.go.kr/theme/{소분류slug}>  a skos:Concept
  --skos:prefLabel-->  "{소분류}"@ko
  --skos:broader-->    <https://data.go.kr/theme/{대분류slug}>
  --skos:inScheme-->   <https://data.go.kr/theme>

<https://data.go.kr/theme/{대분류slug}>  a skos:Concept
  --skos:prefLabel-->       "{대분류}"@ko
  --skos:topConceptOf-->    <https://data.go.kr/theme>

<https://data.go.kr/theme>  a skos:ConceptScheme
  --dct:title-->  "공공데이터 분류체계"@ko
```

**v1.0 대비 변경**: Dataset에 소분류만 연결하던 것을 **대분류도 `dcat:theme`으로 직접 연결**. SPARQL에서 대분류 기반 필터링 시 별도 `skos:broader` 탐색 불필요.

### B-4. 목록유형

**컬럼**: #2 목록유형 — FILE, API, STD

```
Dataset  --dct:type-->  <https://data.go.kr/type/{값}>  a skos:Concept
  --skos:prefLabel-->  "{값}"@ko
  --skos:inScheme-->   <https://data.go.kr/type>

<https://data.go.kr/type>  a skos:ConceptScheme
  --dct:title-->  "공공데이터 목록유형"@ko
```

### B-5. 업데이트 주기

**컬럼**: #12 업데이트 주기

```
Dataset  --dct:accrualPeriodicity-->  <freq:URI>
```

| 원본 값 | 매핑 URI |
|---------|----------|
| 일간 | `http://publications.europa.eu/resource/authority/frequency/DAILY` |
| 주간 | `.../WEEKLY` |
| 월간 | `.../MONTHLY` |
| 분기 | `.../QUARTERLY` |
| 반기 | `.../ANNUAL_2` |
| 연간 | `.../ANNUAL` |
| 수시 | `.../IRREG` |

### B-6. 이용허락범위 — **v2.0 보강**

**컬럼**: #29 이용허락범위

```
Distribution  --dct:license-->  <https://data.go.kr/license/kogl/type-{N}>
```

| 원본 패턴 | 매핑 URI |
|----------|----------|
| 이용허락범위 제한 없음 | `https://data.go.kr/license/kogl/type-1` |
| 자유이용 (제 0유형) | `https://data.go.kr/license/kogl/type-0` |
| 출처표시 (제 1유형) | `https://data.go.kr/license/kogl/type-1` |
| 출처표시, 상업적 이용금지 (제 2유형) | `https://data.go.kr/license/kogl/type-2` |
| 출처표시, 변경금지 (제 3유형) | `https://data.go.kr/license/kogl/type-3` |
| 출처표시, 상업적 이용금지, 변경금지 (제 4유형) | `https://data.go.kr/license/kogl/type-4` |

제3자 권리 포함인 경우 `aird:hasThirdPartyRights true` 추가

**v2.0 추가**: 각 License 리소스에 KOGL 공식 URI 연결

```
<https://data.go.kr/license/kogl/type-{N}>  a dct:LicenseDocument
  --dct:title-->    "공공누리 제{N}유형"@ko
  --rdfs:seeAlso--> <https://www.kogl.or.kr/info/license.do#type-{N}>
```

### B-7. 비용 정보

**컬럼**: #27 비용부과유무, #28 비용부과기준 및 단위

```
Distribution  --schema:isAccessibleForFree-->  true/false  (xsd:boolean)

(유료인 경우)
Distribution  --schema:offers-->  _:offer  a schema:Offer
  --schema:description-->  "{비용부과기준 및 단위}"@ko
```

### B-8. 이용통계

**컬럼**: #18 다운로드_활용신청건수, #33 조회수

```
Dataset  --schema:interactionStatistic-->  _:stat  a schema:InteractionCounter
  --schema:interactionType-->      schema:DownloadAction (또는 schema:ViewAction)
  --schema:userInteractionCount--> "{값}"^^xsd:integer
```

### B-9. 데이터 한계 (품질)

**컬럼**: #21 데이터 한계

```
Dataset  --dqv:hasQualityAnnotation-->  _:qa  a dqv:QualityAnnotation
  --rdfs:comment-->  "{데이터 한계}"@ko
```

### B-10. 공간범위 / 시간범위

**컬럼**: #25 공간범위, #26 시간범위

```
Dataset  --dct:spatial-->   _:loc  a dct:Location
  --rdfs:label-->  "{공간범위}"@ko

Dataset  --dct:temporal-->  _:period  a dct:PeriodOfTime
  --rdfs:label-->  "{시간범위}"@ko
```

<!-- TODO: spec-pending — 향후 행정구역코드 URI, startDate/endDate 파싱 적용 예정 -->

### B-11. 매체유형 / 확장자 — **v2.0 변경**

**컬럼**: #14 매체유형, #16 확장자(데이터포맷)

**v1.0 문제**: `dcat:mediaType`에 `"text"`, `"image"` 등 비표준 값 사용 — DCAT 스펙 위반

**v2.0**: 확장자 기반 IANA 미디어 타입 매핑 테이블 도입

```
Distribution  --dcat:mediaType-->  "{IANA 미디어 타입}"
Distribution  --dct:format-->      "{확장자소문자}"
```

#### IANA 미디어 타입 매핑 (확장자 → 미디어 타입)

| 확장자 | IANA 미디어 타입 |
|--------|----------------|
| csv | `text/csv` |
| json | `application/json` |
| xml | `application/xml` |
| xlsx | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| xls | `application/vnd.ms-excel` |
| pdf | `application/pdf` |
| hwp | `application/x-hwp` |
| hwpx | `application/hwp+zip` |
| zip | `application/zip` |
| html | `text/html` |
| txt | `text/plain` |
| doc | `application/msword` |
| docx | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` |
| ppt | `application/vnd.ms-powerpoint` |
| pptx | `application/vnd.openxmlformats-officedocument.presentationml.presentation` |
| jpg, jpeg | `image/jpeg` |
| png | `image/png` |
| gif | `image/gif` |
| tif, tiff | `image/tiff` |
| shp | `application/x-shapefile` |
| geojson | `application/geo+json` |
| rdf | `application/rdf+xml` |

매핑 테이블에 없는 확장자: `dcat:mediaType` 트리플 미생성, `dct:format`만 기록

**v1.0의 매체유형 컬럼(#14) 처리 변경**: 더 이상 `dcat:mediaType` 값으로 사용하지 않음. 대신 확장자와 매체유형이 불일치하는 경우 검증 로그를 출력.

### B-12. 제공형태

**컬럼**: #22 제공형태

```
Distribution  --aird:accessMethod-->  <https://data.go.kr/accessMethod/{slug}>  a skos:Concept
  --skos:prefLabel-->  "{제공형태}"@ko
```

### B-13. API 관련 (DataService)

**컬럼**: #30 API 유형, #31 신청가능 트래픽, #32 심의 유형

목록유형 = API인 경우에만 생성:

```
Distribution  --dcat:accessService-->  _:svc  a dcat:DataService
  --dct:type-->            "{API유형}" (REST, LINK, SOAP)
  --aird:trafficLimit-->   "{신청가능 트래픽}"@ko
  --aird:approvalType-->   "{심의 유형}"@ko
```

---

## C. RDF 구조 모델

```
dcat:Catalog  (공공데이터포털)
 │
 ├─ dcat:themeTaxonomy ──→ skos:ConceptScheme (분류체계)
 ├─ dcat:themeTaxonomy ──→ skos:ConceptScheme (목록유형)
 │
 └─ dcat:dataset ──→  dcat:Dataset
      │
      ├─ [직접 속성]
      │   dct:identifier, dct:title, dct:description,
      │   dcat:keyword(多), dct:issued, dct:modified,
      │   dcat:landingPage, rdfs:comment,
      │   dct:references (보유근거),
      │   aird:collectionMethod (수집방법),
      │   dct:conformsTo (표준데이터 해당 시),        ← v2.0 변경
      │   aird:nextUpdateDate, aird:isNationalCoreDataset
      │
      ├─ [통제어휘 연결]
      │   dct:type ──→ skos:Concept (목록유형)
      │   dcat:theme ──→ skos:Concept (대분류 + 소분류)  ← v2.0 변경
      │   dct:accrualPeriodicity ──→ dct:Frequency (EU 코드)
      │
      ├─ [조직/연락처]
      │   dct:publisher ──→ foaf:Organization
      │   dcat:contactPoint ──→ vcard:Kind
      │
      ├─ [품질/통계]
      │   dqv:hasQualityAnnotation ──→ dqv:QualityAnnotation
      │   schema:interactionStatistic ──→ schema:InteractionCounter (x2)
      │
      ├─ [공간/시간]
      │   dct:spatial ──→ dct:Location
      │   dct:temporal ──→ dct:PeriodOfTime
      │
      └─ dcat:distribution ──→ dcat:Distribution
           │   dct:title, dct:format,
           │   dcat:mediaType (IANA 표준),              ← v2.0 변경
           │   dct:license ──→ dct:LicenseDocument,     ← v2.0 보강
           │   schema:isAccessibleForFree,
           │   aird:rowCount, aird:accessMethod,
           │   schema:offers ──→ schema:Offer
           │
           └─ (API인 경우)
               dcat:accessService ──→ dcat:DataService
                   dct:type, aird:trafficLimit,
                   aird:approvalType
```

---

## D. 전처리 (변환 시 내장)

1. 결측값: `"-"`, `""` → null → 해당 트리플 미생성
2. 확장자: 소문자 정규화 + 오타 수정 (xlxs→xlsx, cvs→csv)
3. 설명: HTML 태그 제거
4. 전화번호: 백틱(`` ` ``) 제거
5. 이용허락범위: KOGL 유형코드 추출 → URI 매핑
6. 비용부과유무: 무료→true, 유료→false, -→null
7. **매체유형 검증**: 매체유형 컬럼과 확장자 기반 IANA 타입의 대분류 일치 여부 로그 출력 (v2.0 추가)

---

## E. 커스텀 어휘 목록 (aird 네임스페이스)

v2.0에서 최소화된 커스텀 속성 목록. 표준 어휘에 적절한 대안이 없는 경우에만 사용.

| 속성 | 도메인 | 레인지 | 설명 |
|------|--------|--------|------|
| `aird:collectionMethod` | `dcat:Dataset` | `rdf:langString` | 수집방법 (크롤링, 조사, 센서 등) |
| `aird:nextUpdateDate` | `dcat:Dataset` | `xsd:date` | 차기 등록 예정일 |
| `aird:rowCount` | `dcat:Distribution` | `xsd:integer` | 테이블형 데이터 전체 행 수 |
| `aird:isNationalCoreDataset` | `dcat:Dataset` | `xsd:boolean` | 국가중점데이터 여부 |
| `aird:accessMethod` | `dcat:Distribution` | `skos:Concept` | 제공형태 (포털 다운로드, 기관 URL 등) |
| `aird:hasThirdPartyRights` | `dcat:Distribution` | `xsd:boolean` | 제3자 권리 포함 여부 |
| `aird:trafficLimit` | `dcat:DataService` | `rdf:langString` | API 신청가능 트래픽 |
| `aird:approvalType` | `dcat:DataService` | `rdf:langString` | API 심의 유형 |

### v2.0에서 제거된 커스텀 속성

| 제거된 속성 | 대체 | 사유 |
|------------|------|------|
| `aird:isStandardDataset` | `dct:conformsTo` | DCMI 표준 준수 관계 속성 |
