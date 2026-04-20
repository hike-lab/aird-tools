# AI-Ready Data Transformation & Governance Specification
## AI-Ready 데이터 변환 및 거버넌스 규격

| 항목 | 내용 |
|---|---|
| 문서 번호 | AIRD-STD-003 |
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
| AIRD-STD-002 | AI-Ready Data Metadata Profile | 메타데이터 항목·레이어·스키마 — 기술·기록 |
| **AIRD-STD-003** | **AI-Ready Data Transformation & Governance Specification (본 표준)** | ETL 파이프라인·Gate 판정·AIRD Pack·거버넌스 — 실행·운영 |
| AIRD-STD-005 | AI-Ready Data Discovery & Exchange Specification *(예정)* | Pack 탐색·교환·에이전트 인터페이스 — 탐색·배포 |
| AIRD-OPG-001 | AI-Ready Data 품질 진단 운영 지침 *(예정)* | 진단 주기·유효기간·이의제기·도구 인증 — 운영 세부 |
| AIRD-TR-001 | 가중치 설계 기술 보고서 *(예정)* | Purpose-Type별 가중치 수치 근거 |

> **설계 원칙**
>
> 이 표준은 Quality-Ready Data Preparation Framework(AIRD-STD-001)이 만든 품질 진단 결과를 **소비(consume)** 하고, AI-Ready Data Metadata Profile(AIRD-STD-002)이 정의한 메타데이터 필드를 **채우는(populate)** 실행 절차 표준이다. 측정 공식과 스키마를 재정의하지 않는다.
>
> 네 가지 원칙이 적용된다.
>
> 첫째, **Gate가 파이프라인의 실질적 통제 지점이다.** QI 점수가 아니라 Gate 판정이 상태 전이를 결정한다. 점수가 높아도 Gate를 통과하지 못하면 전이가 차단된다.
>
> 둘째, **단일 출처 원칙을 준수한다.** Quality-Ready 전이 조건은 AI-Ready Data Metadata Profile(AIRD-STD-002) 7.2절이 단일 출처이며, 이 표준은 그 조건을 그대로 적용한다. 수치를 독립적으로 재정의하지 않는다.
>
> 셋째, **DM(진단 성숙도)이 운영에 실질적 의미를 갖는다.** DM-1 Q-Tier로는 공식 공시가 불가하며, 이를 파이프라인 산출물에 명시하여 다운스트림 사용자가 혼동하지 않도록 한다.
>
> 넷째, **실무자가 체크리스트로 실행할 수 있는 수준으로 명세한다.** 각 Stage의 입출력 아티팩트와 Gate 판정 조건을 구체적으로 기술한다.

---

## 서문

인공지능 기술의 확산과 함께 데이터를 AI 파이프라인에 즉시 투입 가능한 상태로 정비해야 할 필요성이 공공·민간·연구 영역 전반에서 커지고 있다. 단순히 데이터를 공개하는 것을 넘어, AI 모델 학습·추론·검색증강생성(RAG)·지식 그래프 구축 등 다양한 목적에 맞게 품질을 측정하고 변환하여 제공하는 체계가 요구된다.

AI-Ready 데이터 표준 시리즈(AIRD)는 이러한 필요에 대응하여 구성된다.

- **Quality-Ready Data Preparation Framework (AIRD-STD-001)** — 품질 측정 기준과 판정 로직을 정의한다.
- **AI-Ready Data Metadata Profile (AIRD-STD-002)** — 메타데이터 기술 스키마를 정의한다.
- **AI-Ready Data Transformation & Governance Specification (AIRD-STD-003)** — 실행 절차를 정의한다(이 표준).

AIRD-STD-001이 "무엇을 측정·판정할 것인가"를, AIRD-STD-002가 "무엇을 기록·표현할 것인가"를 규정한다면, 이 표준(AIRD-STD-003)은 "어떻게 실행·운영할 것인가"를 규정함으로써 세 표준이 유기적으로 결합하여 AI-Ready 데이터 전환을 체계적으로 지원한다.

이 표준의 기술 내용은 데이터의 출처(공공/민간)나 보유 주체의 성격과 무관하게 적용 가능하다. 국내 공공데이터 관리체계와의 연계 방안은 AIRD-STD-002 부록 A(참고)를 참조한다.

---

## 머리말

이 표준은 AI 활용 목적의 데이터셋을 Raw 상태에서 Quality-Ready 상태를 거쳐 Purpose-Ready 상태로 전환하는 파이프라인의 실행 절차, Gate 판정, Provenance 기록, Extension Profile 등록 거버넌스를 규정한다.

이 표준은 Quality-Ready Data Preparation Framework(AIRD-STD-001)이 정의한 품질 측정 기준과 판정 로직, AI-Ready Data Metadata Profile(AIRD-STD-002)이 정의한 메타데이터 스키마를 전제로 하며, 그 요구사항을 실제 운영 환경에서 실행하기 위한 절차적 규격을 제공한다.

세 가지 목적을 위해 제정한다.

1. **실행 가능성(Executability):** 파이프라인의 각 단계를 구체적 입출력과 판정 조건으로 명세하여 자동화 구현이 가능하도록 한다.
2. **추적 가능성(Traceability):** 데이터 변환의 전 과정을 Provenance 기록으로 남겨 감사·재현이 가능하도록 한다.
3. **확장 가능성(Extensibility):** 새로운 Purpose-Type의 수용을 위한 Extension Profile 등록 거버넌스를 제공한다.

---

## 목차

1. 적용 범위
2. 인용 표준
3. 용어 및 정의
4. 파이프라인 아키텍처
5. Stage 1: Ingestion (수집·등록)
6. Stage 2: Quality Evaluation (품질 평가)
7. Stage 3: Purpose Packaging (목적별 패키징)
8. Provenance 기록 규격
9. 재현성 보장 규격
10. 파이프라인 운영 규칙
11. Extension Profile 등록 거버넌스
12. 적합성

**부속서**
- 부속서 A (규범적): Gate 판정 절차서
- 부속서 B (규범적): Provenance JSON-LD 예시
- 부속서 C (참고): Purpose-Type별 파이프라인 예시
- 부속서 D (참고): Extension Profile 등록 템플릿
- 부속서 E (참고): 표준 간 참조 매트릭스
- 부속서 F (참고): Value-level 이상 탐지 규칙 로드맵

---

## 1. 적용 범위

### 1.1 목적 및 적용 대상

이 표준은 AI 활용 목적의 데이터셋을 **Raw → Quality-Ready → Purpose-Ready** 상태로 전환하는 3-Stage 파이프라인에 대하여 다음 사항을 규정한다.

**(a)** 3-Stage 파이프라인(Ingestion → Quality Evaluation → Purpose Packaging)의 실행 절차 및 각 Stage의 입출력 아티팩트

**(b)** 각 Stage 간 전이를 통제하는 Gate(Gate 1/2/3)의 판정 기준 및 절차

**(c)** 파이프라인 전 과정의 데이터 Provenance 기록 규격

**(d)** 파이프라인 실행의 재현성(Reproducibility) 보장 요건

**(e)** Extension Profile 등록·버전관리 거버넌스

**(f)** 오류 처리, 갱신, 책임 주체 등 파이프라인 운영 규칙

**적용 대상:**

| 구분 | 대상 | 적용 의무 |
|---|---|---|
| 필수 적용 | 공공기관이 보유한 AI 활용 목적 데이터셋 | SHALL |
| 준용 권장 | AI 학습·운용 목적의 민간 데이터셋, 연구기관 데이터셋, 기업 내부 데이터 파이프라인 | MAY |

이 표준의 기술 내용 — 3-Stage 파이프라인, Gate 판정, AIRD Pack, Provenance, Extension Profile 거버넌스 — 은 데이터의 출처(공공/민간)나 보유 주체의 성격과 무관하게 적용 가능하다.

> **참고** 이 표준은 파이프라인의 "무엇을 해야 하는가(what)"를 규정하며, "어떤 도구·언어로 구현하는가(how)"는 규정하지 않는다.

### 1.2 적용 범위 외

| 사항 | 담당 문서 |
|---|---|
| 품질 측정 공식·QI 산정·Q-Tier 판정 알고리즘 | Quality-Ready Data Preparation Framework (AIRD-STD-001) |
| 메타데이터 스키마·제어 어휘·검증 규칙 | AI-Ready Data Metadata Profile (AIRD-STD-002) |
| Pack 탐색 API·에이전트 인터페이스·배포 규격 | AI-Ready Data Discovery & Exchange Specification (AIRD-STD-005, 예정) |
| 진단 주기·결과 유효기간·이의제기·도구 인증 | AIRD-OPG-001 (예정) |
| Purpose-Type별 가중치 수치 근거 | AIRD-TR-001 (예정) |
| 각 Purpose-Type의 성능 평가 방법론·기준 | 도메인별 기술규격 (위임) |
| AI 모델 파일·추론 시스템·서비스 엔드포인트 | 모델 레지스트리 / MLOps 표준 |
| Value-level 이상 탐지 규범적 규칙 | 본 표준 v1.1~v1.5 (부속서 F 참조) |

> **설계 원칙**
>
> **상태 표준:** 본 표준은 데이터셋의 AI 활용 준비 상태(Readiness State)를 전환·관리하는 실행 절차를 규정한다. 모델 구성·성능 기준은 도메인 기술규격에 위임하고, 참조 방식만 표준화한다.
>
> **모델-데이터 분리:** AIRD Pack은 AI 모델 파일을 포함하지 않는다. 모델은 변환 수단으로 간주하며, 모델에 의해 생성된 파생 데이터(벡터·인덱스 등)는 Pack에 포함될 수 있다. 이 경우 모델 참조 정보는 필수 기록한다(SHALL).
>
> **기술 스택 중립:** AI 에이전트·A2A·MCP 등 소비 방식의 변화에 대해 특정 기술 스택을 규범적으로 명시하지 않는다. 에이전트 인터페이스 및 탐색 API는 AI-Ready Data Discovery & Exchange Specification(AIRD-STD-005)에서 정의한다.

---

## 2. 인용 표준

### 2.1 내부 표준

| 표준번호 | 표준명 | 버전 | 비고 |
|---|---|---|---|
| AIRD-STD-001 | Quality-Ready Data Preparation Framework | v0.1 | 품질 측정·판정 원칙·공식 |
| AIRD-STD-002 | AI-Ready Data Metadata Profile | v0.1 | 메타데이터 스키마·제어 어휘 |

### 2.2 외부 표준

| 표준 / 규격 | 발행 기관 | 적용 내용 |
|---|---|---|
| PROV-O: The PROV Ontology | W3C | Provenance 온톨로지 |
| DCAT v3 | W3C | 데이터 카탈로그 어휘 |
| DQV (Data Quality Vocabulary) | W3C | 데이터 품질 어휘 |
| W3C CSVW | W3C | 테이블형 데이터 컬럼 스키마 |
| Croissant 1.0 | MLCommons | ML 데이터셋 메타데이터 |
| VoID | W3C | 링크드 데이터셋 기술 |
| ISO 8601:2019 | ISO | 일시 표기 |
| SemVer 2.0.0 | semver.org | 버전 체계 |
| RFC 6920 | IETF | Named Information URI |

---

## 3. 용어 및 정의

이 표준에서 사용하는 용어 중 Quality-Ready Data Preparation Framework(AIRD-STD-001) 및 AI-Ready Data Metadata Profile(AIRD-STD-002)에서 정의된 용어는 해당 표준의 정의를 따른다.

> **AIRD-STD-001 승계 용어:** Quality-Ready, 품질 차원(D1~D6), QI, Q-Tier(Tier 0~4), 필수 게이트(Mandatory Gate), PRECONDITION_UNMET, 진단 성숙도(DM), 공식 가중치/조정 가중치, 컬럼 수준 진단
>
> **AIRD-STD-002 승계 용어:** Raw, Purpose-Ready, Stale, metadata.status, AIRD Pack, Layer 1/2/3, purposeReadinessVector, aird:PreprocessingActivity, aird:TransformationActivity, 모델-데이터 결합도, Pack 완전성, 파생 데이터, Fine-tuning Pack

이 표준에서 추가로 정의하는 용어는 다음과 같다.

### 3.1 파이프라인 (Pipeline)

