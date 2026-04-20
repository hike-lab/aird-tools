# AI-Ready Data Metadata Profile
## AI-Ready Data Metadata Profile

| 항목 | 내용 |
|---|---|
| 문서 번호 | AIRD-STD-002 |
| 버전 | **v0.1** |
| 최초 제정일 | 2026-04-14 |
| 최종 개정일 | 2026-04-14 |
| 분류 | 표준 (초안) |
| 상태 | 초안 |

### 개정 이력

| 버전 | 일자 | 주요 변경 내용 |
|---|---|---|
| **v0.1** | **2026-04-14** | **최초 제정** |

### 표준 시리즈 구성

| 문서 번호 | 표준명 | 역할 |
|---|---|---|
| AIRD-STD-001 | Quality-Ready Data Preparation Framework | 품질 측정·판정·등급 체계 — 원칙·공식 |
| **AIRD-STD-002** | **AI-Ready Data Metadata Profile (본 표준)** | 메타데이터 항목·레이어·스키마 — 기술·기록 |
| AIRD-STD-003 | AI-Ready Data Transformation & Governance Specification | ETL 파이프라인·AIRD Pack·거버넌스 — 실행·운영 |
| AIRD-STD-005 | AI-Ready Data Discovery & Exchange Specification | Pack 탐색 API·에이전트 인터페이스 — 교환 |
| AIRD-OPG-001 | 품질 진단 운영 지침 *(예정)* | 진단 주기·유효기간·이의제기·도구 인증 — 운영 세부 |
| AIRD-TR-001 | 가중치 설계 기술 보고서 *(예정)* | Purpose-Type별 가중치 수치 근거 |

---

## 목차

1. 개요
2. 데이터 상태 모델 및 메타데이터 계층 아키텍처
3. Layer 1: Discovery Metadata
4. Layer 2: Understanding Metadata
5. Layer 3: Operability Metadata
6. 계층 간 연결 메커니즘
7. 제어 어휘 및 검증
8. 적합성 프레임워크
9. 필드 매핑 테이블
10. 구현 로드맵
11. 부록 A: 국내 공공데이터 구현 참고 (참고)
12. 부록 B: JSON-LD 예제
13. 부록 C: 표준 간 참조 매트릭스 (참고)

---

## 1. 개요

### 1.1 목적

본 표준은 AI 활용 목적으로 준비된 데이터셋(AI-Ready Data)을 기술(describe)하는 메타데이터의 기계 판독 가능한 스키마 규격을 정의한다. 데이터셋의 발견·접근·품질·운용 정보를 국제 표준 어휘로 형식화하고, 다양한 AI 데이터 유형(ML, DL, RAG, KG, Stats, FineTuning)에 대응하는 멀티 프로파일 체계를 수립한다.

본 표준은 특정 행정 지침의 하위 규격이 아닌 **독립적 기술 표준**으로 설계되었다. Quality-Ready Data Preparation Framework(AIRD-STD-001)의 메타데이터 모델을 국제 표준 어휘로 형식화하고, AIRD-STD-001이 다루지 않는 Purpose-Ready 상태의 메타데이터 규격(Layer 3)을 추가로 정의한다. 국내 공공데이터 관리체계와의 연계 방안은 부록 A(참고)에서 별도로 다룬다.

### 1.2 적용 범위

본 표준은 다음을 기본 적용 대상으로 한다.

- **필수 적용:** 공공기관이 제공하는 데이터셋 (Raw, Quality-Ready, Purpose-Ready 상태 모두 포함)
- **준용 권장(MAY):** AI 학습·운용 목적의 민간 데이터셋, 연구기관 데이터셋, 기업 내부 데이터 카탈로그

본 표준의 기술적 내용 — 3계층 메타데이터 아키텍처, Purpose-Type별 프로파일, 국제 표준 어휘 매핑 — 은 데이터의 출처(공공/민간)와 무관하게 적용 가능하다. 공공기관 필수 적용 의무의 법적 근거는 부록 A를 참조한다.

### 1.3 국제 표준과의 관계

본 표준이 적용하는 국제 표준 어휘는 각기 다른 목적을 가지며, 3계층 아키텍처로 역할을 분리하여 통합한다.

| 국제 표준 | 계층 | 역할 |
|---|---|---|
| DCAT v3 + Dublin Core | Layer 1 | 데이터셋 발견·접근·권리 확인을 위한 카탈로그 메타데이터 |
| W3C DQV + PROV-O | Layer 2 | 품질 측정값 기록 및 데이터 생성·변환 이력 추적 |
| W3C CSVW | Layer 2 (정형 데이터) | CSV 등 테이블형 데이터의 컬럼 스키마 기술 |
| Croissant 1.0 | Layer 3 (ML/DL, RAG) | ML 프레임워크에서 직접 로딩 가능한 데이터셋 기술 |
| VoID | Layer 3 (KG) | RDF/트리플 기반 지식그래프 구조 기술 |
| SDMX | Layer 3 (Stats) | 다차원 통계 큐브 구조 기술 |

이 표준들은 서로 목적이 달라 단일 표준으로 통합할 수 없다. 본 표준은 이를 계층화하고 상호 참조 메커니즘을 정의하여 일관된 명세로 구성한다.

### 1.4 관련 표준과의 연계

| 표준 | 역할 |
|---|---|
| Quality-Ready Data Preparation Framework (AIRD-STD-001) | 품질 진단·측정 방법론 정의. 진단 결과가 Layer 2 품질 메타데이터로 기록됨. Raw/Quality-Ready 2단계 메타데이터 모델의 원천. |
| AI-Ready Data Metadata Profile (AIRD-STD-002, 본 표준) | AIRD-STD-001의 메타데이터 모델을 국제 표준 어휘로 형식화하고, Layer 3(Operability) 메타데이터를 추가 정의. |
| AI-Ready Data Transformation & Governance Specification (AIRD-STD-003) | 파이프라인 실행 시 Layer 2 프로브넌스 및 Layer 3 메타데이터 자동 생성. |
| AI-Ready Data Discovery & Exchange Specification (AIRD-STD-005) | Pack 탐색 API, 교환 규격, 에이전트 인터페이스 정의. 본 표준의 purposeReadinessVector를 탐색 필터로 사용. |

### 1.5 용어 정의

**1.5.1 Raw Data**
원본 상태의 데이터. 품질 진단이 수행되지 않은 상태.

**1.5.2 Quality-Ready Data**
6개 품질 차원에 대한 진단이 완료되고, QI(Quality Index)가 산출된 데이터. AIRD-STD-001 3.1절 정의를 따른다.

**1.5.3 Purpose-Ready Data**
특정 AI 활용 목적(ML, RAG, KG, Stats 등)에 최적화된 형태로 변환된 데이터.

**1.5.4 품질 지수 (Quality Index, QI)**
6개 품질 차원 점수를 가중 합산하여 산출하는 데이터셋 수준의 종합 품질 점수 (0.0–1.0). 산정 방법은 AIRD-STD-001 6장을 따른다.

**1.5.5 Q-Tier**
QI 및 필수 게이트 조건에 따라 결정되는 품질 등급. Tier 1(Bronze)~Tier 4(Platinum). 판정 기준은 AIRD-STD-001 7장을 따른다.

**1.5.6 Purpose-Type**
AI 활용 목적 분류. ML, DL, RAG, KG, Stats, FineTuning 등.

**1.5.7 AIRD Pack**
Purpose-Ready 상태의 데이터 패키지 (데이터 + Layer 3 메타데이터).

**1.5.8 메타데이터 상태 (metadata.status)**
데이터셋의 현재 상태를 선언하는 메타데이터 필드. Raw / Quality-Ready / Purpose-Ready / Stale 4개 값.

**1.5.9 적용 주체**
본 표준을 적용하는 기관 또는 조직 (공공기관, 연구기관, 민간 기업 등).

**1.5.10 모델-데이터 결합도 (Model-Data Coupling)**
Purpose-Type에 따른 데이터와 AI 모델 간의 논리적 의존 관계 수준. Loose(데이터 독립) / Derived(모델 산출물이 Pack 구성에 포함) / Tight(모델 없이 실행 불가) 3단계로 분류한다.

**1.5.11 Pack 완전성 (Pack Completeness)**
AIRD Pack이 포함하는 산출물의 범위를 선언하는 속성. `data-only` / `derived-without-model` / `derived-with-model` / `full-reproducible` 4개 값을 사용한다.

**1.5.12 Stale 상태**
Purpose-Ready 상태이나 원본 데이터 갱신 또는 소비자 피드백으로 재패키징이 필요한 상태. `aird:sourceDataVersion`이 Pack 생성 시점 버전보다 높아진 경우 자동 전이된다.

**1.5.13 소비자 피드백 루프**
데이터 소비자(사람 또는 AI 시스템)가 Pack 활용 중 발견한 문제를 공급자 파이프라인에 신호로 전달하는 구조. 유형 A(구조적 오류) / 유형 B(품질 저하) / 유형 C(데이터 노후화)로 분류한다.

