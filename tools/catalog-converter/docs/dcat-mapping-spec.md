# DCAT 매핑 명세 v1.0

## 개요

공공데이터포털 목록개방현황 CSV(36개 컬럼)를 DCAT 기반 RDF로 변환하기 위한 매핑 규격.

## 사용 어휘 (Prefix)

| Prefix | URI |
|--------|-----|
| `dcat` | `http://www.w3.org/ns/dcat#` |
| `dct` | `http://purl.org/dc/terms/` |
| `vcard` | `http://www.w3.org/2006/vcard/ns#` |
| `foaf` | `http://xmlns.com/foaf/0.1/` |
| `schema` | `http://schema.org/` |
| `adms` | `http://www.w3.org/ns/adms#` |
| `dqv` | `http://www.w3.org/ns/dqv#` |
| `skos` | `http://www.w3.org/2004/02/skos/core#` |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` |
| `rdfs` | `http://www.w3.org/2000/01/rdf-schema#` |
| `aird` | `http://datahub.kr/ns/aird#` |

---

## A. 직접 속성 매핑 (컬럼 → literal/URI 1:1)

| # | CSV 컬럼 | 대상 클래스 | RDF 속성 | 값 타입 | 비고 |
|---|----------|------------|----------|---------|------|
| 1 | 목록키 | `dcat:Dataset` | `dct:identifier` | `xsd:string` | |
| 3 | 목록명 | `dcat:Dataset` | `dct:title` | `rdf:langString` | `@ko` |
| 4 | 파일데이터명 | `dcat:Distribution` | `dct:title` | `rdf:langString` | `@ko` |
| 17 | 키워드 | `dcat:Dataset` | `dcat:keyword` | `rdf:langString` | 쉼표 분리 → 다중 트리플, `@ko` |
| 19 | 등록일 | `dcat:Dataset` | `dct:issued` | `xsd:date` | |
| 20 | 수정일 | `dcat:Dataset` | `dct:modified` | `xsd:date` | |
| 23 | 설명 | `dcat:Dataset` | `dct:description` | `rdf:langString` | `@ko`, HTML 태그 제거 |
| 24 | 기타 유의사항 | `dcat:Dataset` | `rdfs:comment` | `rdf:langString` | `@ko` |
| 34 | 목록 URL | `dcat:Dataset` | `dcat:landingPage` | `xsd:anyURI` | |
| 15 | 전체행 | `dcat:Distribution` | `aird:rowCount` | `xsd:integer` | 커스텀 속성 |
| 13 | 차기 등록 예정일 | `dcat:Dataset` | `aird:nextUpdateDate` | `xsd:date` | 커스텀 속성 |
| 35 | 국가중점여부 | `dcat:Dataset` | `aird:isNationalCoreDataset` | `xsd:boolean` | N→false, Y→true |
| 36 | 표준데이터여부 | `dcat:Dataset` | `aird:isStandardDataset` | `xsd:boolean` | N→false, Y→true |
| 10 | 보유근거 | `dcat:Dataset` | `dct:references` | `rdf:langString` | `@ko`, 법적 근거 |
| 11 | 수집방법 | `dcat:Dataset` | `aird:collectionMethod` | `rdf:langString` | `@ko`, 커스텀 속성 |

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
Dataset  --dcat:contactPoint-->  _:cp  a vcard:Organization
  --vcard:fn-->              "{관리 부서명}"@ko
  --vcard:hasTelephone-->    <tel:{전화번호}>  a vcard:Voice
```

전화번호: 백틱 제거, `tel:` URI 스킴

### B-3. Theme (분류체계)

**컬럼**: #5 분류체계 — `"대분류 - 소분류"` 패턴 (100% 2파트)

```
Dataset  --dcat:theme-->  <https://data.go.kr/theme/{소분류slug}>  a skos:Concept
  --skos:prefLabel-->  "{소분류}"@ko
  --skos:broader-->    <https://data.go.kr/theme/{대분류slug}>

<https://data.go.kr/theme/{대분류slug}>  a skos:Concept
  --skos:prefLabel-->       "{대분류}"@ko
  --skos:topConceptOf-->    <https://data.go.kr/theme>

<https://data.go.kr/theme>  a skos:ConceptScheme
  --dct:title-->  "공공데이터 분류체계"@ko
```

### B-4. 목록유형

**컬럼**: #2 목록유형 — FILE, API, STD

```
Dataset  --dct:type-->  <https://data.go.kr/type/{값}>  a skos:Concept
  --skos:prefLabel-->  "{값}"@ko
  --skos:inScheme-->   <https://data.go.kr/type>
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

### B-6. 이용허락범위

**컬럼**: #29 이용허락범위

```
Distribution  --dct:license-->  <license:URI>
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

향후: 공간범위 → 행정구역코드 URI, 시간범위 → startDate/endDate 파싱

### B-11. 매체유형 / 확장자

**컬럼**: #14 매체유형, #16 확장자(데이터포맷)

```
Distribution  --dcat:mediaType-->  "{IANA타입}"
Distribution  --dct:format-->      "{확장자소문자}"
```

매체유형 매핑: 텍스트→text, 이미지→image, 동영상→video, 소리→audio, 기타/멀티미디어→그대로

확장자: 소문자 정규화, 오타 수정 (xlxs→xlsx, cvs→csv)

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
  --dct:type-->              "{API유형}" (REST, LINK, SOAP)
  --aird:trafficLimit-->    "{신청가능 트래픽}"@ko
  --aird:approvalType-->    "{심의 유형}"@ko
```

---

## C. RDF 구조 모델

```
dcat:Catalog  (공공데이터포털)
 │
 └─ dcat:dataset ──→  dcat:Dataset
      │
      ├─ [직접 속성]
      │   dct:identifier, dct:title, dct:description,
      │   dcat:keyword(多), dct:issued, dct:modified,
      │   dcat:landingPage, rdfs:comment,
      │   dct:references (보유근거),
      │   aird:nextUpdateDate, aird:isNationalCoreDataset,
      │   aird:isStandardDataset, aird:collectionMethod
      │
      ├─ [통제어휘 연결]
      │   dct:type ──→ skos:Concept (목록유형)
      │   dcat:theme ──→ skos:Concept (분류체계, broader/narrower)
      │   dct:accrualPeriodicity ──→ dct:Frequency (EU 코드)
      │
      ├─ [조직/연락처]
      │   dct:publisher ──→ foaf:Organization
      │   dcat:contactPoint ──→ vcard:Organization
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
           │   dct:title, dct:format, dcat:mediaType,
           │   dct:license, schema:isAccessibleForFree,
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
2. 확장자: 소문자 정규화 + 오타 수정
3. 설명: HTML 태그 제거
4. 전화번호: 백틱(`) 제거
5. 이용허락범위: KOGL 유형코드 추출 → URI 매핑
6. 비용부과유무: 무료→true, 유료→false, -→null