데이터셋을 Raw 상태에서 Purpose-Ready 상태로 전환하기 위해 순서대로 실행되는 Stage와 Gate의 연결 구조. 이 표준에서 파이프라인은 Stage 1(Ingestion) → Gate 1 → Stage 2(Quality Evaluation) → Gate 2 → Stage 3(Purpose Packaging) → Gate 3 의 순서로 실행된다.

### 3.2 스테이지 (Stage)

파이프라인을 구성하는 개별 처리 단계. 각 Stage는 정의된 입력 아티팩트를 받아 처리를 수행하고 출력 아티팩트를 산출한다. 이 표준에서는 Ingestion, Quality Evaluation, Purpose Packaging 의 3개 Stage를 정의한다.

### 3.3 품질 게이트 (Quality Gate)

하나의 Stage 완료 후 다음 Stage로의 전이를 허용할지 판정하는 검사 지점. 게이트는 사전에 정의된 조건을 검사하여 판정 결과(Gate Verdict)를 산출한다.

### 3.4 게이트 판정 (Gate Verdict)

품질 게이트의 검사 결과. 다음 세 값 중 하나를 가진다.

| 판정값 | 의미 | 적용 Gate |
|---|---|---|
| **PASS** | 모든 조건 충족. 정방향 전이 허용 | Gate 1, Gate 2, Gate 3 |
| **CONDITIONAL** | 핵심 조건 충족, 보조 조건 미충족. 조건부 전이 허용 (조건 기록 필수) | Gate 2 한정 |
| **FAIL** | 필수 조건 미충족. 전이 차단 | Gate 1, Gate 2, Gate 3 |

> **CONDITIONAL은 Gate 2에만 적용된다.** Gate 2 CONDITIONAL의 발생 조건은 6.5절에서 정의한다. Gate 1과 Gate 3은 PASS 또는 FAIL만 산출한다.

### 3.5 상태 전이 (State Transition)

데이터셋의 `aird:metadataStatus` 값이 하나의 상태에서 다른 상태로 변경되는 것. 전이 규칙은 다음과 같다.

**(a) 정방향 전이:** Gate 판정이 PASS 또는 CONDITIONAL인 경우에만 허용된다.

**(b) 역방향 전이 (Quality-Ready → Raw):** Gate 판정 없이 허용된다. 단, 역방향 전이 시 변경 주체·일시·사유를 Provenance 기록에 남겨야 한다(SHALL). 역방향 전이 후 데이터셋의 품질 점수 필드(`aird:qualityIndex`, `aird:qualityTier`)는 삭제하거나 무효 표기하여야 한다(SHALL). AIRD-STD-002 2.3절 참조.

**(c) Raw → Purpose-Ready 직접 전이:** 금지된다(SHALL NOT). 반드시 Quality-Ready 상태를 경유하여야 한다.

> **Raw 상태 금지 규칙(AIRD-STD-002 2.1절 연계):** Raw 상태의 데이터셋은 품질 점수 필드를 포함하여서는 안 된다(SHALL NOT).

### 3.6 체크포인트 (Checkpoint)

파이프라인 실행 중 특정 시점의 데이터셋 및 메타데이터 상태를 저장한 스냅샷. 오류 발생 시 롤백의 기준점으로 사용된다. 체크포인트는 각 Gate 판정 직전에 생성하여야 한다(SHALL).

### 3.7 멱등성 (Idempotency)

동일한 입력과 동일한 파라미터로 파이프라인을 반복 실행했을 때, 동일한 출력이 산출되는 성질. 비결정론적 요소(난수 기반 데이터 분할 등)를 포함하는 경우 시드(seed) 값을 Provenance에 기록하여 재현성을 보장한다(9장 참조).

### 3.8 Extension Profile

AI-Ready Data Metadata Profile(AIRD-STD-002)에서 정의한 코어 메타데이터 스키마를 특정 Purpose-Type의 요구에 맞게 확장한 프로파일. 11장의 등록 절차를 통해 관리된다. 각 Extension Profile은 네임스페이스(`aird-{type}:`), 정량 요건, 변환 규칙, Layer 3 메타데이터 스키마, 검증 방법을 포함하여야 한다(SHALL).

### 3.9 네임스페이스 (Namespace)

메타데이터 속성의 이름 충돌을 방지하기 위해 속성 URI에 부여하는 접두어 체계.

| 네임스페이스 | 패턴 | 관리 주체 | 비고 |
|---|---|---|---|
| 코어 | `aird:` | AIRD 표준 시리즈 | 변경 불가(SHALL NOT) |
| 확장 | `aird-{type}:` | Extension Profile 등록부 | 등록 후 사용 가능 |

현재 등록된 확장 네임스페이스: `aird-rag:` (Candidate 상태, v0.2 확정 예정), `aird-kg:`, `aird-stats:`

### 3.10 AIRD Pack

Stage 3 Purpose Packaging의 최종 출력물. 변환된 데이터 파일과 AIRD-STD-002 Layer 3 메타데이터(`metadata.json`)를 하나의 디렉터리 단위로 묶은 패키지. AIRD Pack의 구조 및 Manifest 규격은 7.4절에서 정의한다.

### 3.11 DM-게이트 조건 (DM Gate Condition)

Gate 2 판정 시 Q-Tier와 함께 적용되는 진단 성숙도(DM) 조건. DM-1에서 산출된 Q-Tier는 내부 참고용으로만 허용되며, 공식 공시 경로로는 전달되지 않는다. AIRD-STD-001 4.4절 참조.

### 3.12 소비자 피드백 루프

데이터 소비자(사람 또는 AI 시스템)가 AIRD Pack 활용 중 발견한 문제를 공급자 파이프라인에 신호로 전달하는 구조. 신호 유형은 다음 세 가지로 분류한다.

| 유형 | 설명 | 후속 조치 |
|---|---|---|
| **유형 A (구조적 오류)** | 데이터 파싱 실패, 스키마 불일치, 체크섬 불일치 | Stage 3 즉시 재패키징 (SHALL) |
| **유형 B (품질 저하)** | AI 모델 성능 지표가 Purpose-Tier 기준 이하 하락 | Stage 2 재평가 검토 트리거 (SHOULD) |
| **유형 C (데이터 노후화)** | 원본 데이터 갱신 후 Pack 미재생성 | `metadata.status` → `"Stale"` 전이 권고 (SHOULD) |

소비자 신호만으로 파이프라인이 자동 재실행되지 않아야 하며(SHALL NOT), 파이프라인 운영자의 판단을 거쳐야 한다. 신호 접수부터 조치 완료까지의 이력은 Provenance에 기록한다(SHALL).

---

## 4. 파이프라인 아키텍처

### 4.1 전체 구조 개요

이 표준의 파이프라인은 3개의 Stage와 3개의 Gate로 구성된다.

```
[원천 데이터]
      │
      ▼
┌─────────────┐
│  Stage 1    │  수집·오픈 포맷 변환·Layer 1 메타데이터 생성
│  Ingestion  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Gate 1    │  Layer 1 필수 항목·오픈 포맷·인코딩 검증
│  Raw 선언   │  → PASS / FAIL
└──────┬──────┘
       │ PASS
       ▼  status = "Raw"
┌─────────────────────┐
│      Stage 2        │  AIRD-STD-001 품질 진단 실행·QI·Q-Tier·DM 산정
│  Quality Evaluation │  Layer 2 메타데이터 생성
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       Gate 2        │  AIRD-STD-002 7.2절 전이 조건·Layer 2 필수 항목
│  Quality-Ready 전이 │  DM 수준 기록·편향성 기록 검증
└──────────┬──────────┘  → PASS / CONDITIONAL / FAIL
           │ PASS 또는 CONDITIONAL
           ▼  status = "Quality-Ready"
┌───────────────────┐
│      Stage 3      │  Purpose-Type별 변환·Layer 3 메타데이터 생성
│ Purpose Packaging │  AIRD Pack 출력·Provenance 완결
└──────────┬────────┘
           │
           ▼
┌───────────────────┐
│      Gate 3       │  Layer 3 필수 항목·무결성·purposeReadinessVector
│ Purpose-Ready 전이│  → PASS / FAIL
└──────────┬────────┘
           │ PASS
           ▼  status = "Purpose-Ready"
      [AIRD Pack]
```

### 4.2 표준 간 역할 분담

**표 4.1 — AIRD 표준 시리즈 역할 분담**

| 표준 | 핵심 질문 | 역할 | 이 표준과의 관계 |
|---|---|---|---|
| Quality-Ready Data Preparation Framework (AIRD-STD-001) | 무엇을 측정하고 어떻게 판정하는가? | 품질 측정·판정 원칙·공식 | Stage 2 실행의 측정 기준 제공 |
| AI-Ready Data Metadata Profile (AIRD-STD-002) | 측정 결과를 어떻게 기록하고 표현하는가? | 메타데이터 기술 스키마 | 각 Stage 출력 메타데이터 스키마 제공 |
| **AI-Ready Data Transformation & Governance Specification (AIRD-STD-003, 본 표준)** | **어떻게 자동화하여 운영하는가?** | **실행 파이프라인** | — |
| AIRD-OPG-001 | 언제, 누가, 어떻게 운영하는가? | 운영 세부 지침 | 운영 규칙 위임 수신 |

이 표준의 파이프라인 실행은 다음과 같이 선행 표준을 소비한다.

**(a)** Stage 2의 품질 평가는 AIRD-STD-001의 진단 프로브, 측정 공식, QI 산정 규칙(QI = Σ(Wi × Di)), Q-Tier 판정 알고리즘을 그대로 적용한다. 수치를 독립적으로 재정의하지 않는다.

**(b)** 각 Stage의 메타데이터 생성은 AIRD-STD-002의 해당 Layer 스키마를 충족하도록 필드를 채운다.

**(c)** Gate 2의 Quality-Ready 전이 조건은 AIRD-STD-002 7.2절을 단일 출처로 참조한다. 이 표준의 Gate 2 절(6.5절)은 해당 조건을 적용하는 절차만 규정한다.

### 4.3 상태 모델

데이터셋의 상태는 AIRD-STD-002 2.1절이 정의한 `aird:metadataStatus` 필드로 관리된다.

**표 4.2 — 허용 상태**

| 상태 | `aird:metadataStatus` 값 | 전제 조건 | 포함 메타데이터 |
|---|---|---|---|
| Raw | `"Raw"` | Gate 1 PASS | Layer 1 필수 항목만 |
| Quality-Ready | `"Quality-Ready"` | Gate 2 PASS 또는 CONDITIONAL | Layer 1 + Layer 2 |
| Purpose-Ready | `"Purpose-Ready"` | Gate 3 PASS | Layer 1 + Layer 2 + Layer 3 |

**표 4.3 — 상태 전이 규칙**

| 전이 | 조건 | 비고 |
|---|---|---|
| Raw → Quality-Ready | Gate 2 PASS 또는 CONDITIONAL | 정방향 전이 |
| Quality-Ready → Purpose-Ready | Gate 3 PASS | 정방향 전이 |
| Raw → Purpose-Ready | **금지(SHALL NOT)** | 직접 전이 불가 |
| Quality-Ready → Raw | Gate 없이 허용 | 역방향. 사유 기록 필수. 품질 점수 필드 삭제 필수. |

**상태 전이 기록 요건:** 모든 상태 전이 시 다음을 기록해야 한다(SHALL).

- 변경 주체 (기관 또는 시스템 식별자)
- 변경 일시 (ISO 8601)
- Gate 판정 결과 (역방향 전이 시 해당 없음)
- 전이 사유 (역방향 전이 시 필수, 정방향 시 권장)

### 4.4 DM(진단 성숙도)과 파이프라인의 관계

AIRD-STD-001이 정의한 DM 체계는 파이프라인 운영에 다음과 같이 연계된다.

```
     Q-Tier (데이터 품질 수준)
         높음 ↑
              │                ★ 공식 공시 가능 영역
     Platinum │                (DM-2 이상 + Q-Tier 임의)
         Gold ────────────────────────────────────
              │                │
       Silver ────────────────│────────────────────
              │                │
       Bronze ────────────────│────────────────────
              │                │
    Unqualified               │
         낮음 └────────────────┴──────────────────→ DM
                             DM-1         DM-2      DM-3
                        (내부 참고용) (공식 공시) (완전 적합성)
```

**DM 수준이 파이프라인에 미치는 영향:**