**1.5.14 파생 데이터 (Derived Data)**
AI 모델이 원본 데이터를 변환하여 생성한 결과물(예: 임베딩 벡터, 인덱스). 특정 모델에 논리적으로 종속되며, AIRD Pack에 포함될 수 있으나 모델 파일 자체는 포함되지 않는다.

**1.5.15 참조 프로파일 URI (Transformation Profile URI)**
특정 Purpose-Type의 변환 방법론·성능 기준·구현 가이드를 담은 외부 기술규격을 가리키는 표준화된 URI. 본 표준은 참조 방식만 정의하며 내용은 위임한다.

**1.5.16 Fine-tuning Pack**
LLM을 특정 도메인에 맞게 파인튜닝하기 위한 instruction-response 페어, preference 데이터(DPO), 대화 이력 등을 포함하는 AIRD Pack. Purpose-Type 식별자 `aird-ft`를 사용한다.

### 1.6 표준 어휘 우선 적용 원칙 및 커스텀 어휘 도입 기준

본 표준에서 메타데이터 속성을 정의할 때는 다음 우선순위에 따라 어휘를 선택한다. 커스텀 어휘(`aird:` 네임스페이스)는 국제 표준으로 표현 불가능한 경우에만 도입하며, 도입 시 아래 요건을 충족해야 한다.

| 순위 | 어휘 체계 | 예시 | 비고 |
|---|---|---|---|
| 1순위 | W3C 권고안 (Recommendation) | DCAT, DCT, PROV-O, DQV, ADMS, VCARD, SKOS, RDF, OWL, CSVW | FOAF는 W3C Note이나 DCAT이 normative 인용하므로 1순위에 준함 |
| 2순위 | 광범위하게 채택된 커뮤니티 표준 | Schema.org, Croissant (MLCommons), SDMX (ISO/통계기관 채택), VoID | W3C 권고안은 아니나 사실상 표준으로 광범위하게 사용 |
| 3순위 | AIRD 커스텀 어휘 | `aird:qualityIndex`, `aird:purposeType` 등 | 1~2순위로 표현 불가능한 경우에만 도입 |

**커스텀 어휘 도입 요건:**
- **대체 표준 부재:** 동일 의미를 표현하는 1~2순위 어휘가 존재하지 않음을 명시적으로 확인
- **향후 정렬 계획:** 관련 국제 표준 커뮤니티에 제안하거나, 정렬(alignment) 규칙 제공 일정 명시
- **등록 의무:** 7.1절 제어 어휘 목록에 등재, 8.3절 확장 프로파일 거버넌스 절차 준수

---

## 2. 데이터 상태 모델 및 메타데이터 계층 아키텍처

### 2.1 통합 상태 모델

본 표준은 AIRD-STD-001의 2단계 상태 모델(Raw → Quality-Ready)을 확장하여, 4단계 상태 모델을 정의한다. 각 상태에 대응하는 메타데이터 계층을 명시한다.

| 상태 | metadata.status 값 | 메타데이터 범위 | 전이 조건 |
|---|---|---|---|
| Raw | `"Raw"` | Layer 1 필수 항목만 | 최초 등록 시 기본 상태 |
| Quality-Ready | `"Quality-Ready"` | Layer 1 + Layer 2 | **7.2절 참조 (단일 출처)** |
| Purpose-Ready | `"Purpose-Ready"` | Layer 1 + Layer 2 + Layer 3 | Quality-Ready 상태 + 목적별 프로파일 충족 |
| Stale | `"Stale"` | Layer 1 + Layer 2 + Layer 3 | 자동 전이 조건 참조 (아래) |

> **Quality-Ready 전이 조건은 7.2절(유효성 검증 규칙)에서 단일 출처(normative)로 정의한다.** 본 절 및 4.2.2절은 해당 조건을 요약 참조하며, 충돌 시 7.2절이 우선한다.
>
> **Stale 자동 전이 조건:** 다음 중 하나 이상 충족 시 `metadata.status`를 `"Stale"`로 자동 전이한다(SHOULD).
> 1. `aird:sourceDataVersion`이 Pack 생성 시점에 기록된 버전보다 높은 경우
> 2. 소비자 피드백 유형 C(데이터 노후화) 신호 수신
> 3. `aird:packGeneratedAt`으로부터 `dct:accrualPeriodicity`에 정의된 갱신 주기의 1.5배 이상 경과
>
> Stale 상태의 데이터셋은 Stage 3 재실행(재패키징) 또는 역방향 전이(Quality-Ready 복귀) 중 하나를 택하여야 한다(SHALL).

**상태 전이 규칙 (AIRD-STD-001 연계)**

- Raw 상태의 데이터셋은 품질 점수 필드를 포함해서는 안 된다(SHALL NOT). 품질 점수가 없는 것이 아니라, 명시적으로 금지된다.
- Quality-Ready 전이는 명시적 품질 평가에 의해서만 이루어지며, 자동 전이되지 않는다.
- Purpose-Ready 전이는 Q-Tier와 독립적이다. Bronze 데이터도 특정 Purpose-Type의 요구사항을 충족하면 Purpose-Ready가 될 수 있다.

### 2.2 3계층 메타데이터 아키텍처

AI-Ready 데이터의 메타데이터를 목적과 이용자에 따라 3계층으로 분리한다. 각 계층은 독립적으로 관리되되 상호 참조한다.

| 계층 | 목적 | 기반 표준 | 작동 위치 | 대상 이용자 |
|---|---|---|---|---|
| Layer 1 — Discovery | 데이터셋 발견·접근·권리 확인 | DCAT v3 + Dublin Core | 데이터 카탈로그, 포털 | 모든 이용자 |
| Layer 2 — Understanding | 품질·이력·출처 파악, 활용 적합성 판단 | DQV + PROV-O + DCAT 확장 | 데이터셋 상세 페이지, 데이터 카드 | 분석가·연구자, 정책 담당자 |
| Layer 3 — Operability | AI 도구가 데이터를 파싱·로딩·실행 | Purpose-Type별 멀티 프로파일 | 데이터셋 패키지 내부 (metadata.json 등) | AI 개발자, 자동화 파이프라인 |

**활용 시나리오와의 매핑**

- Layer 1 + 2 → Quality-Ready 상태의 데이터셋 기술
- Layer 1 + 2 + 3 → Purpose-Ready 상태의 AIRD Pack (ML, RAG, KG, Stats, FineTuning) 기술

### 2.3 상태별 메타데이터 포함/제외 규칙

| 메타데이터 항목군 | Raw | Quality-Ready | Purpose-Ready | Stale |
|---|---|---|---|---|
| Layer 1 필수 항목 | 필수 | 필수 | 필수 | 필수 |
| Layer 1 권장/선택 항목 | 선택 | 권장 | 권장 | 권장 |
| Layer 2 품질 점수 | 금지 | 필수 | 필수 | 필수 |
| Layer 2 프로브넌스 | 선택 | 권장 | 필수 | 필수 |
| Layer 3 Operability | 금지 | 금지 | 필수 | 유지 |
| metadata.status | `"Raw"` | `"Quality-Ready"` | `"Purpose-Ready"` | `"Stale"` |
| aird:qualityIndex | 금지 | 필수 | 필수 | 필수 |
| aird:qualityTier | 금지 | 필수 | 필수 | 필수 |
| aird:purposeReadinessVector | 금지 | 선택 | 필수 | 필수 |
| aird:packGeneratedAt | 금지 | 금지 | 필수 | 필수 |
| aird:sourceDataVersion | 금지 | 금지 | 필수 | 필수 |

---

## 3. Layer 1: Discovery Metadata

데이터셋의 발견, 접근, 권리 확인을 위한 카탈로그 수준 메타데이터. DCAT v3 Application Profile을 기반으로 한다.

### 3.1 식별·기술 메타데이터

| 항목명 | 속성 | 구분 | 설명 | 예시 |
|---|---|---|---|---|
| 고유식별자 | `dct:identifier` | 필수 | 변하지 않는 영구 식별자(PID) | `https://example.org/pid/{dataset-id}` |
| 제목(국문) | `dct:title` | 필수 | 데이터셋 명칭 | 서울시 연도별 인구 변화 |
| 제목(영문) | `dct:title@en` | 권장 | 영문 명칭 | Seoul Annual Population Change |
| 설명 | `dct:description` | 필수 | 데이터셋 상세 설명 | |
| 키워드 | `dcat:keyword` | 필수 | 검색용 키워드 (3개 이상) | 인구, 서울, 연도별 |
| 데이터셋 유형 | `dct:type` | 필수 | 정형/이미지/음성/영상/텍스트/지리공간 | `aird:Structured` |
| 주제 분류 | `dcat:theme` | 권장 | 도메인 분류 체계 연계. 공공기관은 BRM 연계 권장 (부록 A 참조) | |
| 언어 | `dct:language` | 필수 | ISO 639-1 언어 코드 | `ko` |
| 시간 범위 | `dct:temporal` | 권장 | 데이터 커버 기간 | `1990-01-01/2025-12-31` |
| 공간 범위 | `dct:spatial` | 권장 | 지리적 커버 범위 | `http://geonames.org/1835848` |
| 메타데이터 상태 | `aird:metadataStatus` | 필수 | Raw / Quality-Ready / Purpose-Ready / Stale | `"Raw"` |

