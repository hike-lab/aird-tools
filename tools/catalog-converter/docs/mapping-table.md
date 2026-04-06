# 어휘 매핑 테이블 v2.0

공공데이터포털 목록개방현황 CSV 36개 컬럼 → RDF 매핑 결과 요약.
상세 규격은 [vocabulary-mapping-spec.md](vocabulary-mapping-spec.md) 참조.

## 전체 매핑 테이블

| # | CSV 컬럼 | RDF 속성 | 대상 클래스 | 값 타입 / 범위 | 매핑 유형 | 비고 |
|---|----------|----------|------------|---------------|----------|------|
| 1 | 목록키 | `dct:identifier` | `dcat:Dataset` | `xsd:string` | 직접 | |
| 2 | 목록유형 | `dct:type` | `dcat:Dataset` | `skos:Concept` | 통제어휘 | FILE, API, STD → ConceptScheme |
| 3 | 목록명 | `dct:title` | `dcat:Dataset` | `rdf:langString @ko` | 직접 | |
| 4 | 파일데이터명 | `dct:title` | `dcat:Distribution` | `rdf:langString @ko` | 직접 | |
| 5 | 분류체계 | `dcat:theme` | `dcat:Dataset` | `skos:Concept` | 통제어휘 | "대분류 - 소분류" → 대·소 모두 연결, SKOS 계층 |
| 6 | 제공기관코드 | `dct:identifier` | `foaf:Organization` | `xsd:string` | 중간노드 | Publisher URI 생성 |
| 7 | 제공기관 | `foaf:name` | `foaf:Organization` | `rdf:langString @ko` | 중간노드 | |
| 8 | 관리 부서명 | `vcard:fn` | `vcard:Kind` | `rdf:langString @ko` | 중간노드 | ContactPoint |
| 9 | 관리부서 전화번호 | `vcard:hasTelephone` | `vcard:Kind` | `xsd:anyURI` | 중간노드 | `tel:` URI, 백틱 제거 |
| 10 | 보유근거 | `dct:references` | `dcat:Dataset` | `rdf:langString @ko` | 직접 | 법적 근거 |
| 11 | 수집방법 | `aird:collectionMethod` | `dcat:Dataset` | `rdf:langString @ko` | 직접 | 커스텀 속성 |
| 12 | 업데이트 주기 | `dct:accrualPeriodicity` | `dcat:Dataset` | `dct:Frequency` (URI) | 통제어휘 | EU frequency authority URI |
| 13 | 차기 등록 예정일 | `aird:nextUpdateDate` | `dcat:Dataset` | `xsd:date` | 직접 | 커스텀 속성 |
| 14 | 매체유형 | *(검증용)* | — | — | — | `dcat:mediaType` 값으로 사용하지 않음. 확장자 기반 IANA 타입과 교차 검증 |
| 15 | 전체행 | `aird:rowCount` | `dcat:Distribution` | `xsd:integer` | 직접 | 커스텀 속성 |
| 16 | 확장자(데이터포맷) | `dct:format` + `dcat:mediaType` | `dcat:Distribution` | `xsd:string` + IANA 미디어 타입 | 직접 | 소문자 정규화, 오타 수정. IANA 매핑 테이블 기반 |
| 17 | 키워드 | `dcat:keyword` | `dcat:Dataset` | `rdf:langString @ko` | 직접 | 쉼표 분리 → 다중 트리플 |
| 18 | 다운로드_활용신청건수 | `schema:interactionStatistic` | `dcat:Dataset` | `schema:InteractionCounter` | 중간노드 | `interactionType: DownloadAction` |
| 19 | 등록일 | `dct:issued` | `dcat:Dataset` | `xsd:date` | 직접 | |
| 20 | 수정일 | `dct:modified` | `dcat:Dataset` | `xsd:date` | 직접 | |
| 21 | 데이터 한계 | `dqv:hasQualityAnnotation` | `dcat:Dataset` | `dqv:QualityAnnotation` | 중간노드 | `rdfs:comment`로 기술 |
| 22 | 제공형태 | `aird:accessMethod` | `dcat:Distribution` | `skos:Concept` | 통제어휘 | 커스텀 속성, ConceptScheme |
| 23 | 설명 | `dct:description` | `dcat:Dataset` | `rdf:langString @ko` | 직접 | HTML 태그 제거 |
| 24 | 기타 유의사항 | `rdfs:comment` | `dcat:Dataset` | `rdf:langString @ko` | 직접 | |
| 25 | 공간범위 | `dct:spatial` | `dcat:Dataset` | `dct:Location` | 중간노드 | `rdfs:label`로 기술. 향후 행정구역코드 URI 예정 |
| 26 | 시간범위 | `dct:temporal` | `dcat:Dataset` | `dct:PeriodOfTime` | 중간노드 | `rdfs:label`로 기술. 향후 startDate/endDate 파싱 예정 |
| 27 | 비용부과유무 | `schema:isAccessibleForFree` | `dcat:Distribution` | `xsd:boolean` | 직접 | 무료→true, 유료→false |
| 28 | 비용부과기준 및 단위 | `schema:offers` | `dcat:Distribution` | `schema:Offer` | 중간노드 | 유료인 경우만 생성 |
| 29 | 이용허락범위 | `dct:license` | `dcat:Distribution` | `dct:LicenseDocument` (URI) | 통제어휘 | KOGL type-0~4, `rdfs:seeAlso`로 공식 URI 연결 |
| 30 | API 유형 | `dct:type` | `dcat:DataService` | `xsd:string` | 중간노드 | REST, LINK, SOAP. API인 경우만 |
| 31 | 신청가능 트래픽 | `aird:trafficLimit` | `dcat:DataService` | `rdf:langString @ko` | 직접 | 커스텀 속성. API인 경우만 |
| 32 | 심의 유형 | `aird:approvalType` | `dcat:DataService` | `rdf:langString @ko` | 직접 | 커스텀 속성. API인 경우만 |
| 33 | 조회수 | `schema:interactionStatistic` | `dcat:Dataset` | `schema:InteractionCounter` | 중간노드 | `interactionType: ViewAction` |
| 34 | 목록 URL | `dcat:landingPage` | `dcat:Dataset` | `xsd:anyURI` | 직접 | |
| 35 | 국가중점여부 | `aird:isNationalCoreDataset` | `dcat:Dataset` | `xsd:boolean` | 직접 | 커스텀 속성. Y→true, N→false |
| 36 | 표준데이터여부 | `dct:conformsTo` | `dcat:Dataset` | `dct:Standard` (URI) | 통제어휘 | Y→URI 생성, N→트리플 미생성 |