| DM 수준 | Gate 2 처리 | Stage 3 진입 | 공식 공시 경로 |
|---|---|---|---|
| DM-1 | PASS 가능 (단, DM-1 표기 필수) | 허용 (DM-1 표기 유지) | **차단** — AIRD Pack에 DM-1 표기 포함 |
| DM-2 | PASS (정규 Q-Tier) | 허용 | 허용 |
| DM-3 | PASS (완전 적합성 Q-Tier) | 허용 | 허용 (완전 적합성 선언 가능) |

---

## 5. Stage 1: Ingestion (수집·등록)

### 5.1 목적

원천 데이터를 수집하여 기계 판독 가능한 오픈 포맷으로 변환하고, AIRD-STD-002 Layer 1 필수 메타데이터를 생성하는 단계.

### 5.2 입력 아티팩트

| 아티팩트 | 설명 |
|---|---|
| 원천 데이터 파일 | 수집 대상 데이터 (포맷 무관) |
| 원천 메타데이터 | 제공기관이 보유한 기존 메타데이터 (있는 경우) |

### 5.3 처리 절차

Stage 1의 처리는 다음 순서로 진행한다(SHALL).

**(a) 원천 데이터 수집** — 원천 시스템 또는 저장소에서 데이터를 수집한다.

**(b) 오픈 포맷 변환** — 비개방 포맷(XLSX, HWP 등)을 오픈 포맷(CSV, JSON, Parquet 등)으로 변환한다.

**(c) 인코딩 정규화** — 문자 인코딩을 UTF-8로 정규화한다. 단, 데이터셋 유형·용도상 다른 인코딩이 필요한 경우 Layer 1 메타데이터(`aird:encoding`)에 명시한다.

**(d) Layer 1 메타데이터 생성** — AIRD-STD-002 3장의 필수 항목(표 5.1 참조)을 기록한다.

**(e) Provenance 기록 시작** — `aird:PreprocessingActivity` 타입의 Activity를 생성하고, 수집 방법·도구·실행 주체를 기록한다. 8장 참조.

**표 5.1 — Layer 1 필수 항목 체크리스트**

| 항목 | 속성 | 확인 |
|---|---|---|
| 고유식별자 | `dct:identifier` | □ |
| 제목(국문) | `dct:title` | □ |
| 설명 | `dct:description` | □ |
| 키워드 (3개 이상) | `dcat:keyword` | □ |
| 데이터셋 유형 | `dct:type` | □ |
| 언어 | `dct:language` | □ |
| 생성자 | `dct:creator` | □ |
| 게시자 | `dct:publisher` | □ |
| 관리 담당자 | `dcat:contactPoint` | □ |
| 갱신 주기 | `dct:accrualPeriodicity` | □ |
| 접근 URL | `dcat:accessURL` | □ |
| 다운로드 URL | `dcat:downloadURL` | □ |
| 매체 유형 | `dcat:mediaType` | □ |
| 배포 포맷 | `dct:format` | □ |
| 인코딩 | `aird:encoding` | □ |
| 라이선스 | `dct:license` | □ |
| 권한 | `dct:rights` | □ |
| 접근 제한 | `aird:accessRestriction` | □ |
| 비식별화 처리 여부 | `aird:deidentification` | □ |
| 생성 방법 | `aird:creationMethod` | □ |
| 메타데이터 상태 | `aird:metadataStatus` = `"Raw"` 예정 | □ |

### 5.4 출력 아티팩트

| 아티팩트 | 설명 |
|---|---|
| 오픈 포맷 데이터 파일 | UTF-8 인코딩, 오픈 포맷 |
| Raw Metadata (Layer 1) | AIRD-STD-002 3장 필수 항목 충족 JSON-LD |
| Stage 1 Provenance 로그 | `aird:PreprocessingActivity` Activity 기록 |

### 5.5 Gate 1: Raw 선언

Gate 1은 Stage 1 출력이 Raw 상태로 선언될 조건을 충족하는지 검사한다.

**판정 기준:**

| 검사 항목 | 기준 | 미충족 시 |
|---|---|---|
| Layer 1 필수 항목 완비 | 표 5.1의 전 항목 기록 완료 | FAIL |
| 오픈 포맷 확인 | 기계 판독 가능 오픈 포맷 여부 | FAIL |
| UTF-8 인코딩 또는 명시적 인코딩 선언 | 인코딩 정의 존재 | FAIL |

**판정 결과:** PASS → `aird:metadataStatus` = `"Raw"` 전이 및 체크포인트 생성. FAIL → Stage 1 재처리.

---

## 6. Stage 2: Quality Evaluation (품질 평가)

### 6.1 목적

Quality-Ready Data Preparation Framework(AIRD-STD-001)의 품질 진단 프레임워크를 적용하여 6개 품질 차원을 측정하고, QI·Q-Tier·DM을 산정하며, AI-Ready Data Metadata Profile(AIRD-STD-002) Layer 2 메타데이터를 생성하는 단계.

> **이 장의 측정 기준은 Quality-Ready Data Preparation Framework(AIRD-STD-001)을 원천으로 한다.** 이 장은 AIRD-STD-001의 측정 절차를 파이프라인 실행 맥락으로 적용하는 방법만 규정한다. 측정 공식·임계치·판정 알고리즘은 AIRD-STD-001을 참조한다.

### 6.2 입력 아티팩트

| 아티팩트 | 설명 |
|---|---|
| Raw 상태 데이터 파일 | Gate 1 PASS 후 산출된 오픈 포맷 파일 |
| Raw Metadata (Layer 1) | AIRD-STD-002 Layer 1 메타데이터 |
| 전제 조건 자료 | 업무 규칙 정의서, 마스터 코드 테이블, 참조 데이터 등 (있는 경우) |

### 6.3 처리 절차

Stage 2의 처리는 다음 순서로 진행한다(SHALL).

#### 6.3.1 데이터 유형 판정

AIRD-STD-001 표 4.2의 유형 분류(STRUCT / TEXT / IMAGE / TSERIES / FT)에 따라 데이터셋 유형을 결정한다. 복수 유형 포함 시 MIXED로 분류하고 유형별 QI를 별도 산출한다.

#### 6.3.2 전제 조건 확인 및 PRECONDITION_UNMET 처리

각 지표 측정 전 AIRD-STD-001 부속서 A에 명시된 전제 조건을 확인한다.

- 전제 조건 충족 시: `applicability = "APPLIED"` → 측정 실행
- 전제 조건 미충족 시: `applicability = "PRECONDITION_UNMET"` → 다음 처리 수행

**PRECONDITION_UNMET 처리 규칙:**

| 누적 횟수 (동일 지표) | 처리 | 보고 의무 |
|---|---|---|
| 1회 | Warning 기록, DM-2 허용(MAY) | 리포트 기록 |
| 2회 | Warning 기록, DM-1 강등 | 전담기관 보고 의무(SHALL) |
| 3회 이상 | 해당 차원 Q-Tier 게이트 Tier 1 고정, 전체 Q-Tier 강등 가능 | 전담기관 보고 + 개선계획 제출(SHALL) |

> **AIRD-STD-001 5.1절 4항 참조:** 동일 지표 3회 연속 PRECONDITION_UNMET 시 해당 차원의 Q-Tier 게이트 기준이 Tier 1(Bronze)로 고정된다.

리포트의 `preconditionCount` 필드에 누적 횟수를, `preconditionGuideRef` 필드에 AIRD-STD-001 부속서 F의 구축 단계 참조를 기록하여야 한다(SHALL).

#### 6.3.3 6개 품질 차원 측정

AIRD-STD-001 5장의 측정 공식을 데이터 유형에 따라 적용한다. 적용 지표는 AIRD-STD-001 표 8.1(유형별 지표 적용 매트릭스)을 따른다.

| 차원 | AIRD-STD-001 참조 절 |
|---|---|
| D1: 완전성 (Completeness) | 5.2절 |
| D2: 일관성 (Consistency) | 5.3절 |
| D3: 정확성 (Accuracy) | 5.4절 |
| D4: 적시성 (Timeliness) | 5.5절 |
| D5: 유효성 (Validity) | 5.6절 |
| D6: 유일성 (Uniqueness) | 5.7절 |

#### 6.3.4 QI 산정

AIRD-STD-001 6장의 산정 규칙에 따라 Quality Index를 산출한다.

**QI = Σ(Wi × Di)**  (AIRD-STD-001 6.2절)

- Wi: 공식 가중치 (AIRD-STD-001 표 6.1 참조)
- Di: 차원 i의 점수 (측정 가능 차원 기준 재배분 적용)
- D3 Case A/B/FULL에 따라 산정 방식 분기 (AIRD-STD-001 6.3절 참조)

> **산술 평균이 아닌 가중 합산이다.** 가중치 기본값: D1=0.20, D2=0.15, D3=0.25, D4=0.10, D5=0.15, D6=0.15. 기관이 Purpose-Type에 따라 조정 가중치(Adjusted Weight)를 사용할 수 있으나, 공식 Q-Tier 판정은 반드시 공식 가중치(Official Weight)를 사용한다(SHALL).

#### 6.3.5 Q-Tier 판정

AIRD-STD-001 7장의 판정 알고리즘을 적용한다.

**표 6.1 — Q-Tier 기준** (AIRD-STD-001 표 7.1)

| Q-Tier | 등급명         | QI 범위            | Quality-Ready 여부 |
| ------ | ----------- | ---------------- | ---------------- |
| Tier 4 | Platinum    | QI ≥ 0.95        | ●                |
| Tier 3 | Gold        | 0.85 ≤ QI < 0.95 | ●                |
| Tier 2 | Silver      | 0.70 ≤ QI < 0.85 | ●                |
| Tier 1 | Bronze      | 0.50 ≤ QI < 0.70 | ●                |
| Tier 0 | Unqualified | QI < 0.50        | —                |

> **QI만으로 Q-Tier가 결정되지 않는다.** AIRD-STD-001 7.2절의 필수 게이트(Mandatory Gate) 조건을 함께 적용하며, 게이트 미통과 시 해당 등급에서 강등(downgrade)된다. 판정 알고리즘은 AIRD-STD-001 7.4절 참조.

#### 6.3.6 진단 성숙도(DM) 산정

AIRD-STD-001 4.4절·8.2절의 기준에 따라 DM 수준을 결정한다.

| DM 수준 | 조건                           | 리포트 표기                     |
| ----- | ---------------------------- | -------------------------- |
| DM-1  | 유형별 필수(●) 지표의 50% 이상 APPLIED | `"Q-Tier (DM-1)"` — 내부 참고용 |
| DM-2  | 유형별 필수(●) 지표 전체 APPLIED      | `"Q-Tier"` — 공식 공시 가능      |
| DM-3  | 필수(●) + 선택(○) 지표 전체 APPLIED  | `"Q-Tier (DM-3)"` — 완전 적합성 |

#### 6.3.7 편향성·한계·결측치 정보 기록

AIRD-STD-002 4.2.4절의 신뢰·윤리 메타데이터를 기록한다.

- `rai:dataBiases`: 확인된 편향 유형 및 설명
- `rai:knownLimitations`: 구조적·내용적 제한사항
- `rai:dataCollectionMissingData`: 결측 비율 및 처리 방식

이 세 항목은 Gate 2 통과의 필수 조건이다(SHALL). 편향성이 없는 경우에도 "없음 확인" 기록을 남겨야 한다.

#### 6.3.8 Layer 2 메타데이터 생성

AIRD-STD-002 4장의 Layer 2 스키마에 따라 메타데이터를 생성한다. 각 항목의 의무수준은 AIRD-STD-002를 원천으로 하며, Gate 2 판정 시 SHALL 항목 누락은 FAIL, SHOULD 항목 누락은 CONDITIONAL 사유가 된다(6.5절 참조).

**표 6.2 — Layer 2 항목 의무수준 및 Gate 2 영향**