### 3.2 책임·출처 메타데이터

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 생성자 | `dct:creator` | 필수 | 데이터를 생성한 기관 또는 조직 |
| 게시자 | `dct:publisher` | 필수 | 데이터를 공개한 기관 또는 조직 |
| 관리 담당자 | `dcat:contactPoint` | 필수 | 연락처 정보 (`vcard:Contact`) |
| 생성 방법 | `aird:creationMethod` | 필수 | 수집/가공/합성(synthetic) 구분 |
| 갱신 주기 | `dct:accrualPeriodicity` | 필수 | EU frequency vocabulary 준용 |

### 3.3 접근·배포 메타데이터

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 접근 URL | `dcat:accessURL` | 필수 | 데이터셋 접근 페이지 |
| 다운로드 URL | `dcat:downloadURL` | 필수 | 직접 다운로드 링크 |
| 매체 유형 | `dcat:mediaType` | 필수 | IANA MIME type (`text/csv` 등) |
| 배포 포맷 | `dct:format` | 필수 | CSV, JSON, Parquet, GeoJSON 등 |
| 인코딩 | `aird:encoding` | 필수 | 문자 인코딩 (UTF-8 등) |
| 파일 크기 | `dcat:byteSize` | 권장 | 바이트 단위 |
| API 엔드포인트 | `dcat:endpointURL` | 권장 | RESTful API 주소 |
| 압축 포맷 | `dcat:compressFormat` | 선택 | `application/zip` 등 |

### 3.4 권리·이용 메타데이터

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 라이선스 | `dct:license` | 필수 | 라이선스 URI. 공공기관은 공공누리·CC 계열, 민간은 해당 라이선스 URI 사용 |
| 권한 | `dct:rights` | 필수 | 이용 범위 고지문 |
| 접근 제한 | `aird:accessRestriction` | 필수 | 공개/부분공개/비공개 구분 |
| 비식별화 처리 여부 | `aird:deidentification` | 필수 | 처리 여부 (`true` / `false`). 처리 방법 상세는 Layer 2 `aird:deidentMethod` 참조 |
| 이용 정책 | `odrl:hasPolicy` | 권장 | ODRL 기계 판독 가능 정책 |

---

## 4. Layer 2: Understanding Metadata

Layer 2는 데이터셋의 품질 수준, 변경 이력, 생성 과정을 파악하여 AI 활용 적합성을 판단하기 위한 메타데이터이다. Quality-Ready Data Preparation Framework(AIRD-STD-001)의 품질 진단 결과와 AI-Ready Data Transformation & Governance Specification(AIRD-STD-003)의 변환 이력이 이 계층에 기록된다.

### 4.1 버전·이력 메타데이터

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 버전 번호 | `dcat:version` | 필수 | 시맨틱 버전닝 (MAJOR.MINOR.PATCH) |
| 최초 등록일 | `dct:issued` | 필수 | ISO 8601 일시 |
| 최종 수정일 | `dct:modified` | 필수 | ISO 8601 일시 |
| 버전 노트 | `adms:versionNotes` | 필수 | 변경 사항 기술 |
| 이전 버전 | `dcat:previousVersion` | 권장 | 이전 버전 데이터셋 URI |
| 데이터셋 시리즈 | `dcat:inSeries` | 권장 | 소속 데이터셋 시리즈 URI |

### 4.2 품질 메타데이터 (AIRD-STD-001 연계)

AIRD-STD-001의 품질 진단 결과를 기록하는 메타데이터. W3C DQV(Data Quality Vocabulary)를 적용한다.

#### 4.2.1 품질 지수 (Quality Index)

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 품질 지수(QI) | `aird:qualityIndex` | 필수 | 6개 품질 차원 점수의 가중 합산 (0.0–1.0). 산정 방법은 AIRD-STD-001 6장 참조 |
| 품질 등급(Q-Tier) | `aird:qualityTier` | 필수 | 품질 등급. 판정 기준은 AIRD-STD-001 7장 참조 |
| 진단 성숙도(DM) | `aird:diagnosticMaturity` | 필수 | DM-1 / DM-2 / DM-3. 정의는 AIRD-STD-001 4.4절 참조 |
| 품질 진단 일시 | `dqv:computedOn` | 필수 | 진단 수행 일시 (ISO 8601) |
| 품질 진단 도구 | `aird:qualityTool` | 권장 | 진단에 사용된 도구 및 버전 |

#### 4.2.2 6개 품질 차원 점수

각 차원의 점수는 0.0–1.0으로 정규화된다. **Quality-Ready 전이 조건의 규범적 정의는 7.2절을 참조한다.** 측정 방법은 AIRD-STD-001 5장에서 정의하며, 본 표준은 기록 스키마만 정의한다.

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 완전성 점수 | `dqv:value` (dimension=`aird:completeness`) | 필수 | 결측 비율 기반 완전성 지표 |
| 일관성 점수 | `dqv:value` (dimension=`aird:consistency`) | 필수 | 포맷·도메인 규칙 준수 지표 |
| 정확성 점수 | `dqv:value` (dimension=`aird:accuracy`) | 필수 | 참값 대비 정확도 지표 |
| 적시성 점수 | `dqv:value` (dimension=`aird:timeliness`) | 필수 | 데이터 최신성 지표 |
| 유효성 점수 | `dqv:value` (dimension=`aird:validity`) | 필수 | 스키마·제약조건 준수 지표 |
| 유일성 점수 | `dqv:value` (dimension=`aird:uniqueness`) | 필수 | 중복 레코드 비율 기반 지표 |
| 컬럼별 세부 진단 결과 | `aird:columnQualityBreakdown` | 선택(MAY) | 차원별 점수의 컬럼 단위 세부 결과. 아래 구조 참조 |

> **진단 계층 설계 원칙**
>
> 품질 진단은 Dataset → Column → Value → Concept 순으로 계층화될 수 있다. 현재 본 표준은 Dataset-level 점수를 필수로 요구하며, 하위 계층은 단계적으로 수용한다.
>
> | 계층 | 진단 대상 | 본 표준 위치 |
> |---|---|---|
> | Dataset-level | 데이터셋 전체 품질 지수(QI) | 4.2.1~4.2.2절 (필수) |
> | Column-level | 컬럼 단위 품질 세부 분포 | `aird:columnQualityBreakdown` (MAY) |
> | Value-level | 위장 결측·분포 이상·단위 혼재 탐지 | AIRD-STD-003 소관 |
> | Concept-level | 컬럼-표준개념 매핑 | `csvw:tableSchema` `propertyUrl` (4.2.3절) |

**`aird:columnQualityBreakdown` 구조 (JSON-LD, MAY):**

```json
{
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "aird:completeness",
      "dqv:value": 0.96,
      "dqv:computedOn": "2026-04-07T10:00:00Z",
      "aird:columnQualityBreakdown": [
        { "csvw:column": "종업원수",   "aird:columnScore": 0.96, "aird:nullRate": 0.04 },
        { "csvw:column": "사업자번호", "aird:columnScore": 1.00, "aird:nullRate": 0.00 },
        { "csvw:column": "업종코드",   "aird:columnScore": 0.88, "aird:nullRate": 0.12 }
      ]
    }
  ]
}
```

#### 4.2.3 구조·의미 준비도 메타데이터

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 피처 완전성 지수 | `aird:featureCompletenessIndex` | 필수 | 피처별 결측 분포 요약 (0.0–1.0) |
| 스키마 적합률 | `aird:schemaConformanceRate` | 필수 | 정의된 스키마 대비 적합 비율. `csvw:tableSchema`가 정의된 경우 이를 기준으로 측정 |
| 컬럼 스키마 | `csvw:tableSchema` | 권장* | CSV 등 테이블형 데이터의 컬럼별 이름·데이터 타입·제약조건·설명 기술 (*정형 데이터 한정, W3C CSVW 기반) |
| 레이블 적합률 | `aird:labelConformanceRate` | 필수* | 레이블 정합성 비율 (*지도학습 데이터 한정) |
| 클래스 균형도 | `aird:classBalanceIndex` | 권장 | 클래스 분포의 균형도 지표 (0.0–1.0) |

