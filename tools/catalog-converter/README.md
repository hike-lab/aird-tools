# catalog-converter

공공데이터포털 목록개방현황 CSV를 DCAT(Data Catalog Vocabulary) 기반 RDF로 변환하는 도구

## 개요

공공데이터활용지원센터에서 제공하는 **공공데이터포털 목록개방현황** 데이터(CSV)를 DCAT 어휘 기반의 RDF(JSON-LD, Turtle, N-Triples)로 변환합니다. AI-Ready Data 표준(Part 2: 메타데이터 프로파일)의 DCAT 매핑을 구현한 첫 번째 도구입니다.

> 기본 수준의 초기 변환입니다. 표준 확정에 따라 업데이트 예정입니다.

- 36개 CSV 컬럼을 DCAT, DCT, SKOS, FOAF, VCARD, Schema.org, DQV 등 표준 어휘로 매핑
- 6가지 기본 데이터 정제 적용
- JSON-LD, Turtle, N-Triples 출력 (전체 95,544건 -> 약 4백만 트리플)

## 데이터 원본

- **데이터명**: 공공데이터활용지원센터_공공데이터포털 목록개방현황
- **출처**: https://www.data.go.kr/data/15062804/fileData.do
- **기준일**: 2026-02-28
- **규모**: 95,544건, 36개 컬럼
- **이용조건**: 공공누리(KOGL)

원본 CSV(126MB)는 저장소에 포함되어 있지 않습니다. 위 링크에서 다운로드 후 `data/` 디렉토리에 배치하세요.

## 사용법

```bash
cd tools/catalog-converter
pip install -r requirements.txt

# 전체 변환 (약 4백만 트리플, 500MB+ 출력, 수 분 소요)
python src/converter.py

# 건수 제한 (테스트용)
python src/converter.py 100
```

출력 파일은 `output/` 디렉토리에 생성됩니다.

## 사용 어휘

| Prefix | 네임스페이스 | 용도 |
|--------|------------|------|
| dcat | http://www.w3.org/ns/dcat# | 데이터 카탈로그 핵심 구조 |
| dct | http://purl.org/dc/terms/ | 메타데이터 속성 |
| skos | http://www.w3.org/2004/02/skos/core# | 분류체계, 통제어휘 |
| foaf | http://xmlns.com/foaf/0.1/ | 조직 |
| vcard | http://www.w3.org/2006/vcard/ns# | 연락처 |
| schema | http://schema.org/ | 이용통계, 비용 |
| dqv | http://www.w3.org/ns/dqv# | 데이터 품질 |
| aird | http://datahub.kr/ns/aird# | AI-Ready Data 커스텀 속성 |

## 문서

- [DCAT 매핑 명세](docs/dcat-mapping-spec.md) — 36개 컬럼 전체 매핑 규격
- [데이터 정제 계획](docs/data-cleansing-plan.md) — 정제 항목 및 향후 과제