| 항목 | 속성 | 의무수준 | Gate 2 미충족 시 | AIRD-STD-002 참조 |
|---|---|---|---|---|
| 버전 번호 | `dcat:version` | **SHALL** | FAIL | 4.1절 |
| 최초 등록일 | `dct:issued` | **SHALL** | FAIL | 4.1절 |
| 최종 수정일 | `dct:modified` | **SHALL** | FAIL | 4.1절 |
| 버전 노트 | `adms:versionNotes` | **SHALL** | FAIL | 4.1절 |
| 품질 지수(QI) | `aird:qualityIndex` | **SHALL** | FAIL | 4.2.1절 |
| 품질 등급(Q-Tier) | `aird:qualityTier` | **SHALL** | FAIL | 4.2.1절 |
| DM 수준 | `aird:diagnosticMaturity` | **SHALL** | FAIL | AIRD-STD-001 4.4절 연계 |
| 품질 진단 일시 | `dqv:computedOn` | **SHALL** | FAIL | 4.2.1절 |
| 6개 차원 점수 | `dqv:value` × 6 | **SHALL** | FAIL | 4.2.2절 |
| 알려진 편향성 | `rai:dataBiases` | **SHALL** | FAIL | 4.2.4절 |
| 데이터 한계 | `rai:knownLimitations` | **SHALL** | FAIL | 4.2.4절 |
| 결측치 정보 | `rai:dataCollectionMissingData` | **SHALL** | FAIL | 4.2.4절 |
| 합성 데이터 여부 | `aird:isSynthetic` | **SHALL** | FAIL | 4.2.4절 |
| 전처리 Provenance | `prov:wasGeneratedBy` (PreprocessingActivity) | **SHALL** | FAIL | 4.3절 |
| 피처 완전성 지수 | `aird:featureCompletenessIndex` | **SHALL** | FAIL | 4.2.3절 |
| 스키마 적합률 | `aird:schemaConformanceRate` | **SHALL** | FAIL | 4.2.3절 |
| 컬럼 스키마 | `csvw:tableSchema` | SHOULD | CONDITIONAL | 4.2.3절 (정형 데이터 한정) |
| 클래스 균형도 | `aird:classBalanceIndex` | SHOULD | CONDITIONAL | 4.2.3절 |
| 이전 버전 | `dcat:previousVersion` | SHOULD | CONDITIONAL | 4.1절 |
| 데이터셋 시리즈 | `dcat:inSeries` | SHOULD | CONDITIONAL | 4.1절 |
| 품질 진단 도구 | `aird:qualityTool` | SHOULD | CONDITIONAL | 4.2.1절 |
| 레이블 적합률 | `aird:labelConformanceRate` | SHALL* | FAIL* | 4.2.3절 (*지도학습 한정) |

> **CONDITIONAL 판정 발생 조건:** SHOULD 항목 중 1개 이상 미충족 시 CONDITIONAL 판정이 가능하다(MAY). 단 SHALL 항목이 단 하나라도 누락되면 CONDITIONAL 불가, 반드시 FAIL이다.
>
> **`aird:featureCompletenessIndex`와 `aird:schemaConformanceRate`는 SHALL(필수)이다.** 이 두 항목은 AIRD-STD-002 4.2.3절에서 필수로 지정되어 있으며, CONDITIONAL 사유가 될 수 없다.

#### 6.3.9 품질 진단 리포트 산출

AIRD-STD-001 9장의 스키마에 따라 JSON 포맷의 품질 진단 리포트를 산출한다. 리포트는 Stage 2의 핵심 출력 아티팩트이며 Gate 2 판정의 입력이 된다.

리포트에 포함하여야 할 주요 필드:

- `diagnosticMaturity`: "DM-1" / "DM-2" / "DM-3"
- `preconditionGuideRef` (IndicatorResult): PRECONDITION_UNMET 시 AIRD-STD-001 부속서 F 단계 참조
- `preconditionCount` (IndicatorResult): 누적 선언 횟수
- `preconditionUpperBoundApplied` (QTierResult): 3회 상한 제한 적용 여부

### 6.4 출력 아티팩트

| 아티팩트 | 설명 |
|---|---|
| 품질 진단 리포트 | AIRD-STD-001 9장 스키마 JSON |
| Quality-Ready Metadata (Layer 2) | AIRD-STD-002 4장 필수 항목 충족 JSON-LD |
| Stage 2 Provenance 로그 | `aird:PreprocessingActivity` 업데이트 기록 |

### 6.5 Gate 2: Quality-Ready 전이 판정

> **Gate 2의 전이 조건 단일 출처는 AI-Ready Data Metadata Profile(AIRD-STD-002) 7.2절이다.** 이 절은 해당 조건을 파이프라인 판정 맥락에서 적용하는 절차를 규정한다. 조건 수치 자체는 AIRD-STD-002 7.2절을 참조한다.

#### 6.5.1 PASS 조건

다음 세 그룹의 조건을 모두 충족하면 PASS를 산출한다.

| 검사 그룹 | 검사 항목 | 기준 |
|---|---|---|
| **[A] 품질 전이 조건** (AIRD-STD-002 7.2절) | QI | ≥ 0.50 (Tier 1 Bronze 이상) |
| | Mandatory Gate 조건 | AIRD-STD-001 부속서 B의 Tier 1 임계치 전 차원 충족 |
| | D3(정확성) | ≥ 0.65 (D3 Case B 시 자동 면제) |
| **[B] Layer 2 SHALL 항목 완비** | 표 6.2의 SHALL 항목 전체 | 기록 완료 |
| **[C] 신뢰·윤리 기록** | `rai:dataBiases`, `rai:knownLimitations`, `rai:dataCollectionMissingData` | 6.3.7절 전 항목 — SHALL |

#### 6.5.2 CONDITIONAL 조건

[A]·[B]·[C]를 모두 충족하나, 표 6.2의 **SHOULD 항목 중 일부가 미충족**인 경우 CONDITIONAL을 산출할 수 있다(MAY).

> **CONDITIONAL 적용 원칙:** SHALL 항목이 하나라도 누락되면 CONDITIONAL은 불가하며 반드시 FAIL이다. CONDITIONAL은 오직 SHOULD 항목 미충족에만 적용된다.

**CONDITIONAL 산출 시 처리:**

**(a) 상태 전이:** `aird:metadataStatus = "Quality-Ready"` 전이를 허용한다.

**(b) Gate Record 기록 (SHALL):** Gate 판정 기록(`gate-record.json`)에 다음을 명시한다.

```json
{
  "gateId": "Gate2",
  "verdict": "CONDITIONAL",
  "conditionalItems": [
    {
      "attribute": "csvw:tableSchema",
      "obligation": "SHOULD",
      "deadline": "2026-05-14",
      "status": "PENDING"
    }
  ],
  "suspendedAt": null,
  "resolvedAt": null
}
```

**(c) 보완 기한 경과 처리:** 보완 기한 내 미충족 항목을 보완하지 않은 경우, Gate Record의 `status`를 `"SUSPENDED"`로 변경하고 다음 조치를 취한다(SHALL).

- AIRD Pack이 이미 발행된 경우: manifest.json에 `"conditionalSuspended": true`를 추가하여 공시를 차단한다.
- Stage 3 진입이 시도되는 경우: Gate Record `status = "SUSPENDED"` 확인 후 진입을 차단한다.
- 보완 완료 시: Gate Record `status = "RESOLVED"`, `resolvedAt` 기록 후 정상 운영 복귀.

**(d) Stage 3 진입:** CONDITIONAL 데이터셋은 Gate Record `status = "PENDING"` 상태에서 Stage 3 진입이 가능하다.

#### 6.5.3 FAIL 조건

다음 중 하나라도 해당하면 FAIL을 산출한다.

- [A] 품질 전이 조건 미충족
- [B] SHALL 항목 누락
- [C] 편향성·한계·결측치 기록 누락

FAIL 시 처리:
- `aird:metadataStatus`는 `"Raw"` 유지.
- 품질 진단 리포트의 `downgradeReason` 및 `improvementSuggestion`을 담당자에게 전달한다.
- 체크포인트로 롤백하고 Stage 2를 재실행한다.

#### 6.5.4 DM 수준 기록

Gate 2 PASS/CONDITIONAL 시 DM 수준을 판정 기록에 포함한다.

- DM-1: Layer 2 메타데이터와 AIRD Pack(이후 생성 시)에 `aird:diagnosticMaturity = "DM-1"` 표기 유지. 공식 공시 차단 플래그 설정(SHALL).
- DM-2/DM-3: 정규 Q-Tier로 공시 경로 허용.

---

## 7. Stage 3: Purpose Packaging (목적별 패키징)

### 7.1 목적

Quality-Ready 상태의 데이터를 특정 Purpose-Type(ML, DL, RAG, KG, Stats, FineTuning)에 최적화된 형태로 변환하고, AIRD-STD-002 Layer 3 메타데이터를 생성하여 AIRD Pack으로 패키징하는 단계.

### 7.2 입력 아티팩트

| 아티팩트 | 설명 |
|---|---|
| Quality-Ready 데이터 파일 | Gate 2 PASS/CONDITIONAL 후 데이터 |
| Quality-Ready Metadata (Layer 1+2) | AIRD-STD-002 Layer 1+2 메타데이터 |
| 품질 진단 리포트 | Stage 2 산출 JSON 리포트 |
| Purpose-Type 사양 | 대상 Purpose-Type 및 Extension Profile |

### 7.3 Purpose-Type별 변환 개요

**표 7.1 — Purpose-Type별 변환 및 메타데이터**

| Purpose-Type | 핵심 변환 | 기반 표준 | Coupling | Extension Profile 상태 |
|---|---|---|---|---|
| ML Pack | 분할(Train/Valid/Test)·라벨 지정·피처 정의 | Croissant 1.0 | `loose` | **Registered** |
| DL Pack | ML Pack + 전처리 파이프라인 명세 | Croissant 1.0 | `loose` | **Registered** |
| RAG Pack | 청킹·임베딩·벡터 인덱스 구축 | Croissant + `aird-rag:` | `derived` | **Candidate** |
| KG Pack | 엔티티 추출·정규화·RDF 변환·온톨로지 매핑 | VoID + DCAT | `loose` | **Registered** |
| Stats Pack | 차원 정의·집계 규칙·코드리스트 매핑 | SDMX 또는 Croissant* | `loose` | **Registered** |
| Fine-tuning Pack | 지시문-응답 페어 생성·정제·분할 | AIRD-FT 확장 | `derived` | **Draft (등록 절차 예정)** |

> **Stats Pack 표준 선택 기준 (AIRD-STD-002 5.6절 참조):** SDMX 다차원 큐브가 필요한 경우 SDMX 적용, 단순 집계 테이블인 경우 Croissant 적용.
>
> **Candidate Profile 사용 시 주의:** RAG Pack 적용 시 manifest.json에 `"profileStatus": "Candidate"` 명시 필수(SHALL). 11.4절 참조.
>
> **모델-데이터 결합도(Coupling) 원칙:** AIRD Pack은 모델 파일을 포함하지 않는다. `loose`는 데이터가 모델과 독립적임을, `derived`는 모델 산출물(벡터·인덱스·페어 등)이 Pack 구성에 포함됨을 의미한다.

### 7.4 AIRD Pack 구조

AIRD Pack은 다음 구조의 디렉터리 패키지로 구성된다(SHALL).

```
{dataset-id}-{purpose-type}-pack-v{version}/
├── metadata.json          # AIRD-STD-002 Layer 3 메타데이터 (필수)
├── manifest.json          # 파일 목록·체크섬·버전 (필수)
├── provenance.jsonld      # Provenance 기록 전체 (필수)
├── data/                  # 변환된 데이터 파일 (필수)
│   ├── train.csv          # (ML Pack 예시)
│   ├── valid.csv
│   └── test.csv
└── quality-report.json    # Stage 2 품질 진단 리포트 사본 (필수)
```

**manifest.json 필수 필드:**

```json
{
  "packId": "...",
  "datasetId": "...",
  "purposeType": "ML",
  "packVersion": "1.0.0",
  "diagnosticMaturity": "DM-2",
  "qualityTier": "Gold",
  "createdAt": "2026-04-14T09:00:00+09:00",
  "sourceDataVersion": "1.2.0",
  "modelDataCoupling": "loose",
  "packCompleteness": "data-only",
  "agentAccessible": true,
  "files": [
    {"path": "data/train.csv", "sha256": "...", "byteSize": 0},
    {"path": "metadata.json",  "sha256": "...", "byteSize": 0}
  ]
}
```

> `diagnosticMaturity = "DM-1"` 인 경우 manifest.json에 `"officialPublicationBlocked": true` 필드를 포함하여야 한다(SHALL).

### 7.5 처리 절차

Stage 3의 처리는 다음 순서로 진행한다(SHALL).

**(a) Purpose-Type 선택 및 Extension Profile 확인** — 대상 Purpose-Type의 Extension Profile이 11장 등록부에 등록되어 있는지 확인한다. 미등록 Profile 사용 금지(SHALL NOT).