> **`csvw:tableSchema`와 Layer 3 `cr:Field`의 역할 분리**
>
> - `csvw:tableSchema` (Layer 2): 데이터 이해를 위한 범용 컬럼 스키마. 사람과 시스템 모두를 대상으로 하며, AI 목적 변환 여부와 무관하게 Quality-Ready 단계에서 기술한다.
> - `cr:RecordSet` / `cr:Field` (Layer 3): ML 프레임워크가 데이터를 직접 로딩·실행하기 위한 기계 실행 명세. Purpose-Ready 상태에서만 요구된다.
>
> 두 속성은 동일한 컬럼 정보를 다른 목적으로 기술하며, 중복이 아닌 계층별 역할 분리이다.

**CSVW tableSchema 예시 (JSON-LD):**

```json
{
  "@context": "http://www.w3.org/ns/csvw",
  "url": "population.csv",
  "tableSchema": {
    "columns": [
      { "name": "year",       "datatype": "integer", "dc:description": "통계 기준 연도", "required": true },
      { "name": "district",   "datatype": "string",  "dc:description": "서울시 자치구명", "required": true },
      { "name": "population", "datatype": "integer", "dc:description": "주민등록 인구 수", "required": true, "minimum": 0 }
    ],
    "primaryKey": ["year", "district"]
  }
}
```

#### 4.2.4 신뢰·윤리 메타데이터

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 알려진 편향성 | `rai:dataBiases` | 필수 | 확인된 편향 유형 및 설명 |
| 데이터 한계 | `rai:knownLimitations` | 필수 | 구조적·내용적 제한사항 |
| 결측치 정보 | `rai:dataCollectionMissingData` | 필수 | 결측 비율 및 처리 방식 |
| 품질 검증 정보 | `dqv:hasQualityAnnotation` | 권장 | 검증 주체 및 방법 |
| 합성 데이터 여부 | `aird:isSynthetic` | 필수 | `true` / `false` |

### 4.3 프로브넌스 메타데이터

W3C PROV-O(Provenance Ontology)를 적용하여 데이터 생성·변환 과정을 기록한다. AIRD-STD-003 실행 시 자동 생성되는 메타데이터이다.

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 원천 데이터 소스 | `prov:wasDerivedFrom` | 필수 | 원본 데이터셋 URI |
| 수집 방법 | `aird:collectionMethod` | 필수 | 센서/조사/크롤링/API 등 |
| 전처리 이력 | `prov:wasGeneratedBy` | 권장 | **Activity 타입: `aird:PreprocessingActivity`.** 적용한 정제 규칙 및 도구 참조 |
| 변환 이력 | `prov:wasGeneratedBy` | 권장 | **Activity 타입: `aird:TransformationActivity`.** AIRD-STD-003 파이프라인 실행 로그 참조 |
| 비식별화 방법 | `aird:deidentMethod` | 필수* | 집계/부분삭제/마스킹 등 (*개인정보 포함 시). Layer 1의 `aird:deidentification`(boolean)과 역할 분리 |

> **`prov:wasGeneratedBy` Activity 타입 구분 규칙**
>
> 동일 속성(`prov:wasGeneratedBy`)을 전처리와 변환 이력에 모두 사용하며, Activity 인스턴스의 `@type`으로 구분한다.
>
> - 전처리: `@type` → `aird:PreprocessingActivity` (예: `aird:activity/preprocessing-20260101-001`)
> - 변환: `@type` → `aird:TransformationActivity` (예: `aird:activity/transform-ml-20260101-001`)
>
> 각 Activity는 `prov:startedAtTime`, `prov:endedAtTime`, `prov:wasAssociatedWith`(도구/담당자)를 함께 기록한다. **AIRD-STD-003 부속서 B의 JSON-LD 예시(Stage 1~3 Provenance)를 규범적(normative) 참조로 사용한다.**

### 4.4 Purpose-Readiness Vector

각 Purpose-Type에 대한 준비도를 독립적으로 표현한다.

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 목적 준비도 벡터 | `aird:purposeReadinessVector` | 선택 (Purpose-Ready 시 필수) | Purpose-Type별 독립적 Tier |

```yaml
purposeReadinessVector:
  ML:          Bronze | Silver | Gold | N/A
  DL:          Bronze | Silver | Gold | N/A
  KG:          Bronze | Silver | Gold | N/A
  RAG:         Bronze | Silver | Gold | N/A
  Stats:       Bronze | Silver | Gold | N/A
  FineTuning:  Bronze | Silver | Gold | N/A
  Multimodal:  Bronze | Silver | Gold | N/A   # Extension 등록 후 활성화
  Streaming:   Bronze | Silver | Gold | N/A   # Extension 등록 후 활성화
  Evaluation:  Bronze | Silver | Gold | N/A   # Extension 등록 후 활성화
```

**Q-Tier와 Purpose-Tier의 관계:** Q-Tier는 데이터 자체의 품질 등급이며, Purpose-Tier는 특정 목적에 대한 적합도 등급이다. Q-Tier는 Purpose-Tier의 선행 조건이지만, Gold가 자동으로 모든 Purpose-Tier Gold를 의미하지는 않는다.

---

## 5. Layer 3: Operability Metadata

AI 도구가 데이터를 파싱·로딩·실행할 수 있게 하는 메타데이터. Purpose-Ready 데이터의 유형에 따라 적합한 메타데이터 규격이 다르므로, Purpose-Type별 멀티 프로파일로 설계한다.

### 5.1 설계 원칙

Layer 3는 단일 표준을 강제하지 않는다. 각 Purpose-Type에 적합한 기존 표준을 채택하고, 필요 시 확장을 추가한다.

**공통 요구사항:**
- 모든 Operability Metadata는 기계 판독 가능한 정형 포맷(JSON-LD 또는 RDF/XML)으로 제공
- Layer 1의 DCAT 카탈로그에서 `dcat:distribution`으로 참조 가능
- 데이터 로딩에 필요한 최소 정보(파일 위치, 포맷, 스키마) 포함
- Purpose-Type 식별자(`aird:purposeType`)를 반드시 명시

**모델-데이터 결합도 원칙:**

> AIRD Pack은 AI 모델 파일을 포함하지 않는다. 모델은 Purpose-Ready Data를 생성하기 위한 **변환 수단**으로 간주하며, 그 자체는 Pack의 구성 요소가 아니다. 단, 모델에 의해 생성된 파생 데이터(예: 임베딩 벡터, 인덱스)는 Pack에 포함될 수 있으며, 이 경우 해당 데이터는 특정 모델에 논리적으로 종속된다.

**모델-데이터 결합도(Model-Data Coupling) 분류:**

| Coupling | 정의 | 해당 Purpose-Type | packCompleteness |
|---|---|---|---|
| `loose` | 데이터가 모델 독립적. 소비자가 임의 모델 선택 | ML, DL, KG, Stats | `data-only` |
| `derived` | 모델 산출물이 Pack에 포함. 특정 모델에 논리적 종속 | RAG, FineTuning | `derived-without-model` 또는 `derived-with-model` |
| `tight` | 모델 없이 Pack 실행 불가 (미래 확장용) | Agent Pack (예정) | `full-reproducible` |

**Layer 3 공통 필수 속성 (모든 Purpose-Type 적용):**

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| Pack 생성 시점 | `aird:packGeneratedAt` | 필수 | ISO 8601. Stale 판단 기준 |
| 기반 데이터 버전 | `aird:sourceDataVersion` | 필수 | SemVer. Pack 생성에 사용된 Quality-Ready 데이터 버전 |
| 모델-데이터 결합도 | `aird:modelDataCoupling` | 필수 | `loose` \| `derived` \| `tight` |
| Pack 완전성 | `aird:packCompleteness` | 필수 | `data-only` \| `derived-without-model` \| `derived-with-model` \| `full-reproducible` |
| 에이전트 접근 가능 | `aird:agentAccessible` | 권장 | `true` \| `false`. AIRD-STD-005 탐색 API 필터 조건 |
| 변환 참조 프로파일 | `aird:transformationProfile` | 권장 | 도메인 기술규격 URI. 변환 방법론·성능 기준 위임처 |
| 복수 Pack 관계 | `aird:multiPurposeLinks` | 권장 | 연관 Pack URI 목록 |

### 5.2 Purpose-Type별 프로파일 개요

| Purpose-Type | 기반 표준 | 적용 대상 | 로딩 대상 도구 |
|---|---|---|---|
| ML/DL Pack | Croissant 1.0 | 지도학습, 비지도학습, 딥러닝, QA 데이터셋 | TensorFlow, PyTorch, JAX, HuggingFace |
| RAG Pack | Croissant 기반 + AIRD-RAG 확장 (Candidate) | 검색증강생성용 문서 코퍼스 | LangChain, LlamaIndex, Chroma, FAISS |
| KG Pack | VoID + DCAT | 지식그래프, RDF/트리플 데이터 | Neo4j, GraphDB, SPARQL 엔드포인트 |
| Stats Pack | SDMX 또는 Croissant 선택 | 통계 분석용 집계 데이터 | R, pandas, 통계 분석 도구 |
| Fine-tuning Pack | AIRD-FT 확장 (Draft) | LLM 파인튜닝용 instruction 데이터 | HuggingFace Trainer, DeepSpeed, Axolotl |