## 매핑 유형별 분류

### 직접 매핑 (18건)

CSV 값을 리터럴 또는 URI로 직접 변환.

| CSV 컬럼 | RDF 속성 |
|----------|----------|
| 목록키 | `dct:identifier` |
| 목록명 | `dct:title` (Dataset) |
| 파일데이터명 | `dct:title` (Distribution) |
| 키워드 | `dcat:keyword` |
| 등록일 | `dct:issued` |
| 수정일 | `dct:modified` |
| 설명 | `dct:description` |
| 기타 유의사항 | `rdfs:comment` |
| 목록 URL | `dcat:landingPage` |
| 보유근거 | `dct:references` |
| 수집방법 | `aird:collectionMethod` |
| 차기 등록 예정일 | `aird:nextUpdateDate` |
| 전체행 | `aird:rowCount` |
| 국가중점여부 | `aird:isNationalCoreDataset` |
| 비용부과유무 | `schema:isAccessibleForFree` |
| 확장자(데이터포맷) | `dct:format` + `dcat:mediaType` |
| 신청가능 트래픽 | `aird:trafficLimit` |
| 심의 유형 | `aird:approvalType` |

### 통제어휘 매핑 (6건)

값을 URI/Concept으로 변환하여 통제어휘에 연결.

| CSV 컬럼 | RDF 속성 | 대상 어휘 |
|----------|----------|----------|
| 목록유형 | `dct:type` | 자체 ConceptScheme (FILE/API/STD) |
| 분류체계 | `dcat:theme` | 자체 SKOS 계층 (대분류·소분류) |
| 업데이트 주기 | `dct:accrualPeriodicity` | EU frequency authority |
| 이용허락범위 | `dct:license` | KOGL type-0~4 |
| 제공형태 | `aird:accessMethod` | 자체 ConceptScheme |
| 표준데이터여부 | `dct:conformsTo` | 자체 Standard URI |

### 중간노드 매핑 (11건)

하나 이상의 컬럼 → 구조화된 RDF 서브 리소스 생성.

| CSV 컬럼 | 생성 리소스 | 연결 속성 |
|----------|------------|----------|
| 제공기관코드 + 제공기관 | `foaf:Organization` | `dct:publisher` |
| 관리 부서명 + 전화번호 | `vcard:Kind` | `dcat:contactPoint` |
| 다운로드_활용신청건수 | `schema:InteractionCounter` | `schema:interactionStatistic` |
| 조회수 | `schema:InteractionCounter` | `schema:interactionStatistic` |
| 데이터 한계 | `dqv:QualityAnnotation` | `dqv:hasQualityAnnotation` |
| 공간범위 | `dct:Location` | `dct:spatial` |
| 시간범위 | `dct:PeriodOfTime` | `dct:temporal` |
| 비용부과기준 및 단위 | `schema:Offer` | `schema:offers` |
| API 유형 + 트래픽 + 심의유형 | `dcat:DataService` | `dcat:accessService` |

### 검증 전용 (1건)

| CSV 컬럼 | 용도 |
|----------|------|
| 매체유형 | 확장자 기반 IANA 타입과 교차 검증 (트리플 미생성) |

## 사용 어휘 통계

| 어휘 | 사용 속성 수 | 속성 목록 |
|------|------------|----------|
| `dct` (Dublin Core) | 11 | identifier, title, description, issued, modified, references, source, type, accrualPeriodicity, license, conformsTo, format, spatial, temporal |
| `dcat` | 7 | keyword, landingPage, theme, contactPoint, distribution, mediaType, accessService |
| `schema` | 4 | isAccessibleForFree, offers, interactionStatistic, interactionType |
| `aird` (커스텀) | 8 | collectionMethod, nextUpdateDate, rowCount, isNationalCoreDataset, accessMethod, hasThirdPartyRights, trafficLimit, approvalType |
| `skos` | 4 | prefLabel, broader, topConceptOf, inScheme |
| `foaf` | 2 | Organization (class), name |
| `vcard` | 3 | Kind (class), fn, hasTelephone |
| `dqv` | 2 | hasQualityAnnotation, QualityAnnotation (class) |
| `rdfs` | 2 | comment, label, seeAlso |