**(b) 변환 실행** — Extension Profile의 변환 규칙에 따라 데이터를 변환한다. 원본 Quality-Ready 파일은 변환 후에도 보존한다(SHALL).

**(c) Layer 3 메타데이터 생성** — AIRD-STD-002 5장의 해당 Purpose-Type Profile 필수 항목을 생성한다. `aird:TransformationActivity` 타입의 Provenance Activity를 기록한다.

**(d) purposeReadinessVector 갱신** — Layer 2 메타데이터의 `aird:purposeReadinessVector`에 해당 Purpose-Type의 Tier를 기록한다.

**(e) AIRD Pack 조립** — 7.4절의 구조에 따라 파일을 배치하고 manifest.json을 생성한다.

**(f) 무결성 검증** — 모든 파일의 SHA-256 체크섬을 산출하여 manifest.json에 기록한다.

### 7.6 Q-Bronze 데이터의 Stage 3 진입 조건

Q-Tier ≥ Tier 1(Bronze)이면 Stage 3 진입이 원칙적으로 가능하다. 단, 다음 규칙이 적용된다.

**(a) Extension Profile 내 차원 조건 의무화 (SHALL)**

공식 등록된 모든 Extension Profile은 `min_qtier` 외에 **Purpose-Type 특성을 반영한 차원별 최소 점수 조건**을 반드시 포함하여야 한다(SHALL). `min_qtier: Bronze`만을 단독 기준으로 사용하는 Profile은 등록이 허용되지 않는다(SHALL NOT).

```yaml
# Extension Profile 정량 요건 예시 (올바른 작성)
quantitative_requirements:
  min_qtier: "Bronze"
  required_dimensions:          # 반드시 1개 이상 포함 (SHALL)
    - "D1(완전성) >= 0.70"
    - "D3(정확성) >= 0.70"
```

**(b) Bronze 허용 Profile의 공시 제한**

Q-Tier Bronze 데이터로 생성된 AIRD Pack은 manifest.json에 다음을 명시하여야 한다(SHALL).

```json
{
  "qualityTier": "Bronze",
  "bronzeUsageNote": "Q-Bronze 데이터 기반 Pack. 고위험 공공서비스 또는 AI 학습 단독 사용에 적합하지 않을 수 있습니다. Extension Profile 정량 요건을 확인하십시오."
}
```

### 7.7 출력 아티팩트

| 아티팩트 | 설명 |
|---|---|
| AIRD Pack 디렉터리 | 7.4절 구조의 완성된 패키지 |
| Stage 3 Provenance 로그 | `aird:TransformationActivity` 기록 |

### 7.8 Gate 3: Purpose-Ready 전이 판정

#### 7.8.1 PASS 조건

다음 조건을 모두 충족하면 PASS를 산출한다.

| 검사 항목 | 기준 |
|---|---|
| Layer 3 필수 항목 완비 | 해당 Purpose-Type Extension Profile의 필수 항목 전부 |
| 무결성 | manifest.json의 모든 파일 SHA-256 일치 |
| `purposeReadinessVector` 기록 | 해당 Purpose-Type의 Tier 기록 완료 |
| AIRD Pack 구조 | 7.4절 필수 파일 전부 존재 |
| DM 표기 일관성 | manifest.json의 `diagnosticMaturity`가 Layer 2와 일치 |

#### 7.8.2 FAIL 조건

위 조건 중 하나라도 미충족 시 FAIL. `aird:metadataStatus`는 `"Quality-Ready"` 유지. 체크포인트로 롤백 후 Stage 3 재실행.

---

## 8. Provenance 기록 규격

### 8.1 목적 및 원칙

파이프라인의 모든 처리 단계를 W3C PROV-O 기반으로 기록하여 감사·재현·신뢰성 확보를 지원한다.

**AIRD-STD-002 4.3절 연계:** 이 장의 JSON-LD 예시(부속서 B)는 AIRD-STD-002 4.3절이 규범적(normative) 참조로 지정한 자료이다. AIRD-STD-002 4.3절의 `prov:wasGeneratedBy` Activity 타입 구분 규칙을 준수한다.

### 8.2 Activity 타입 구분

| 파이프라인 단계 | Activity `@type` | 예시 URI 패턴 |
|---|---|---|
| Stage 1 (수집·변환·정규화) | `aird:PreprocessingActivity` | `aird:activity/preprocessing-{date}-{seq}` |
| Stage 2 (품질 진단) | `aird:PreprocessingActivity` | `aird:activity/quality-eval-{date}-{seq}` |
| Stage 3 (목적별 변환) | `aird:TransformationActivity` | `aird:activity/transform-{type}-{date}-{seq}` |

> Stage 1과 Stage 2는 모두 `aird:PreprocessingActivity` 타입이다. 두 단계를 하나의 Activity로 통합하거나 별도 Activity로 분리할 수 있다(MAY). 분리하는 경우 `prov:wasInformedBy`로 연결한다.

### 8.3 필수 기록 필드

각 Activity는 다음 필드를 포함하여야 한다(SHALL).

| 필드 | PROV-O 속성 | 필수 여부 |
|---|---|---|
| Activity 식별자 | `@id` | 필수 |
| Activity 타입 | `@type` | 필수 |
| 시작 일시 | `prov:startedAtTime` | 필수 |
| 종료 일시 | `prov:endedAtTime` | 필수 |
| 실행 주체 | `prov:wasAssociatedWith` | 필수 |
| 입력 엔티티 | `prov:used` | 필수 |
| 출력 엔티티 | `prov:generated` | 필수 |
| 파라미터 기록 | `aird:parameters` | 권장 |

### 8.4 엔티티 명명 규칙

```
aird:entity/{dataset-id}-{status}-v{version}.{ext}

예시:
aird:entity/factory-data-raw-v1.0.0.csv
aird:entity/factory-data-quality-ready-v1.0.0.csv
aird:entity/factory-data-ml-pack-v1.0.0
```

JSON-LD 전체 예시는 부속서 B를 참조한다.

---

## 9. 재현성 보장 규격

### 9.1 멱등성 요건

파이프라인은 동일한 입력과 파라미터로 반복 실행 시 동일한 출력을 산출하여야 한다(SHALL). "동일한 출력"의 판정 기준은 manifest.json에 기록된 각 파일의 SHA-256 체크섬 일치로 한다.

### 9.2 Canonical Serialization 원칙

SHA-256 체크섬 기반 재현성 판정이 실질적으로 작동하려면 직렬화 방식이 일관되어야 한다. 다음 원칙을 적용한다(SHALL).

**(a) JSON/JSON-LD 파일:** RFC 8785(JSON Canonicalization Scheme, JCS)에 따라 정규화된 형태로 직렬화한다. 키 순서는 사전순(lexicographic)으로 고정하고, 공백·줄바꿈은 제거한다.

**(b) CSV 파일:** 헤더 행을 포함하고, 줄 끝은 LF(`\n`)로 통일하며, 인코딩은 UTF-8 BOM 없음(UTF-8 without BOM)으로 고정한다.

**(c) 타임스탬프 필드:** Provenance의 시각 필드는 재현성 판정에서 제외한다. SHA-256 산출 대상은 데이터 파일과 메타데이터 파일에 한하며, Provenance 파일(`provenance.jsonld`)은 체크섬 산출에서 제외할 수 있다(MAY).

**(d) 바이너리 파일(벡터, 인덱스 등):** 파일 생성 도구와 버전을 Provenance에 기록하고(SHALL), 동일 도구·버전·파라미터로 재생성한 결과가 원본과 SHA-256이 일치함을 확인한다.

### 9.3 비결정론적 요소 처리

난수 기반 처리(Train/Valid/Test 분할 등)를 포함하는 경우 다음을 Provenance에 기록하여야 한다(SHALL).

- 난수 시드(seed) 값
- 사용 라이브러리·버전
- 분할 방법 (random / stratified 등)

### 9.4 환경 기록 요건

Stage별로 다음을 Provenance Activity의 `aird:parameters`에 기록하여야 한다(SHALL).

- 처리 도구명 및 버전
- 실행 일시 (ISO 8601)
- 주요 파라미터 목록

### 9.5 버전 관리

- 데이터셋 버전은 SemVer 2.0.0을 적용한다(SHALL).
- 품질 평가 결과가 변경되면 MINOR 버전을 증가한다.
- 데이터 내용이 변경되면 MAJOR 버전을 증가한다.

---

## 10. 파이프라인 운영 규칙

### 10.1 이 표준에서 직접 규율하는 핵심 규칙

**(a) 품질 진단 의무 시점 (SHALL)**

데이터셋 최초 등록 시 및 데이터 내용 변경 시 Stage 2를 재실행하여야 한다.

**(b) 책임 주체 (SHALL)**

파이프라인 실행의 1차 책임은 데이터 보유 기관(공공기관, 연구기관, 민간기업 등)에 있다. Gate 판정 결과의 검증 책임은 소관 전담 기관이 정하는 바에 따른다.

**(c) DM-1 공식 공시 차단 (SHALL)**

DM-1 Q-Tier로 산출된 AIRD Pack은 공식 데이터 카탈로그에 게시하여서는 안 된다(SHALL NOT). AIRD Pack의 `manifest.json`에 `"officialPublicationBlocked": true`를 포함하고, 수신 시스템은 이 플래그를 확인하여 게시를 차단하는 로직을 구현하여야 한다(SHALL).

**(d) OPG 위임 (SHALL)**

진단 주기의 세부 기준, 결과 유효기간, 이의제기 절차, 도구 인증 기준은 AIRD-OPG-001에서 정한다.

### 10.2 오류 처리 규칙

| 오류 유형 | 처리 방법 |
|---|---|
| Gate FAIL | 체크포인트로 롤백 후 해당 Stage 재실행 |
| Gate CONDITIONAL 미보완 (기한 경과) | `aird:metadataStatus` 유지. Gate Record `status = "SUSPENDED"` 변경. 공시 차단 및 Stage 3 진입 차단. |
| 처리 중 예외 발생 | 즉시 중단, 마지막 체크포인트로 롤백, 오류 로그 Provenance에 기록 |
| 전제 조건 미충족 (PRECONDITION_UNMET) | 6.3.2절의 누적 횟수 규칙 적용 |
| AIRD Pack 무결성 오류 | Stage 3 재실행 (데이터 재변환 불필요 시 재조립만 실행) |
| Gate Record SUSPENDED 상태에서 Stage 3 진입 시도 | 진입 차단. 담당자에게 CONDITIONAL 미보완 항목 및 보완 방법 안내 |

### 10.3 갱신 규칙

원본 데이터가 갱신된 경우 Stage 1부터 전체 파이프라인을 재실행하여야 한다. 단, 메타데이터만 변경된 경우 해당 메타데이터 항목을 갱신하고 버전을 증가시키는 것으로 갈음할 수 있다(MAY).

**Stale 상태 갱신 절차:**

`metadata.status = "Stale"`로 전이된 데이터셋에 대해 파이프라인 운영자는 다음 중 하나를 선택하여야 한다(SHALL).

| 조치 | 설명 | 적용 조건 |
|---|---|---|
| Stage 3 재실행 | 원본 Quality-Ready 데이터는 유효하며 패키징만 갱신 | 원본 데이터 변경 없이 Pack만 노후화된 경우 |
| Stage 1 전체 재실행 | 원본 데이터 자체가 갱신된 경우 | `aird:sourceDataVersion` 증가 시 |
| Stale 유지 선언 | 의도적으로 갱신하지 않는 경우 | 사유 기록 및 소비자 고지 필수 (SHALL) |

### 10.4 소비자 피드백 루프

3.12절에서 정의한 소비자 피드백 루프의 운영 절차를 규정한다.

#### 10.4.1 피드백 접수

파이프라인 운영자는 소비자(사람 또는 AI 시스템)로부터 유형 A·B·C 피드백 신호를 접수하는 경로를 운영하여야 한다(SHALL). 접수된 신호는 파이프라인 Provenance에 기록하여야 한다(SHALL).

#### 10.4.2 유형별 후속 조치

**(a) 유형 A (구조적 오류):** 접수 즉시 Gate 3 재판정을 실행한다(SHALL). 오류가 확인되면 Stage 3를 재실행한다(SHALL).