### 5.3 ML/DL Profile (Croissant 1.0 기반)

Croissant의 4계층 구조(Metadata, Resource, Structure, Semantic)를 그대로 적용한다.

#### 5.3.1 Resource Layer

| 항목명 | 클래스/속성 | 구분 | 설명 |
|---|---|---|---|
| 파일 객체 | `cr:FileObject` | 필수 | 개별 파일 (CSV, Parquet, 이미지 등) |
| 파일 집합 | `cr:FileSet` | 선택 | 파일 집합 (이미지 폴더, 분할 CSV) |
| 콘텐츠 URL | `sc:contentUrl` | 필수 | 데이터 파일 위치 |
| 인코딩 포맷 | `sc:encodingFormat` | 필수 | MIME type (`text/csv` 등) |
| 체크섬 | `sc:sha256` | 권장 | 무결성 검증용 해시 |
| 포함 관계 | `cr:containedIn` | 선택 | ZIP 내부 파일 참조 |

#### 5.3.2 Structure Layer

| 항목명 | 클래스/속성 | 구분 | 설명 |
|---|---|---|---|
| 레코드셋 | `cr:RecordSet` | 필수 | 데이터의 논리적 테이블 구조 |
| 필드 | `cr:Field` | 필수 | 컬럼 정의 (이름, 타입, 설명) |
| 데이터 타입 | `cr:dataType` | 필수 | `sc:Integer`, `sc:Text`, `sc:ImageObject` 등 |
| 추출 방법 | `cr:source/extract` | 필수 | 파일에서 필드 추출 방법 (column, jsonPath 등) |
| 참조 관계 | `cr:references` | 선택 | 다른 RecordSet의 Field 참조 (외래키) |

> **Layer 2 `csvw:tableSchema`와의 관계:** `cr:Field`는 ML 프레임워크가 데이터를 직접 로딩·실행하기 위한 기계 실행 명세이다. 범용 컬럼 스키마 기술은 Layer 2의 `csvw:tableSchema`(4.2.3절)에서 담당한다. Layer 2의 `csvw:tableSchema`가 존재하는 경우 `cr:Field`의 이름·타입 정보는 이와 일치해야 한다(SHOULD).

#### 5.3.3 Semantic Layer

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 분할 정의 | `aird:split` | 필수 | train/validation/test 분할 규칙 |
| 라벨 필드 | `aird:labelField` | 필수* | 목표 변수 지정 (*지도학습 시) |
| 피처 필드 | `aird:featureFields` | 권장 | 입력 변수 목록 |
| 클래스 매핑 | `aird:classMapping` | 권장 | 라벨 값 → 의미 매핑 테이블 |
| 어노테이션 포맷 | `aird:annotationFormat` | 권장 | COCO, VOC, YOLO, NER-BIO 등 |
| 타스크 유형 | `aird:taskType` | 필수 | 아래 허용값 참조 |

**`aird:taskType` 허용값:**

```yaml
# ML 계열
- classification
- regression
- clustering
- anomaly-detection
- time-series-forecasting
- ranking
# DL 계열
- image-classification
- object-detection
- image-segmentation
- semantic-segmentation
- text-classification
- named-entity-recognition
- speech-recognition
- text-generation
- question-answering
```

#### 5.3.4 Croissant RAI 확장

| 항목명 | 속성 | 설명 |
|---|---|---|
| 의도된 사용 목적 | `rai:intendedUse` | 권장되는 AI 활용 시나리오 |
| 금지된 사용 | `rai:prohibitedUse` | 금지되는 활용 시나리오 |
| 인구통계 분포 | `rai:demographicDistribution` | 편향 감사용 인구통계 정보 |
| 데이터 수집 윤리 | `rai:dataCollectionProcess` | 수집 과정의 윤리적 검토 사항 |

### 5.4 RAG Profile (Croissant 기반 + AIRD-RAG 확장)

> **네임스페이스 상태: Candidate 어휘**
>
> `aird-rag:` 확장 속성은 Candidate 어휘로 채택한다. Candidate 어휘는 표준 내에서 공식 사용 가능하되, 향후 변경 가능성을 선언한 상태이다.
> - **임시 네임스페이스 URI:** `http://datahub.kr/ns/aird-rag#`
> - Croissant 커뮤니티(MLCommons)에 한국어 데이터 확장 제안을 병행 진행한다.

RAG Pack은 임베딩 모델을 포함하지 않지만, 해당 모델에 의해 생성된 파생 데이터(벡터, 인덱스)에 논리적으로 종속된다. 임베딩 모델의 명칭·버전·레지스트리 URI·커밋 해시는 재현성 보장을 위해 필수적으로 제공되어야 한다(SHALL). `aird:modelDataCoupling`은 `derived`, `aird:packCompleteness`는 `derived-without-model`로 선언한다.

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 청킹 전략 | `aird-rag:chunkStrategy` | 필수 | fixed-size, sentence, semantic, recursive 등 |
| 청크 크기 | `aird-rag:chunkSize` | 필수 | 토큰 또는 문자 수 단위 |
| 청크 오버랩 | `aird-rag:chunkOverlap` | 필수 | 인접 청크 간 중복 크기 |
| 임베딩 모델 명칭·버전 | `aird-rag:embeddingModel` | 필수 | 벡터 생성에 사용된 모델 명칭 및 버전 |
| 임베딩 차원 | `aird-rag:embeddingDimension` | 필수 | 벡터 차원 수 (768, 1536 등) |
| 임베딩 모델 레지스트리 | `aird-rag:embeddingModelRegistry` | 필수 | HuggingFace Hub 등 레지스트리 URI |
| 임베딩 모델 커밋 해시 | `aird-rag:embeddingModelCommit` | 필수 | 버전 고정용 커밋 해시 또는 태그 |
| 임베딩 모델 라이선스 | `aird-rag:embeddingModelLicense` | 필수 | SPDX 라이선스 식별자 |
| 모델 카드 URI | `aird-rag:modelCardURI` | 권장 | HuggingFace Model Card 등 URI |
| 인덱스 유형 | `aird-rag:indexType` | 권장 | FAISS, Chroma, Pinecone, Milvus 등 |
| 인덱스 설정 | `aird-rag:indexConfig` | 권장 | 거리 메트릭, 인덱스 파라미터 |
| 원본 문서 포맷 | `aird-rag:sourceFormat` | 필수 | PDF, HWP, HTML, Markdown 등 |
| 청크 총 수 | `aird-rag:totalChunks` | 권장 | 전체 청크 개수 |
| 메타데이터 필드 | `aird-rag:metadataFields` | 권장 | 청크별 부가 메타데이터 (출처, 페이지 등) |

### 5.5 KG Profile (VoID + DCAT 기반)

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 트리플 수 | `void:triples` | 필수 | 전체 트리플 개수 |
| 엔티티 수 | `void:entities` | 필수 | 고유 엔티티 수 |
| 클래스 수 | `void:classes` | 필수 | 온톨로지 클래스 수 |
| 속성 수 | `void:properties` | 필수 | 사용된 속성(predicate) 수 |
| 온톨로지 참조 | `void:vocabulary` | 필수 | 사용된 온톨로지 URI |
| 직렬화 포맷 | `void:feature` | 필수 | N-Triples, Turtle, RDF/XML, JSON-LD 등 |
| SPARQL 엔드포인트 | `void:sparqlEndpoint` | 권장 | SPARQL 쿼리 엔드포인트 URL |
| 링크셋 | `void:linkset` | 권장 | 외부 KG와의 링크 정보 |
| 추론 규칙 | `aird-kg:inferenceRules` | 선택 | 적용된 추론 규칙 (RDFS, OWL 등) |
| 서브그래프 통계 | `void:classPartition` | 권장 | 클래스별 트리플 분포 통계 |

> **한국어 레이블 제약 조건:** 모든 핵심 클래스·개체는 최소 1개의 `@ko` 태그 레이블을 가져야 한다(SHOULD). `rdfs:label` 또는 `skos:prefLabel`을 사용하며, SHACL shape으로 `@ko` 레이블 존재 여부를 검증한다.

### 5.6 Stats Profile (SDMX 또는 Croissant 선택)

통계 분석용 집계 데이터는 데이터 구조 특성에 따라 Croissant 또는 SDMX를 선택적으로 적용한다.

**선택 판단 기준표:**