**(b) 유형 B (품질 저하):** 파이프라인 운영자가 영향 범위를 분석하고, 재평가 필요성을 판단하여 Stage 2 재실행 여부를 결정하여야 한다(SHOULD). 판단 결과와 근거는 이력으로 기록한다(SHALL).

**(c) 유형 C (데이터 노후화):** `metadata.status`를 `"Stale"`로 전이하고, 10.3절의 갱신 절차를 적용한다(SHOULD).

#### 10.4.3 자동화 금지

소비자 피드백 신호만으로 파이프라인이 자동 재실행되어서는 안 된다(SHALL NOT). 모든 재실행은 파이프라인 운영자의 명시적 승인을 거쳐야 한다.

---

## 11. Extension Profile 등록 거버넌스

### 11.1 Extension Profile 구성 요소

Extension Profile은 다음 5개 요소를 포함하여야 한다(SHALL).

| 번호 | 요소 | 설명 |
|---|---|---|
| 1 | 목적 정의 | 해당 Purpose-Type의 목적 및 대상 사용 시나리오 |
| 2 | 정량 요건 | 최소 Q-Tier, 최소 레코드 수, 필수 품질 차원 조건 |
| 3 | 변환 규칙 | Quality-Ready 데이터에서 해당 Purpose-Type으로의 변환 절차 |
| 4 | Layer 3 메타데이터 스키마 | 해당 Purpose-Type 전용 속성 정의 (URI, 범위, 카디널리티) |
| 5 | 검증 방법 | 변환 결과 적합성 검증 방법 및 통과 기준 |

등록 템플릿은 부속서 D를 참조한다.

### 11.2 네임스페이스 관리 규칙

**(a)** 코어 네임스페이스 `aird:`는 AIRD 표준 시리즈 전용이며 변경할 수 없다(SHALL NOT).

**(b)** 확장 네임스페이스는 `aird-{type}:` 패턴을 따르며, Extension Profile당 1개 할당한다.

**(c)** URI 패턴: `http://data.go.kr/ns/aird-{type}#`

**(d)** 모든 확장 네임스페이스는 등록부(Registry)에 등록 후 사용한다(SHALL).

**현재 등록 네임스페이스 (생애주기 상태 기준):**

| 네임스페이스 | Purpose-Type | 생애주기 상태 | 비고 |
|---|---|---|---|
| `aird-ml:` | ML Pack | **Registered** | — |
| `aird-dl:` | DL Pack | **Registered** | — |
| `aird-kg:` | KG Pack | **Registered** | — |
| `aird-stats:` | Stats Pack | **Registered** | — |
| `aird-rag:` | RAG Pack | **Candidate** | v0.2 Registered 전환 목표. URI 변경 가능 |
| `aird-ft:` | Fine-tuning Pack | **Draft** | 등록 심의 예정 |

### 11.3 버전 체계

Extension Profile에 SemVer 2.0.0을 적용한다(SHALL).

| 변경 유형 | 버전 증가 | 추가 요건 |
|---|---|---|
| MAJOR (하위 호환 불가) | X+1.0.0 | 마이그레이션 가이드 제공 의무 |
| MINOR (하위 호환, 필드 추가) | x.Y+1.0 | — |
| PATCH (오류 수정) | x.y.Z+1 | — |

### 11.4 등록 생애주기

```
Draft → Candidate → Registered → Deprecated
```

| 단계 | 정의 | 조건 | 권한 | 사용 가능 여부 |
|---|---|---|---|---|
| **Draft** | 제안자가 작성 중인 초안 | 제안자 제출 | 제안자 | 내부 실험 한정 |
| **Candidate** | 편집위원회 심의 중인 후보 Profile | 편집위원회 접수 후 심의 기간(최대 60일) | 편집위원회 | 조건부 사용 가능. 속성 URI 변경 가능성 명시 필수 |
| **Registered** | 심의 통과, 등록부 정식 등재 | 편집위원회 의결 | 편집위원회 | 정식 사용 가능 |
| **Deprecated** | 후속 Profile로 대체 완료 | Governance Authority 승인 | Governance Authority | 사용 금지. 마이그레이션 가이드 제공 |

> **Candidate 상태 사용 규칙:**
> Candidate Profile을 적용하여 생성한 AIRD Pack은 manifest.json에 `"profileStatus": "Candidate"` 를 명시하여야 한다(SHALL). Candidate 상태의 속성 URI는 Registered 전환 시 변경될 수 있으며, 구현체는 이를 감안하여야 한다.

---

## 12. 적합성

> **운영 상태(status)와 적합성(conformance)은 독립적인 두 축이다.**
>
> - **`aird:metadataStatus`(운영 상태):** 데이터셋이 현재 어느 처리 단계에 있는가를 선언한다.
> - **적합성 수준(Level A/B/C):** 이 표준의 절차를 준수하여 해당 산출물을 올바르게 생성했는가를 선언한다.
>
> 이 둘은 같은 축이 아니다. DM-1로 Gate 2를 통과한 데이터셋은 `aird:metadataStatus = "Quality-Ready"`가 되지만(운영 상태는 Quality-Ready), 이 표준 **Level B 적합성은 달성하지 못한다**(DM-2 이상 필요).

### 12.1 적합성 수준

**표 12.1 — 적합성 수준**

| 수준 | 명칭 | 요구사항 |
|---|---|---|
| Level A | 기본 적합성 | Stage 1·Gate 1 절차를 준수하고 Raw Metadata를 산출한다 |
| Level B | 품질 적합성 | Level A + Stage 2·Gate 2 절차를 준수하고 Quality-Ready Metadata와 품질 진단 리포트를 산출한다. **DM-2 이상 필수** |
| Level C | 목적 적합성 | Level B + Stage 3·Gate 3 절차를 준수하고 AIRD Pack을 산출한다 |

**표 12.2 — 3종 표준 적합성 매핑**

| 본 표준 (AIRD-STD-003) | AIRD-STD-001 | AIRD-STD-002 | 달성 운영 상태 |
|---|---|---|---|
| Level A | — | Basic Conformance | Raw |
| Level B | Level A + **DM-2 이상** | Quality Conformance | Quality-Ready |
| Level C | Level B | Purpose Conformance | Purpose-Ready |

### 12.2 적합성 선언

적합성 선언문에는 다음을 포함하여야 한다(SHALL).

- 선언 주체 (기관명·담당자)
- 적합성 수준 (Level A / B / C)
- DM 수준 (Level B 이상 시)
- Q-Tier (Level B 이상, DM-2 이상 시)
- 데이터셋 식별자 (`dct:identifier`)
- 진단 일시 (ISO 8601)
- 진단 도구명 및 버전
- **Pack 정보 (Level C 시 필수):** packGeneratedAt, sourceDataVersion, modelDataCoupling, packCompleteness

**적합성 선언 예시 (Level C, RAG Pack):**

```yaml
Conformance:
  Standard: AIRD-STD-003
  Version: v0.1
  Level: C
  DM: DM-2
  QTier: Silver
  DatasetId: "https://data.go.kr/pid/ds-law-2026"
  DiagnosisDate: "2026-04-14"
  DiagnosisTool: "aird-validator v1.0"
  PackInfo:
    packGeneratedAt: "2026-04-14T09:00:00+09:00"
    sourceDataVersion: "1.2.0"
    modelDataCoupling: "derived"
    packCompleteness: "derived-without-model"
    agentAccessible: true
  PurposeReadiness:
    RAG: Silver
```

---

## 부속서 A (규범적): Gate 판정 절차서

### A.1 Gate 1 판정 절차

```
[입력: Stage 1 출력 아티팩트]
    │
    ▼
① Layer 1 필수 항목 체크 (표 5.1)
    │ 미충족 → FAIL
    ▼
② 오픈 포맷 확인
    │ 비오픈 포맷 → FAIL
    ▼
③ 인코딩 확인 (UTF-8 또는 명시적 선언)
    │ 미확인 → FAIL
    ▼
[PASS] → aird:metadataStatus = "Raw" + 체크포인트 생성
```

### A.2 Gate 2 판정 절차

```
[입력: Stage 2 출력 아티팩트]
    │
    ▼
① [A] 품질 전이 조건 검사 (AIRD-STD-002 7.2절)
    │  QI ≥ 0.50 AND Mandatory Gate 전 차원 충족 AND D3 ≥ 0.65
    │ 미충족 → FAIL (Raw 유지, Stage 2 재실행)
    ▼
② [C] 편향성·한계·결측치 SHALL 기록 확인 (6.3.7절)
    │ 누락 → FAIL
    ▼
③ [B] Layer 2 SHALL 항목 완비 확인 (표 6.2)
    │ SHALL 항목 누락 → FAIL
    ▼
④ [B] Layer 2 SHOULD 항목 확인 (표 6.2)
    │ 전체 충족 → PASS 후보
    │ 일부 미충족 → CONDITIONAL 후보
    ▼
⑤ DM 수준 확인
    │ DM-2/3 → PASS / CONDITIONAL 확정
    │ DM-1 → PASS(DM-1) / CONDITIONAL(DM-1) 확정
    │         → 공시 차단 플래그 설정 (SHALL)
    ▼
[PASS] → aird:metadataStatus = "Quality-Ready"
         Gate Record verdict = "PASS"
         체크포인트 생성

[CONDITIONAL] → aird:metadataStatus = "Quality-Ready"
                Gate Record verdict = "CONDITIONAL"
                conditionalItems 목록 + 기한 기록 (SHALL)
                status = "PENDING"
                체크포인트 생성

                  ↓ 기한 경과 후 미보완
              Gate Record status = "SUSPENDED"
              공시·Stage 3 진입 차단

                  ↓ 보완 완료
              Gate Record status = "RESOLVED"
              resolvedAt 기록
              정상 운영 복귀
```

### A.3 Gate 3 판정 절차

```
[입력: Stage 3 출력 아티팩트]
    │
    ▼
① Layer 3 필수 항목 확인 (해당 Extension Profile 기준)
    │ 누락 → FAIL
    ▼
② AIRD Pack 구조 확인 (7.4절)
    │ 필수 파일 누락 → FAIL
    ▼
③ 무결성 검증 (SHA-256 대조)
    │ 불일치 → FAIL
    ▼
④ purposeReadinessVector 기록 확인
    │ 미기록 → FAIL
    ▼
⑤ DM 표기 일관성 확인
    │ 불일치 → FAIL
    ▼
[PASS] → aird:metadataStatus = "Purpose-Ready"
```

---

## 부속서 B (규범적): Provenance JSON-LD 예시

> **이 부속서는 규범적(normative)이다.** AIRD-STD-002 4.3절이 이 부속서를 규범적 참조로 지정한다.

### B.1 Stage 1 Provenance (PreprocessingActivity)

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "aird": "http://data.go.kr/ns/aird#",
    "xsd":  "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "aird:activity/preprocessing-20260414-001",
  "@type": ["prov:Activity", "aird:PreprocessingActivity"],
  "prov:startedAtTime": { "@value": "2026-04-14T09:00:00+09:00", "@type": "xsd:dateTime" },
  "prov:endedAtTime":   { "@value": "2026-04-14T09:30:00+09:00", "@type": "xsd:dateTime" },
  "prov:wasAssociatedWith": { "@id": "aird:agent/ingest-pipeline-v1.0" },
  "prov:used":      { "@id": "aird:entity/factory-data-source-xlsx" },
  "prov:generated": {
    "@id": "aird:entity/factory-data-raw-v1.0.0.csv",
    "@type": "prov:Entity",
    "prov:wasGeneratedBy": { "@id": "aird:activity/preprocessing-20260414-001" },
    "prov:wasDerivedFrom": { "@id": "aird:entity/factory-data-source-xlsx" }
  },
  "aird:parameters": {
    "targetFormat": "CSV",
    "encoding": "UTF-8",
    "toolName": "aird-ingest",
    "toolVersion": "1.0.0"
  }
}
```

### B.2 Stage 2 Provenance (PreprocessingActivity)

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "aird": "http://data.go.kr/ns/aird#",
    "xsd":  "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "aird:activity/quality-eval-20260414-001",
  "@type": ["prov:Activity", "aird:PreprocessingActivity"],
  "prov:startedAtTime": { "@value": "2026-04-14T10:00:00+09:00", "@type": "xsd:dateTime" },
  "prov:endedAtTime":   { "@value": "2026-04-14T11:00:00+09:00", "@type": "xsd:dateTime" },
  "prov:wasAssociatedWith": { "@id": "aird:agent/quality-eval-tool-v1.0" },
  "prov:used": { "@id": "aird:entity/factory-data-raw-v1.0.0.csv" },
  "prov:wasInformedBy": { "@id": "aird:activity/preprocessing-20260414-001" },
  "prov:generated": {
    "@id": "aird:entity/factory-data-quality-ready-v1.0.0.csv",
    "@type": "prov:Entity",
    "prov:wasGeneratedBy": { "@id": "aird:activity/quality-eval-20260414-001" },
    "prov:wasDerivedFrom": { "@id": "aird:entity/factory-data-raw-v1.0.0.csv" }
  },
  "aird:parameters": {
    "stdVersion": "AIRD-STD-001-v0.1",
    "qiFormula": "QI = Σ(Wi × Di)",
    "officialWeights": {
      "D1": 0.20, "D2": 0.15, "D3": 0.25,
      "D4": 0.10, "D5": 0.15, "D6": 0.15
    },
    "diagnosticMaturity": "DM-2",
    "qualityIndex": 0.87,
    "qualityTier": "Gold",
    "toolName": "aird-quality-eval",
    "toolVersion": "1.0.0"
  }
}
```

### B.3 Stage 3 Provenance (TransformationActivity)

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "aird": "http://data.go.kr/ns/aird#",
    "xsd":  "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "aird:activity/transform-ml-20260414-001",
  "@type": ["prov:Activity", "aird:TransformationActivity"],
  "prov:startedAtTime": { "@value": "2026-04-14T14:00:00+09:00", "@type": "xsd:dateTime" },
  "prov:endedAtTime":   { "@value": "2026-04-14T14:30:00+09:00", "@type": "xsd:dateTime" },
  "prov:wasAssociatedWith": { "@id": "aird:agent/ml-packaging-pipeline-v1.0" },
  "prov:used": { "@id": "aird:entity/factory-data-quality-ready-v1.0.0.csv" },
  "prov:generated": {
    "@id": "aird:entity/factory-data-ml-pack-v1.0.0",
    "@type": "prov:Entity",
    "prov:wasGeneratedBy": { "@id": "aird:activity/transform-ml-20260414-001" },
    "prov:wasDerivedFrom": { "@id": "aird:entity/factory-data-quality-ready-v1.0.0.csv" }
  },
  "aird:parameters": {
    "purposeType": "ML",
    "extensionProfile": "aird-ml-v1.0.0",
    "splitRatio": {"train": 0.70, "validation": 0.15, "test": 0.15},
    "splitMethod": "stratified",
    "randomSeed": 42,
    "toolName": "aird-ml-packager",
    "toolVersion": "1.0.0"
  }
}
```

---

## 부속서 C (참고): Purpose-Type별 파이프라인 예시

> 공장현황 데이터셋(STRUCT 유형, 125만 건)을 공통 예시 데이터로 사용한다. C.5는 Gate 2 CONDITIONAL 시나리오를 별도로 다룬다.

### C.1 ML Pack 변환 예시

**데이터셋:** 전국 산업단지 공장 현황 CSV (125만 건, DM-2 달성)

| 단계 | 처리 내용 | 산출물 |
|---|---|---|
| Stage 1 | XLSX → CSV 변환, UTF-8 정규화, Layer 1 메타데이터 21항목 생성 | `factory-data-raw-v1.0.0.csv` |
| Gate 1 | Layer 1 필수 항목 완비, 오픈 포맷·인코딩 확인 | **PASS** → `aird:metadataStatus = "Raw"` |
| Stage 2 | 6개 차원 측정(STRUCT 14개 필수 지표), QI=0.87(가중합산), Q-Tier=Gold(Tier 3), DM-2, 편향성 기록, Layer 2 생성 | 품질 진단 리포트, Layer 2 메타데이터 |
| Gate 2 | [A] QI=0.87≥0.50 ✅ / Mandatory Gate 전 차원 충족 ✅ / D3≥0.65 ✅ · [B] Layer 2 완비 ✅ · [C] 편향성·한계·결측치 기록 ✅ | **PASS** → `aird:metadataStatus = "Quality-Ready"` |
| Stage 3 | Train(70%)/Valid(15%)/Test(15%) stratified 분할(seed=42), 라벨 필드 지정, 피처 12개 정의, Croissant 1.0 메타데이터 생성, AIRD Pack 조립, SHA-256 체크섬 산출 | `factory-data-ml-pack-v1.0.0/` |
| Gate 3 | Layer 3 필수 항목 완비 ✅ / manifest.json SHA-256 일치 ✅ / `purposeReadinessVector.ML = "Gold"` ✅ / DM 표기 일관성 ✅ | **PASS** → `aird:metadataStatus = "Purpose-Ready"` |

**AIRD Pack 구조:**
```
factory-data-ml-pack-v1.0.0/
├── metadata.json          # Croissant 1.0 Layer 3 메타데이터
├── manifest.json          # 파일 목록·SHA-256·버전
├── provenance.jsonld      # Stage 1~3 Provenance 전체
├── data/
│   ├── train.csv          # 875,000건 (70%)
│   ├── valid.csv          # 187,500건 (15%)
│   └── test.csv           # 187,500건 (15%)
└── quality-report.json    # Stage 2 품질 진단 리포트 사본
```

---

### C.2 RAG Pack 변환 예시

**데이터셋:** 행정 규정·지침 텍스트 코퍼스 (TEXT 유형, 42,000건)

| 단계 | 처리 내용 | 산출물 |
|---|---|---|
| Stage 1 | HWP → TXT 변환, UTF-8 정규화, Layer 1 메타데이터 생성 | `admin-text-raw-v1.0.0/` |
| Gate 1 | Layer 1 필수 항목 완비, 오픈 포맷·인코딩 확인 | **PASS** → Raw 선언 |
| Stage 2 | TEXT 유형 8개 필수 지표 측정, QI=0.76, Q-Tier=Silver(Tier 2), DM-2, Layer 2 생성 | 품질 진단 리포트, Layer 2 메타데이터 |
| Gate 2 | [A] QI=0.76≥0.50 ✅ · [B] Layer 2 완비 ✅ · [C] 편향성 기록 ✅ | **PASS** → Quality-Ready 전이 |
| Stage 3 | Semantic 청킹(512 tokens, overlap 64), `bge-m3` 임베딩 모델 적용(dim=1024), FAISS 인덱스 구축, 원본 문서 보존, `aird-rag:` Candidate 메타데이터 생성 | `admin-text-rag-pack-v1.0.0/` |
| Gate 3 | Layer 3 필수 항목 완비 ✅ / SHA-256 일치 ✅ / `purposeReadinessVector.RAG = "Silver"` ✅ | **PASS** → Purpose-Ready 전이 |

**AIRD Pack 구조:**
```
admin-text-rag-pack-v1.0.0/
├── metadata.json          # aird-rag: Candidate 메타데이터
├── manifest.json
├── provenance.jsonld
├── data/
│   ├── chunks.jsonl       # 청킹 결과 (JSON Lines)
│   ├── vectors.bin        # 임베딩 벡터 (FAISS 포맷)
│   ├── index.faiss        # 벡터 인덱스
│   └── original/          # 원본 문서 보존 디렉터리
└── quality-report.json
```

---

### C.3 KG Pack 변환 예시

**데이터셋:** 공장현황 데이터 (STRUCT → KG 변환, 125만 건)

| 단계 | 처리 내용 | 산출물 |
|---|---|---|
| Stage 1~2 | C.1과 동일 (QI=0.87, Gold, DM-2) | Quality-Ready 파일 + Metadata |
| Stage 3 — 엔티티 추출 | 공장·지역·업종·인허가 엔티티 추출 및 정규화 | 엔티티 목록 (JSON Lines) |
| Stage 3 — 관계 추출 | "공장 socat 업종", "공장 locatedIn 지역" 등 관계 패턴 추출 | 트리플 목록 |
| Stage 3 — RDF 변환 | N-Quads 포맷으로 RDF 트리플 생성 | `factory-kg.nq` |
| Stage 3 — 메타데이터 | VoID + DCAT 메타데이터 생성, SHACL shapes 포함, AIRD Pack 조립 | `factory-data-kg-pack-v1.0.0/` |
| Gate 3 | Layer 3 필수 항목(VoID 핵심 속성) ✅ / SHA-256 일치 ✅ / `purposeReadinessVector.KG = "Gold"` ✅ / 핵심 클래스 `@ko` 레이블 존재 ✅ | **PASS** → Purpose-Ready 전이 |

---

### C.4 Stats Pack 변환 예시

**데이터셋:** 공장현황 통계 집계 데이터 (STRUCT, 다차원 큐브 구조)

> **표준 선택 판단:** 지역×업종×연도 3차원 큐브 구조이므로 SDMX 적용. 판단 기준은 AIRD-STD-002 5.6절 참조.

| 단계 | 처리 내용 | 산출물 |
|---|---|---|
| Stage 1~2 | 집계 소스 CSV 수집, UTF-8 정규화, QI=0.91(Gold, DM-2) | Quality-Ready 파일 + Metadata |
| Stage 3 | 지역·업종·연도 3차원 코드리스트 매핑, 측정값 정의 및 집계 규칙 적용, SDMX DSD 생성, AIRD Pack 조립 | `factory-data-stats-pack-v1.0.0/` |
| Gate 3 | Layer 3 필수 항목(SDMX DSD) ✅ / SHA-256 ✅ / `purposeReadinessVector.Stats = "Gold"` ✅ | **PASS** → Purpose-Ready 전이 |

---

### C.5 Gate 2 CONDITIONAL 시나리오 예시

**상황:** 품질 조건과 SHALL 항목은 충족하나 SHOULD 항목(`csvw:tableSchema`) 미기록

| 검사 | 결과 | 판정 근거 |
|---|---|---|
| [A] QI=0.72≥0.50 | 충족 | 전이 조건 충족 |
| [A] Mandatory Gate 전 차원 충족 | 충족 | D1=0.88, D2=0.75, D3=0.71, D4=0.62, D5=0.80, D6=0.82 |
| [B] Layer 2 SHALL 항목 전체 | 충족 | 완비 |
| [B] `csvw:tableSchema` (SHOULD) | 미충족 | SHOULD 항목 미기록 |
| [C] 편향성·한계·결측치 기록 | 충족 | 완비 |

**판정:** Gate 2 **CONDITIONAL**

**처리 흐름:**
1. `aird:metadataStatus = "Quality-Ready"` 전이 허용
2. Gate Record `status = "PENDING"`, 보완 기한 30일 기록
3. Stage 3 진입 허용 (Gate 3에서 재검사)
4. 기한 내 미보완 시 → Gate Record `status = "SUSPENDED"`, 공시 차단
5. 보완 완료 시 → Gate Record `status = "RESOLVED"`, 정상 운영 복귀

---

## 부속서 D (참고): Extension Profile 등록 템플릿

### D.1 빈 양식

```yaml
# Extension Profile 등록 신청서
# AIRD-STD-003 11장에 따른 등록 템플릿

profile_name: ""
profile_id: "aird-{type}"
version: "0.1.0"
proposer:
  name: ""
  organization: ""
  contact: ""
submission_date: ""

# 1. 목적 정의
purpose:
  description: ""
  use_cases:
    - ""

# 2. 정량 요건
quantitative_requirements:
  min_qtier: null                  # 최소 Q-Tier (Bronze/Silver/Gold/Platinum)
  min_dm: "DM-2"
  min_records: null
  required_dimensions: []          # 반드시 1개 이상 포함 (SHALL)
  additional_requirements: ""

# 3. 변환 규칙
transformation_rules:
  - step: 1
    action: ""
    input: ""
    output: ""

# 4. Layer 3 메타데이터 스키마
metadata_schema:
  namespace_uri: "http://data.go.kr/ns/aird-{type}#"
  base_standard: ""
  properties:
    - name: ""
      uri: ""
      range: ""
      cardinality: ""
      description: ""

# 5. 검증 방법
validation:
  - check: ""
    method: ""
    pass_criteria: ""
```

### D.2 작성 예시 — RAG Pack Extension Profile

```yaml
profile_name: "RAG Pack Extension Profile"
profile_id: "aird-rag"
version: "0.9.0"
proposer:
  name: "홍길동"
  organization: "OO기관 데이터혁신팀"
  contact: "hong@example.go.kr"