| 데이터 특성 | 권장 표준 | 판단 근거 |
|---|---|---|
| 단순 테이블 구조 (컬럼 수 ≤ 20, 행 기반) | Croissant | RecordSet/Field 구조로 표현 가능 |
| 연도별 1차원 집계 (시계열 단독) | Croissant | 단일 차원 시계열 처리 가능 |
| 차원 2개 이상 교차 집계 (시간 × 지역 등) | SDMX | 다차원 큐브 구조 필수 |
| 지역 × 업종 × 시간 3차원 이상 조합 | SDMX | DSD(Data Structure Definition) 활용 |
| 혼용: 집계 테이블 + 메타데이터 큐브 | Croissant 기본 + `aird:sdmxDSD` 참조 | 외부 SDMX DSD를 속성으로 연결 |

**메타데이터 필드:**

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 차원 정의 | `sdmx:dimension` | 필수 | 분석 차원 (시간, 지역, 업종 등) |
| 측정값 정의 | `sdmx:measure` | 필수 | 측정 대상 지표 |
| 코드리스트 | `sdmx:codelist` | 필수 | 사용된 코드 체계 참조 |
| 집계 규칙 | `aird-stats:aggregationRule` | 필수 | SUM, AVG, COUNT 등 적용 함수 |
| 기준 시점 | `sdmx:timePeriod` | 필수 | 통계 기준 시점 |
| 단위 | `sdmx:unitMeasure` | 필수 | 측정 단위 (KRW, 명, % 등) |
| 피봇 구조 | `aird-stats:pivotStructure` | 선택 | 행/열 차원 및 값 배치 |
| SDMX DSD 참조 | `aird:sdmxDSD` | 선택 | Croissant 기본 사용 시 SDMX DSD URI 연결 |

### 5.7 Fine-tuning Profile (AIRD-FT, Draft)

> **상태:** Draft. AIRD-STD-003 Extension Profile 등록 절차를 통해 공식화 예정.
>
> **네임스페이스:** `aird-ft:` (`http://data.go.kr/ns/aird-ft#`, Draft)
>
> **모델-데이터 결합도:** `derived`. `aird:packCompleteness`는 `data-only`가 원칙.

LLM을 특정 도메인에 파인튜닝하기 위한 데이터 패키지.

**핵심 산출물:**
- `instruction_response_pairs.jsonl` — 지시문-응답 페어
- `preference_data.jsonl` — 선호도 데이터 (RLHF/DPO)
- `conversation_history.jsonl` — 대화 이력
- `system_prompt_templates.json` — 시스템 프롬프트 템플릿

**메타데이터 속성:**

| 항목명 | 속성 | 구분 | 설명 |
|---|---|---|---|
| 데이터 포맷 유형 | `aird-ft:dataFormat` | 필수 | `instruction-response` \| `preference` \| `conversation` |
| 지시문 템플릿 URI | `aird-ft:instructionTemplate` | 필수 | 사용된 프롬프트 템플릿 URI 또는 내용 |
| 파인튜닝 대상 모델 계열 | `aird-ft:targetModelFamily` | 선택 | llama, mistral, qwen, exaone 등 |
| 학습 페어 수 | `aird-ft:pairCount` | 필수 | 전체 instruction-response 페어 수 |
| 언어 스타일 | `aird-ft:languageStyle` | 권장 | `formal` \| `informal` \| `domain-specific` |
| 도메인 | `aird-ft:taskDomain` | 권장 | 법령, 행정, 의료, 금융 등 도메인 구분 |
| 훈련/검증 분할 | `aird:split` | 필수 | train/validation 비율 (기본 권장: 95/5) |

---

## 6. 계층 간 연결 메커니즘

### 6.1 Layer 1 ↔ Layer 3 연결

Layer 3의 Operability Metadata 파일(`metadata.json` 등)을 Layer 1의 DCAT 카탈로그에서 `dcat:distribution`으로 참조한다.

```json
{
  "ex:dataset1": {
    "type": "dcat:Dataset",
    "dcat:distribution": ["ex:csv-dist", "ex:croissant-dist"]
  },
  "ex:croissant-dist": {
    "type": "dcat:Distribution",
    "dcat:mediaType": "application/ld+json",
    "dcat:downloadURL": "https://example.org/ds001/metadata.json",
    "dct:format": "Croissant"
  }
}
```

### 6.2 Layer 1 ↔ Layer 2 연결

Layer 2의 품질·프로브넌스 메타데이터 중 요약 정보(품질 등급, 최종 검증 일시)는 Layer 1에 포함된다. 상세 정보는 Layer 2 전용 문서로 분리하고, Layer 1에서 `foaf:page`로 참조한다.

```json
{
  "ex:dataset1": {
    "type": "dcat:Dataset",
    "aird:qualityTier": "Silver",
    "aird:qualityIndex": 0.82,
    "foaf:page": "https://example.org/ds001/quality-report.html"
  }
}
```

### 6.3 Layer 2 ↔ Layer 3 연결

Layer 2의 `rai:dataBiases`, `rai:knownLimitations`는 Layer 3의 Croissant RAI 확장과 동일한 네임스페이스를 사용한다. Layer 2에서 기관 관점으로 기술한 품질 정보가, Layer 3에서는 AI 개발자 관점에서 재구성된다.

### 6.4 Base Set의 메타데이터 처리

Base Set(슈퍼스타 데이터셋)은 DCAT v3의 `dcat:DatasetSeries`와 `dcat:inSeries` 속성으로 Base Set 내의 데이터셋 간 관계를 기술한다.

```json
{
  "ex:baseSet1": {
    "type": "dcat:DatasetSeries",
    "dct:title": "도시 종합 인구 분석 Base Set"
  },
  "ex:population2024": {
    "type": "dcat:Dataset",
    "dcat:inSeries": "ex:baseSet1",
    "prov:wasDerivedFrom": "ex:rawPopulation2024"
  }
}
```

---

## 7. 제어 어휘 및 검증

### 7.1 제어 어휘(Controlled Vocabulary)

| 제어 어휘 | 적용 속성 | 값 목록 | 참조 |
|---|---|---|---|
| 데이터셋 유형 | `dct:type` | Structured, Image, Audio, Video, Text, Geospatial, FT | AIRD 자체 정의 |
| Purpose-Type | `aird:purposeType` | ML, DL, RAG, KG, Stats, FineTuning, Multimodal, Streaming, Evaluation | AIRD 자체 정의 |
| 갱신 주기 | `dct:accrualPeriodicity` | annual, quarterly, monthly, daily, irregular | EU frequency vocabulary |
| 라이선스 유형 | `dct:license` | CC-BY, CC-BY-SA, CC-BY-NC 등 국제 표준 라이선스 URI | SPDX + 기관별 |
| 품질 등급 | `aird:qualityTier` | Bronze, Silver, Gold, Platinum | AIRD-STD-001 7장 |
| 접근 제한 | `aird:accessRestriction` | public, restricted, non-public | AIRD 자체 정의 |
| 생성 방법 | `aird:creationMethod` | collected, processed, synthetic, augmented | AIRD 자체 정의 |
| 메타데이터 상태 | `aird:metadataStatus` | Raw, Quality-Ready, Purpose-Ready, Stale | 본 표준 2장 |
| 모델-데이터 결합도 | `aird:modelDataCoupling` | loose, derived, tight | 본 표준 5.1절 |
| Pack 완전성 | `aird:packCompleteness` | data-only, derived-without-model, derived-with-model, full-reproducible | 본 표준 5.1절 |

### 7.2 유효성 검증 규칙

#### Quality-Ready 전이 조건 (규범적)

> **본 조항은 Quality-Ready 전이 조건의 단일 출처(single source of truth)이다.** 2.1절 및 4.2.2절은 본 조항을 참조하며, 내용이 충돌할 경우 본 조항이 우선한다.

데이터셋이 Quality-Ready 상태로 전이하기 위해서는 다음 세 조건을 모두 충족해야 한다. 수치는 AIRD-STD-001 7장의 Q-Tier 판정 기준을 따른다.

1. **QI ≥ 0.50** — 6개 품질 차원 점수의 가중 합산이 0.50 이상 (Tier 1 Bronze 이상)
2. **Mandatory Gate 조건 충족** — 6개 차원 각각이 AIRD-STD-001 부속서 B의 Tier 1 임계치를 통과
3. **D3(정확성) ≥ 0.65** — 단, D3 전체 미측정(Case B) 시 자동 면제

#### 계층별 기계 검증 방법

| 계층 | 검증 방법 | 적용 범위 |
|---|---|---|
| Layer 1 | SHACL shapes — DCAT 프로파일 준수 검증 | 필수 (Core Profile) |
| Layer 2 | JSON Schema — 품질 리포트 구조 검증 | 필수 |
| Layer 3 ML/DL | `mlcroissant` Python 라이브러리 — Croissant 파일 검증 | 필수 |
| Layer 3 KG | SHACL shapes — VoID 메타데이터 검증 및 핵심 클래스 `@ko` 레이블 존재 여부 검증 | 필수 (Core) / 권장 (확장 Profile) |
| Layer 3 RAG | JSON Schema — AIRD-RAG 확장 검증 (Candidate 상태) | 권장 |
| Layer 3 Stats | JSON Schema (Croissant 선택 시) 또는 SDMX Validation | 필수 |