submission_date: "2026-04-14"
namespace_status: "Candidate"

purpose:
  description: >
    검색증강생성(RAG) 파이프라인에서 직접 사용할 수 있도록
    공공데이터를 청킹·임베딩·인덱싱하여 제공하는 Purpose-Type.
  use_cases:
    - "공공 문서 기반 질의응답(QA) 시스템 구축"
    - "행정 규정·지침 RAG 서비스"
    - "민원 처리 보조 AI 검색 엔진"

quantitative_requirements:
  min_qtier: "Bronze"
  min_dm: "DM-2"
  required_dimensions:
    - "D1(완전성) >= 0.70"
    - "D3(정확성) >= 0.70"

transformation_rules:
  - step: 1
    action: "청킹 전략 선택 및 적용"
    input: "Quality-Ready 텍스트 파일"
    output: "청크 파일 (JSON Lines, data/chunks.jsonl)"
  - step: 2
    action: "임베딩 모델 적용 및 벡터 생성"
    input: "청크 파일"
    output: "벡터 파일 (data/vectors.bin)"
  - step: 3
    action: "벡터 인덱스 구축"
    input: "벡터 파일"
    output: "인덱스 파일 (data/index.faiss 또는 동등 포맷)"
  - step: 4
    action: "원본 문서 보존"
    input: "Quality-Ready 텍스트 파일"
    output: "data/original/ 디렉터리"
    note: "원본 보존은 필수(SHALL)."

metadata_schema:
  namespace_uri: "http://data.go.kr/ns/aird-rag#"
  base_standard: "Croissant 1.0 (확장)"
  properties:
    - name: "chunkStrategy"
      uri: "aird-rag:chunkStrategy"
      range: "xsd:string"
      cardinality: "1"
      description: "적용된 청킹 전략"
    - name: "embeddingModel"
      uri: "aird-rag:embeddingModel"
      range: "xsd:string"
      cardinality: "1"
      description: "임베딩 모델 명칭 및 버전"
    - name: "vectorDimension"
      uri: "aird-rag:vectorDimension"
      range: "xsd:integer"
      cardinality: "1"
      description: "임베딩 벡터 차원 수"

validation:
  - check: "청크 커버리지"
    method: "전체 청크를 재조합하여 원본 텍스트 복원률 측정"
    pass_criteria: "원본 텍스트의 95% 이상이 청크에 포함"
  - check: "벡터 차원 일관성"
    method: "모든 벡터 파일의 차원 수 확인"
    pass_criteria: "aird-rag:vectorDimension 선언값과 100% 일치"
  - check: "원본 문서 보존"
    method: "data/original/ 디렉터리 존재 및 파일 수 확인"
    pass_criteria: "Quality-Ready 파일 수와 동일"
```

---

## 부속서 E (참고): 표준 간 참조 매트릭스

> **본 부속서는 참고(informative)이다.** 표준 시리즈를 함께 적용하는 실무 작업자가 조항 간 연결 관계를 빠르게 확인하기 위한 참조 자료이다.

### E.1 AIRD-STD-003 → AIRD-STD-001 참조

| 본 표준 절 | AIRD-STD-001 참조 절 | 참조 내용 |
|---|---|---|
| 6.3.2 | 5.1절 (PRECONDITION_UNMET 규칙) | 전제 조건 확인 및 3회 상한 규칙 |
| 6.3.3 | 5장·8장 (측정 공식·유형별 기준) | 6개 차원 측정 기준 및 유형별 적용 지표 |
| 6.3.4 | 6.2절 (QI = Σ(Wi × Di)) | 가중합산 QI 산정. 가중치 기본값 표 6.1 |
| 6.3.4 | 6.3절 (D3 Case A/B) | D3 전체 미측정 시 QI 산정 분기 |
| 6.3.5 | 7장 (Q-Tier 판정 알고리즘) | Q-Tier 5단계 판정 및 Mandatory Gate 강등 |
| 6.3.6 | 4.4절·8.2절 (DM 정의·기준) | DM 수준 산정. DM-2 기준 유형별 필수 지표 수 |
| 6.3.9 | 9장 (리포트 스키마) | 품질 진단 리포트 전체 스키마 |
| 6.3.9 | 9.4절 (`preconditionGuideRef`, `preconditionCount`) | PRECONDITION_UNMET 추적 필드 |
| 4.4 | 4.4절 (DM 체계 도식) | Q-Tier × DM 이원 축 도식 |
| 10.1 | 10.3절 (운영 규칙 핵심 3개) | 진단 의무 시점·책임 주체·OPG 위임 |

### E.2 AIRD-STD-003 → AIRD-STD-002 참조

| 본 표준 절 | AIRD-STD-002 참조 절 | 참조 내용 |
|---|---|---|
| 3.5 (상태 전이) | 2.1절 (통합 상태 모델) | 상태 전이 규칙 단일 출처. Raw 품질 점수 금지 |
| 3.5 | 2.3절 (상태별 메타데이터 포함/제외 규칙) | 역방향 전이 후 품질 점수 삭제 규칙 |
| 5.3 (표 5.1) | 3장 (Layer 1 Discovery) | Layer 1 필수 항목 21개 스키마 |
| 5.5 (Gate 1) | 3장 | Gate 1 검사 기준 — Layer 1 스키마 준수 |
| 6.3.7 | 4.2.4절 (신뢰·윤리 메타데이터) | `rai:dataBiases`, `rai:knownLimitations`, `rai:dataCollectionMissingData` |
| 6.3.8 (표 6.2) | 4장 (Layer 2 Understanding) | Layer 2 필수·권장 항목 전체 스키마 |
| **6.5 (Gate 2)** | **7.2절 (Quality-Ready 전이 조건 단일 출처)** | **전이 조건 수치의 유일한 원천. 충돌 시 7.2절 우선** |
| 7.3 (표 7.1) | 5장 (Layer 3 Operability) | Purpose-Type별 기반 표준 및 Extension Profile |
| 7.4 (AIRD Pack) | 2.2절 (3계층 아키텍처) | Layer 1+2+3 통합 패키지 개념 |
| 8장 (Provenance) | **4.3절 (Activity 타입 구분 규칙)** | `aird:PreprocessingActivity` / `aird:TransformationActivity` 구분. 부속서 B가 규범적 참조 |
| 10.1(c) | 2.3절 | DM-1 공시 차단 플래그 운영 근거 |
| 11장 | 8.3절 (Extension Profile 거버넌스) | 거버넌스 절차 연계. 11.4절 생애주기와 일치 |

### E.3 AIRD-STD-002 → AIRD-STD-003 역방향 참조

| AIRD-STD-002 절 | 본 표준 참조 절 | 참조 내용 |
|---|---|---|
| 2.1절 (상태 모델) | 4.3절 (상태 전이 규칙) | 파이프라인에서 상태 전이가 일어나는 시점과 조건 |
| 4.3절 (Provenance Activity 타입) | **부속서 B (규범적)** | PreprocessingActivity / TransformationActivity JSON-LD 전체 예시 |
| 4.4절 (purposeReadinessVector) | 7.5(d)절 | Stage 3에서 purposeReadinessVector를 갱신하는 절차 |
| 5장 (Layer 3 각 Profile) | 7.3절 (표 7.1) | 각 Purpose-Type 변환 시 기반 표준 및 Extension Profile 연계 |
| 7.2절 (Quality-Ready 전이 조건) | 6.5절 (Gate 2) | 이 표준에서 7.2절 조건을 파이프라인 판정에 적용하는 절차 |
| 8.3절 (Extension Profile 거버넌스) | 11장 | Extension Profile 등록·심의·네임스페이스 관리 전체 절차 |
| 부록 B.3 (ML Pack JSON-LD) | 부속서 C.1 | ML Pack 변환 시나리오와 Layer 3 메타데이터 연계 예시 |

### E.4 실무 빠른 참조 — 역할별 필수 확인 조항

**파이프라인 개발자 (자동화 구현):**

| 구현 목표 | 확인 조항 |
|---|---|
| Gate 판정 로직 구현 | 부속서 A (규범적) |
| QI 계산 | 6.3.4절 + AIRD-STD-001 6.2절 |
| Q-Tier 판정 | 6.3.5절 + AIRD-STD-001 7장 |
| Provenance 자동 기록 | 8장 + 부속서 B (규범적) |
| AIRD Pack 조립 | 7.4절 |
| DM-1 공시 차단 플래그 | 10.1(c)절 |

**데이터 담당자 (실무 운영):**

| 운영 상황 | 확인 조항 |
|---|---|
| 데이터 최초 등록 시 | 5장 (Stage 1) + 표 5.1 체크리스트 |
| 품질 진단 수행 시 | 6장 (Stage 2) + 표 6.2 체크리스트 |
| Gate 2 FAIL 대응 | 6.5.3절 + AIRD-STD-001 부속서 F |
| PRECONDITION_UNMET 반복 발생 | 6.3.2절 누적 횟수 규칙 |
| 역방향 전이 (재진단) | 3.5(b)절 |

**정책·기획 담당자:**

| 정책 질문 | 확인 조항 |
|---|---|
| 공식 공시 가능 조건 | 4.4절 (DM-2 이상) + 10.1(c)절 |
| 책임 주체 | 10.1(b)절 |
| 새 Purpose-Type 추가 절차 | 11장 전체 |
| 표준 적합성 선언 방법 | 12장 전체 |

---

## 부속서 F (참고): Value-level 이상 탐지 규칙 로드맵

> **본 부속서는 참고(informative)이다.** 진단 계층 확장의 도입 로드맵과 Column-level 준비 초안을 제시한다.

### F.1 진단 계층별 도입 계획

| 계층 | 진단 대상 | AIRD-STD-002 위치 | 본 표준 도입 시기 |
|---|---|---|---|
| Dataset-level | QI (현행) | 4.2.1~4.2.2절 (필수) | 현행 (v0.1) |
| Column-level | 컬럼별 품질 분포 | `aird:columnQualityBreakdown` (MAY) | v0.2: `IndicatorResult.details` 스키마 규범적 확정 |
| Value-level | 위장 결측·분포 이상·단위 혼재 탐지 | 본 표준 부속서 F 소관 | v1.1: 탐지 규칙 정의 |
| Concept-level | 컬럼-표준개념 URI 매핑 | `csvw:tableSchema propertyUrl` (SHOULD) | v0.2: AIRD-STD-002와 정합성 확인 후 규범적 정의 |

### F.2 Column-level 준비 초안

> 아래 내용은 **초안**이다. AIRD-STD-002 `aird:columnQualityBreakdown`과의 스키마 정합성 검토 후 v0.2에서 규범적으로 확정한다.

#### F.2.1 `IndicatorResult.details` 스키마 초안

AIRD-STD-001 9.4절의 `IndicatorResult.details` 필드에 Column-level 결과를 기록할 때 다음 구조를 사용한다.

```json
{
  "indicatorId": "D1-01",
  "applicability": "APPLIED",
  "score": 0.94,
  "details": {
    "columnBreakdown": [
      { "column": "종업원수",   "columnId": "csvw:column:종업원수",   "nullRate": 0.06, "score": 0.94, "isCore": true },
      { "column": "사업자번호", "columnId": "csvw:column:사업자번호", "nullRate": 0.00, "score": 1.00, "isCore": true },
      { "column": "업종코드",   "columnId": "csvw:column:업종코드",   "nullRate": 0.12, "score": 0.88, "isCore": false }
    ],
    "coreColumnNullRate": 0.030,
    "concentrationAlert": false,
    "missingPattern": "MCAR"
  }
}
```

#### F.2.2 Value-level 이상 탐지 예비 목록 (v1.1 목표)

| 이상 유형 | 탐지 방법 | 해당 차원 |
|---|---|---|
| 위장 결측 (disguised missing) | "없음", "N/A", "0", "-" 등 의미적 결측 패턴 탐지 | D1 완전성 |
| 분포 이상 (distribution shift) | IQR 기반 이상치 탐지 + Kolmogorov-Smirnov 검정 | D5 유효성 |
| 단위 혼재 (unit inconsistency) | 동일 컬럼 내 단위 불일치 패턴 (예: km/m 혼재) | D2 일관성 |
| 스케일 이상 (scale anomaly) | 예상 범위 대비 극단값 (D5-03 보조) | D5 유효성 |

*— 끝 —*