---

## 8. 적합성 프레임워크

### 8.1 적합성 수준

| 적합성 수준 | 요구사항 | metadata.status | AIRD-STD-001 연계 |
|---|---|---|---|
| Basic Conformance | Layer 1 필수 항목 모두 충족 | `"Raw"` | AIRD-STD-001 Level A |
| Quality Conformance | Basic + Layer 2 필수 항목 모두 충족, 7.2절 전이 조건 충족, Q-Tier 부여 | `"Quality-Ready"` | AIRD-STD-001 Level B |
| Purpose Conformance | Quality + Layer 3 해당 Purpose-Type 필수 항목 모두 충족 | `"Purpose-Ready"` | 본 표준 추가 정의 |

### 8.2 적합성 선언 형식

> **형식 안내:** 아래 예제는 가독성을 위한 YAML 표현이다. 규범적(normative) 형식은 JSON-LD이며, 부록 B.2절의 JSON-LD 예제를 따른다. 두 표현이 충돌하는 경우 JSON-LD가 우선한다.

```yaml
Conformance:
  Standard: AIRD-STD-002
  Version: v0.1
  Status: Purpose-Ready
  QI: 0.82
  Q-Tier: Silver
  DiagnosticMaturity: DM-2
  PurposeReadiness:
    ML: Silver
    DL: N/A
    RAG: Bronze
    KG: N/A
    Stats: N/A
    FineTuning: N/A
  PackInfo:
    packGeneratedAt: "2026-04-14T09:00:00+09:00"
    sourceDataVersion: "1.2.0"
    modelDataCoupling: "derived"
    packCompleteness: "derived-without-model"
    agentAccessible: true
  EvaluationDate: 2026-04-14
  EvaluationTool: aird-validator v1.0
```

### 8.3 확장 프로파일 관리

Layer 3의 RAG Profile, KG Profile, Stats Profile은 AIRD-STD-003에서 정의한 Extension Profile 거버넌스 하에 관리된다. 모든 확장 프로파일은 다음을 제공해야 한다.

- **목적 정의:** 확장 프로파일이 해결하는 Purpose-Type 명시
- **정량적 요구사항:** 해당 Purpose-Type의 Tier 판정 기준
- **산출 방법:** Tier 결정을 위한 점수 계산 방법
- **Tier 기준:** Bronze/Silver/Gold 문턱값
- **검증 방법:** 적합성 검증 도구 및 절차

---

## 9. 필드 매핑 테이블

Quality-Ready Data Preparation Framework(AIRD-STD-001)에서 사용하는 커스텀 필드명과 본 표준의 국제 표준 어휘 속성 간 정규적(normative) 매핑을 제공한다.

| AIRD-STD-001 필드명 | 본 표준 속성 | 국제 표준 | 비고 |
|---|---|---|---|
| `datasetIdentifier` | `dct:identifier` | Dublin Core | 영구 식별자 |
| `title` | `dct:title` | Dublin Core | |
| `description` | `dct:description` | Dublin Core | |
| `publisher` | `dct:publisher` | Dublin Core | |
| `accessURL` | `dcat:accessURL` | W3C DCAT | |
| `license` | `dct:license` | Dublin Core | |
| `dataFormat` | `dct:format` | Dublin Core | |
| `encoding` | `aird:encoding` | AIRD 확장 | |
| `version` | `dcat:version` | W3C DCAT | |
| `issued` | `dct:issued` | Dublin Core | |
| `modified` | `dct:modified` | Dublin Core | |
| `metadata.status` | `aird:metadataStatus` | AIRD 확장 | Raw / Quality-Ready / Purpose-Ready / Stale |
| `completenessScore` | `dqv:value` (dimension=`aird:completeness`) | W3C DQV | 0.0–1.0 정규화 |
| `consistencyScore` | `dqv:value` (dimension=`aird:consistency`) | W3C DQV | 0.0–1.0 정규화 |
| `accuracyScore` | `dqv:value` (dimension=`aird:accuracy`) | W3C DQV | 0.0–1.0 정규화 |
| `timelinessScore` | `dqv:value` (dimension=`aird:timeliness`) | W3C DQV | 0.0–1.0 정규화 |
| `validityScore` | `dqv:value` (dimension=`aird:validity`) | W3C DQV | 0.0–1.0 정규화 |
| `uniquenessScore` | `dqv:value` (dimension=`aird:uniqueness`) | W3C DQV | 0.0–1.0 정규화 |
| `evaluationDate` | `dqv:computedOn` | W3C DQV | ISO 8601 |
| `qualityIndex` | `aird:qualityIndex` | AIRD 확장 | QI (0.0–1.0) |
| `qualityTier` | `aird:qualityTier` | AIRD 확장 | Bronze / Silver / Gold / Platinum |
| `diagnosticMaturity` | `aird:diagnosticMaturity` | AIRD 확장 | DM-1 / DM-2 / DM-3 |
| `featureCompletenessIndex` | `aird:featureCompletenessIndex` | AIRD 확장 | |
| `schemaConformanceRate` | `aird:schemaConformanceRate` | AIRD 확장 | |
| `labelConformanceRate` | `aird:labelConformanceRate` | AIRD 확장 | |
| `purposeReadinessVector` | `aird:purposeReadinessVector` | AIRD 확장 | Purpose-Type별 독립 Tier |

---

## 10. 구현 로드맵

### 10.1 단계별 적용 전략

3계층 전체를 동시에 적용하는 것은 비현실적이므로, 단계적 적용을 권장한다.

| 단계 | 시기 | 적용 범위 | 핵심 산출물 |
|---|---|---|---|
| 1단계 — 기반 구축 | 2026년 | Layer 1 필수 항목, DCAT 코어 프로파일 | DCAT JSON-LD context, SHACL validation shapes, 공공기관용 구현 가이드 |
| 2단계 — 품질 연계 | 2027년 | Layer 2 품질·프로브넌스, Layer 3 ML/DL Profile | 품질 리포트 스키마, Croissant 확장 프로파일, AIRD-STD-001 연계 인터페이스 |
| 3단계 — 확장 적용 | 2028년 | Layer 3 RAG/KG/Stats/FineTuning, 전체 계층 통합, 민간 적용 확산 | AIRD-RAG 확장 규격, VoID 프로파일, AIRD-STD-003 연계 파이프라인 |

### 10.2 핵심 설계 결정 사항

표준 확정 전 결정이 필요한 사항:

- **PID 체계:** DOI 발급, 국가 자체 PID, 또는 범용 URI 패턴 중 선택
- **AIRD 확장 속성 네임스페이스:** `http://data.go.kr/ns/aird#` 또는 범용 URI 패턴
- **Layer 3 RAG 프로파일 네임스페이스:** `aird-rag:` Candidate 어휘 URI 확정
- **민간 적용 시 적합성 선언 방식:** 공공기관 외 적용 주체의 적합성 선언 절차 및 검증 기관 지정

---

## 11. 부록 A: 국내 공공데이터 구현 참고 (참고)

> **본 부록은 참고(Informative)이다.** 국내 공공데이터 관리체계와의 연계를 위한 구현 참고 사항을 제공하며, 본 표준의 규범적 요구사항에 포함되지 않는다.

### A.1 국내 정책 맥락

본 표준은 AI-Ready 데이터 관련 국내 정책 논의를 기술 표준 어휘로 형식화하는 과정에서 개발되었다. 공공기관 구현 시 관련 행정 지침 및 법령을 함께 참조하도록 권장한다.

### A.2 공공데이터 등록 항목 매핑

| 공공데이터 등록 항목 | Layer 1 속성 | 비고 |
|---|---|---|
| 공공데이터 명칭 | `dct:title` | 기존 항목 그대로 사용 |
| 공공데이터 설명 | `dct:description` | 기존 항목 그대로 사용 |
| 제3자 권리 포함 여부 | `dct:license` | 라이선스 URI로 확장 |
| 이용허락범위 | `dct:rights` | 기존 항목 그대로 사용 |
| 업데이트 주기 | `dct:accrualPeriodicity` | EU frequency 코드로 정규화 |
| 차기 등록 예정일 | `dct:modified` | ISO 8601로 정규화 |
| 위치(URL) | `dcat:accessURL` | 기존 항목 그대로 사용 |
| 매체유형 | `dcat:mediaType` | IANA MIME type으로 정규화 |
| 언어 | `dct:language` | ISO 639-1로 정규화 |
| (신규) 고유식별자 | `dct:identifier` | PID 체계 신규 부여 |
| (신규) 데이터셋 유형 | `dct:type` | AI-Ready 확장 속성 |
| (신규) 생성 방법 | `aird:creationMethod` | AI-Ready 확장 속성 |
| (신규) 인코딩 | `aird:encoding` | AI-Ready 확장 속성 |
| (신규) 메타데이터 상태 | `aird:metadataStatus` | AI-Ready 확장 속성 |

### A.3 주제 분류: BRM 연계

공공기관이 `dcat:theme`에 주제 분류를 기록할 때 정부기능분류체계(BRM)를 사용하도록 권장한다. 민간 적용 주체는 BRM 대신 적합한 도메인 분류 체계를 사용할 수 있다.

### A.4 라이선스: 공공누리 연계

| 유형 | URI |
|---|---|
| 공공누리 제1유형 | `https://www.kogl.or.kr/info/licenseType1.do` |
| 공공누리 제2유형 | `https://www.kogl.or.kr/info/licenseType2.do` |
| 공공누리 제3유형 | `https://www.kogl.or.kr/info/licenseType3.do` |
| 공공누리 제4유형 | `https://www.kogl.or.kr/info/licenseType4.do` |

---

## 12. 부록 B: JSON-LD 예제

### B.1 Quality-Ready 데이터셋 메타데이터 예제

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct":  "http://purl.org/dc/terms/",
    "dqv":  "http://www.w3.org/ns/dqv#",
    "prov": "http://www.w3.org/ns/prov#",
    "aird": "http://data.go.kr/ns/aird#",
    "rai":  "http://mlcommons.org/croissant/RAI/",
    "foaf": "http://xmlns.com/foaf/0.1/"
  },
  "@type": "dcat:Dataset",
  "dct:identifier": "https://example.org/pid/{dataset-id}",
  "dct:title": "서울시 연도별 인구 변화",
  "dct:title@en": "Seoul Annual Population Change",
  "dct:description": "서울시 구별 연도별 인구 통계",
  "dcat:keyword": ["인구", "서울", "연도별"],
  "dct:type": "aird:Structured",
  "dct:language": "ko",
  "dct:publisher": {
    "@type": "foaf:Organization",
    "foaf:name": "서울특별시"
  },
  "aird:metadataStatus": "Quality-Ready",
  "aird:qualityIndex": 0.82,
  "aird:qualityTier": "Silver",
  "aird:diagnosticMaturity": "DM-2",
  "aird:deidentification": false,
  "dqv:hasQualityMeasurement": [
    { "dqv:isMeasurementOf": "aird:completeness", "dqv:value": 0.95, "dqv:computedOn": "2026-04-14T10:30:00Z" },
    { "dqv:isMeasurementOf": "aird:consistency",  "dqv:value": 0.88 },
    { "dqv:isMeasurementOf": "aird:accuracy",     "dqv:value": 0.79 },
    { "dqv:isMeasurementOf": "aird:timeliness",   "dqv:value": 0.72 },
    { "dqv:isMeasurementOf": "aird:validity",     "dqv:value": 0.85 },
    { "dqv:isMeasurementOf": "aird:uniqueness",   "dqv:value": 0.73 }
  ],
  "aird:purposeReadinessVector": {
    "ML": "Silver",
    "Stats": "Gold",
    "RAG": "N/A",
    "KG": "N/A"
  }
}
```

### B.2 적합성 선언 예제 (JSON-LD — 규범적)

```json
{
  "@context": {
    "aird": "http://data.go.kr/ns/aird#"
  },
  "aird:conformance": {
    "aird:standard": "AIRD-STD-002",
    "aird:conformanceLevel": "Quality",
    "aird:metadataStatus": "Quality-Ready",
    "aird:qualityIndex": 0.82,
    "aird:qualityTier": "Silver",
    "aird:diagnosticMaturity": "DM-2",
    "aird:purposeReadinessVector": {
      "ML": "Silver",
      "Stats": "Gold",
      "RAG": "N/A",
      "KG": "N/A"
    },
    "aird:evaluationDate": "2026-04-14",
    "aird:evaluationTool": "aird-validator v1.0"
  }
}
```

### B.3 ML Pack Croissant 메타데이터 예제 (Layer 3)

```json
{
  "@context": {
    "cr":   "http://mlcommons.org/croissant/1.0/",
    "sc":   "https://schema.org/",
    "aird": "http://data.go.kr/ns/aird#",
    "rai":  "http://mlcommons.org/croissant/RAI/"
  },
  "@type": "cr:Dataset",
  "aird:purposeType": "ML",
  "aird:metadataStatus": "Purpose-Ready",
  "aird:packGeneratedAt": "2026-04-14T09:00:00+09:00",
  "aird:sourceDataVersion": "1.2.0",
  "aird:modelDataCoupling": "loose",
  "aird:packCompleteness": "data-only",
  "cr:license": "https://www.kogl.or.kr/info/licenseType1.do",
  "cr:resources": [
    { "@type": "cr:FileObject", "@id": "population-train", "sc:contentUrl": "https://example.org/ds001/ml/train.csv", "sc:encodingFormat": "text/csv", "sc:sha256": "a3f5c2d1..." },
    { "@type": "cr:FileObject", "@id": "population-valid", "sc:contentUrl": "https://example.org/ds001/ml/valid.csv", "sc:encodingFormat": "text/csv", "sc:sha256": "b7e9a4f2..." },
    { "@type": "cr:FileObject", "@id": "population-test",  "sc:contentUrl": "https://example.org/ds001/ml/test.csv",  "sc:encodingFormat": "text/csv", "sc:sha256": "c1d8b3e5..." }
  ],
  "cr:recordSets": [
    {
      "@type": "cr:RecordSet",
      "@id": "population-records",
      "cr:fields": [
        { "@id": "year",       "cr:dataType": "sc:Integer", "cr:description": "통계 기준 연도" },
        { "@id": "district",   "cr:dataType": "sc:Text",    "cr:description": "서울시 자치구명" },
        { "@id": "population", "cr:dataType": "sc:Integer", "cr:description": "주민등록 인구 수 (목표 변수)" }
      ]
    }
  ],
  "aird:split":         { "train": 0.70, "validation": 0.15, "test": 0.15 },
  "aird:labelField":    "population",
  "aird:featureFields": ["year", "district"],
  "aird:taskType":      "regression",
  "rai:intendedUse":    "서울시 구별 인구 변화 추세 예측 모델 학습",
  "rai:prohibitedUse":  "개인 식별 목적 사용 금지"
}
```

---

## 13. 부록 C: 표준 간 참조 매트릭스 (참고)

> **본 부록은 참고(Informative)이다.** 표준 시리즈 간의 절 단위 참조 관계를 정리한다.

| 본 표준 절 | AIRD-STD-001 참조 절 | AIRD-STD-003 참조 절 | 연계 내용 |
|---|---|---|---|
| 1.4 관련 표준 연계 | 전체 | 전체 | 표준 시리즈 역할 분담 개요 |
| 2.1 통합 상태 모델 | 7장 Q-Tier 판정 | 4~7절 Gate 기준 | 전이 조건 정합성 |
| 4.2 품질 메타데이터 | 5~6장 측정 공식 | 6절 Stage 2 | 측정 방법(STD-001) → 기록 스키마(STD-002) |
| 4.2.2 `aird:columnQualityBreakdown` | 5장 지표별 결과 | 부속서 E `IndicatorResult.details` | Column-level 세부 결과 허용(MAY) |
| 4.2.3 컬럼 스키마 (`csvw:tableSchema`) | — | — | W3C CSVW 기반. `aird:schemaConformanceRate`의 기준 스키마 |
| 4.3 프로브넌스 | — | 8절 Provenance + 부속서 B | Activity 타입 구분 규칙. 부속서 B가 규범적 참조 |
| 4.4 Purpose-Readiness Vector | — | 7절 Stage 3 | 벡터 구조 → 메타데이터 기록 |
| 5.3 ML/DL Profile | — | 7.4.1 ML/DL 메타데이터 | Croissant 확장 연계 |
| 5.4 RAG Profile | — | 7.4.2 RAG 메타데이터 | AIRD-RAG 확장 Candidate |
| 5.5 KG Profile | — | 7.4.3 KG 메타데이터 | VoID + SHACL |
| 5.6 Stats Profile | — | 7.4.4 Stats 메타데이터 | SDMX/Croissant 선택 기준표 참조 |
| 7.2 Quality-Ready 전이 조건 | 7장 Q-Tier 판정 | 6.5 Gate 2 판정 | **단일 출처: 본 표준 7.2절** |
| 8 적합성 프레임워크 | 10장 적합성 | 12절 적합성 | 3단계 적합성 정합 |
| 9 필드 매핑 테이블 | 전체 필드명 | — | STD-001 커스텀 필드 → 국제 표준 어휘 정규 매핑 |
| 부록 B.3 ML 예제 | — | 부속서 C.1 ML Pack | ML Pack 변환 시나리오와 메타데이터 연계 |

*— 끝 —*
