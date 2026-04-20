# AI-Ready Data 품질 진단 프레임워크
## Quality-Ready Data Preparation Framework

| 항목 | 내용 |
|---|---|
| 문서 번호 | AIRD-STD-001 |
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
| **AIRD-STD-001** | **Quality-Ready Data Preparation Framework (본 표준)** | 품질 측정·판정·등급 체계 — 원칙·공식 |
| AIRD-STD-002 | AI-Ready Data Metadata Profile | 메타데이터 항목·레이어·스키마 — 기술·기록 |
| AIRD-STD-003 | AI-Ready Data Transformation & Governance Specification | ETL 파이프라인·AIRD Pack·거버넌스 — 실행·운영 |
| AIRD-STD-005 | AI-Ready Data Discovery & Exchange Specification | Pack 탐색 API·에이전트 인터페이스 — 교환 |
| AIRD-OPG-001 | 품질 진단 운영 지침 *(예정)* | 진단 주기·유효기간·이의제기·도구 인증 — 운영 세부 |
| AIRD-TR-001 | 가중치 설계 기술 보고서 *(예정)* | Purpose-Type별 가중치 수치 근거 |

> **설계 원칙**
>
> 이 표준은 네 가지 원칙 위에 설계되었다.
>
> 첫째, **AI 목적 명시:** 이 표준은 데이터 품질 표준이 아니라 AI 처리 파이프라인 투입 가능성 표준이다. Quality-Ready 판정은 "데이터가 깨끗한가"가 아니라 "AI 파이프라인이 이 데이터를 받아들일 수 있는가"를 묻는다.
>
> 둘째, **QI는 보조, Gate가 판정 주체:** QI가 높아도 Gate를 통과하지 못하면 Q-Tier는 강등된다.
>
> 셋째, **DM과 Q-Tier는 독립 축:** Q-Tier는 품질 수준, DM은 측정 신뢰 수준이다.
>
> 넷째, **경계 명확성:** 이 표준은 측정·판정만을 규율한다. Pack 운영·상태 관리·목적별 준비도 판정은 AI-Ready Data Transformation & Governance Specification(AIRD-STD-003)이 규율한다.

---

## 머리말

이 표준은 AI-Ready Data를 6개 품질 차원으로 정량적으로 측정·판정·등급화할 수 있도록 구체적인 공식, 임계치, 판정 로직을 규정한다. 세 가지 원칙을 달성하기 위해 제정한다.

1. **측정 가능성(Measurability):** 서술적 기준을 0.0–1.0 범위의 정량 공식으로 전환하여 기관 간 비교 가능한 단일 척도를 확보한다.
2. **판정 가능성(Decidability):** Quality-Ready 여부를 기계적으로 판정할 수 있는 임계치와 등급 체계를 규정한다.
3. **재현 가능성(Reproducibility):** 진단 결과를 JSON 리포트로 표준화하여 자동화 파이프라인과 연계한다.

---

## 목차

1. 적용 범위
2. 인용 표준
3. 용어 및 정의
4. 품질 프레임워크 개요
5. 품질 차원별 세부 지표 및 측정 공식
6. 점수 정규화 및 품질 지수 산정
7. 품질 등급(Q-Tier) 체계 및 판정 규칙
8. 데이터 유형별 진단 기준 차별화
9. 품질 진단 리포트 스키마
10. 적합성 및 운영 규칙
11. 표준 간 연계 구조

**부속서**
- 부속서 A (규범적): 품질 지표별 측정 공식 및 전제 조건 요약표
- 부속서 B (규범적): 품질 등급 매트릭스
- 부속서 C (규범적): 품질 진단 리포트 JSON 스키마
- 부속서 D (참고): 데이터 유형별 진단 시나리오 예시
- 부속서 E (참고): 컬럼 수준 진단 결과 확장 가이드
- 부속서 F (참고): 전제 조건 구축 가이드 및 템플릿

---

## 1. 적용 범위

### 1.1 목적

이 표준은 데이터셋을 Raw 상태에서 Quality-Ready 상태로 전환하는 과정에서 품질을 측정·판정·등급화하는 기준을 규정한다.

### 1.2 적용 범위 외

아래 사항은 이 표준의 범위 밖이다.

| 사항 | 담당 문서 |
|---|---|
| 메타데이터 기록 스키마 | AI-Ready Data Metadata Profile (AIRD-STD-002) |
| Quality-Ready → Purpose-Ready 변환 파이프라인 실행 | AI-Ready Data Transformation & Governance Specification (AIRD-STD-003) |
| Pack 상태 관리(Stale·피드백 루프·Pack 완전성) | AI-Ready Data Transformation & Governance Specification (AIRD-STD-003) |
| purposeReadinessVector 체계 및 Purpose-Type별 준비도 판정 | AI-Ready Data Transformation & Governance Specification (AIRD-STD-003) |
| Pack 탐색 API 및 에이전트 인터페이스 | AI-Ready Data Discovery & Exchange Specification (AIRD-STD-005) |
| 진단 주기·결과 유효기간·이의제기·도구 인증 | AIRD-OPG-001 (예정) |
| Purpose-Type별 가중치 수치 근거 | AIRD-TR-001 (예정) |
| 각 Purpose-Type의 성능 평가 방법론·기준 | 도메인별 기술규격 |
| AI 모델 파일·추론 시스템·서비스 엔드포인트 관리 | 모델 레지스트리 / MLOps 표준 |
| 모델 기반 품질 평가 | 향후 확장 예정 |

> **설계 원칙:** 본 표준은 데이터셋의 AI 활용 준비 상태(Readiness State)를 정의하고 관리하는 **상태 표준(State Standard)**이다. AIRD Pack은 AI 모델 파일을 포함하지 않으며, 모델은 변환 수단으로 간주한다. 소비자 유형(에이전트·A2A·MCP 등)의 변화에 대해 특정 기술 스택을 규범적으로 명시하지 않는다.

---

## 2. 인용 표준

### 2.1 내부 표준

| 표준번호 | 표준명 |
|---|---|
| AIRD-STD-002 | AI-Ready Data Metadata Profile |
| AIRD-STD-003 | AI-Ready Data Transformation & Governance Specification |

### 2.2 외부 표준

| 표준 | 발행 기관 | 적용 내용 |
|---|---|---|
| ISO/IEC 25012:2008 | ISO/IEC | 데이터 품질 모델 |
| W3C DQV | W3C | 데이터 품질 어휘 |
| DCAT v3 | W3C | 데이터 카탈로그 어휘 |
| Croissant 1.0 | MLCommons | ML 데이터셋 메타데이터 |
| ISO 8601:2019 | ISO | 일시 표기 |

---

## 3. 용어 및 정의

**3.1 Quality-Ready (Base) 상태**
Raw 데이터가 6개 품질 차원의 최소 임계치를 모두 통과하여, AI 학습·분석·추론·검색증강생성(RAG) 등 AI 처리 파이프라인에 직접 투입 가능한 품질 수준에 도달한 상태.

> Quality-Ready 판정은 "데이터가 깨끗한가"가 아니라 "AI 파이프라인이 이 데이터를 받아들일 수 있는가"를 묻는다.

**3.2 품질 차원 (Quality Dimension)**
데이터 품질을 평가하는 독립적 관점. 완전성·일관성·정확성·적시성·유효성·유일성 6개 차원.

**3.3 품질 지표 (Quality Indicator)**
각 품질 차원을 구성하는 세부 측정 항목.

**3.4 측정 공식 (Measurement Formula)**
품질 지표 값을 0.0–1.0 범위로 산출하는 정량적 수학 공식.

**3.5 품질 지수 (Quality Index, QI)**
6개 차원 점수를 가중 합산하여 산출하는 데이터셋 수준의 종합 품질 점수 (0.0–1.0).

**3.6 Q-Tier**
QI 및 필수 게이트 조건에 따라 결정되는 품질 등급. Tier 1(Bronze)~Tier 4(Platinum).

**3.7 필수 게이트 (Mandatory Gate)**
QI 점수와 무관하게 반드시 통과해야 하는 차원별 최소 임계치 조건.

**3.8 진단 프로브 (Diagnostic Probe)**
개별 품질 지표에 측정 공식을 적용하여 점수를 산출하는 단위 검사.

**3.9 품질 진단 리포트 (Quality Diagnosis Report)**
모든 진단 프로브 결과를 집계하여 JSON 포맷으로 출력한 표준화된 보고서.

**3.10 데이터 유형 (Data Type Category)**
정형(STRUCT)·텍스트(TEXT)·이미지(IMAGE)·시계열(TSERIES)·파인튜닝(FT) 5개 유형.

**3.11 진단 성숙도 (Diagnostic Maturity, DM)**
기관이 이 표준의 측정 지표를 얼마나 폭넓게 적용하고 있는지를 나타내는 수준 지표. DM-1(기초)·DM-2(표준)·DM-3(완전) 3단계.

**3.12 PRECONDITION_UNMET**
지표 측정의 전제 조건(업무 규칙 정의, 참조 데이터, 전문 인력 등)이 현재 기관에 갖춰지지 않아 측정이 불가능한 상태. N/A(해당 데이터 유형에 적용 불가)와 구분된다.

**3.13 공식 가중치 / 조정 가중치**
공식 가중치(Official Weight)는 기관 간 비교를 위한 고정값이며, 조정 가중치(Adjusted Weight)는 기관이 Purpose-Type에 따라 설정하는 참고값. 공식 Q-Tier 판정은 항상 공식 가중치를 사용한다.

**3.14 컬럼 수준 진단**
개별 컬럼(필드) 단위로 품질 지표를 분해하여 결측·이상·분포를 측정하는 세부 진단. `IndicatorResult.details` 필드에 선택적으로 기록.

---

## 4. 품질 프레임워크 개요

### 4.1 프레임워크 구조

```
┌─────────────────────────────────────────────────────┐
│  Layer 4: Q-Tier 판정 (7장)                          │
│  Q-Tier = f(QI, Mandatory Gates)                    │
│  + 진단 성숙도(DM) 병기                               │
├─────────────────────────────────────────────────────┤
│  Layer 3: 품질 지수 산정 (6장)                        │
│  QI = Σ(Wi × Di)  ※ 측정 가능 차원 기준 산정           │
├─────────────────────────────────────────────────────┤
│  Layer 2: 차원별 점수 집계 (5장)                      │
│  Di = aggregate(측정된 지표 점수)                     │
├─────────────────────────────────────────────────────┤
│  Layer 1: 지표별 측정 (5장)                           │
│  Probe → 전제 조건 확인 → Formula → Score (0.0–1.0)  │
└─────────────────────────────────────────────────────┘
```

> 전제 조건 미충족 시 `PRECONDITION_UNMET`으로 기록하고 집계에서 제외한다.
> Q-Tier는 단일 기준을 유지하되, 측정 범위를 진단 성숙도(DM)로 함께 표기한다.

### 4.2 6개 품질 차원 체계

**표 4.1 — 품질 차원 요약**

| 차원 ID | 차원명 | 영문 | 세부 지표 수 |
|---|---|---|---|
| D1 | 완전성 | Completeness | 4 |
| D2 | 일관성 | Consistency | 4 |
| D3 | 정확성 | Accuracy | 4 |
| D4 | 적시성 | Timeliness | 2 |
| D5 | 유효성 | Validity | 4 |
| D6 | 유일성 | Uniqueness | 2 |
| — | — | 합계 | **20** |

### 4.3 데이터 유형 분류

**표 4.2 — 데이터 유형 분류 체계**

| 유형 코드 | 유형명 | 정의 | 예시 |
|---|---|---|---|
| STRUCT | 정형 데이터 | 행×열의 테이블 구조, 사전 정의 스키마 | CSV, Parquet, RDBMS |
| TEXT | 텍스트 데이터 | 자연어 문장, 비정형/반정형 | 법령 원문, 민원 텍스트 |
| IMAGE | 이미지 데이터 | 픽셀 기반 시각 정보 | 위성사진, 의료 영상 |
| TSERIES | 시계열 데이터 | 시간 인덱스 포함 순서 있는 관측값 | 기상 관측, IoT 센서 |
| FT | Fine-tuning 데이터 | LLM 파인튜닝용 instruction-response 페어, preference 데이터 | 지시문-응답 JSONL, DPO 데이터 |

복수 유형을 포함하는 데이터셋은 유형별 QI를 별도 산출 후 가중 평균한다.

### 4.4 진단 성숙도(DM) 체계

> **핵심 정의**
>
> **Q-Tier = 데이터의 품질 수준**
> **DM = 해당 품질 측정 결과의 신뢰 수준**
>
> 두 지표는 서로 독립적인 축이다. DM이 높다고 Q-Tier가 높아지지 않으며, Q-Tier가 높아도 DM이 낮으면 공식 공시에 사용할 수 없다.

```
             Q-Tier (품질 수준)
                 높음 ↑
                      │              ★ 공식 공시 가능 영역
                      │        (Q-Tier 임의 + DM-2 이상의 교집합)
          Gold ────── │ ─────────────────────────────
                      │              │
        Silver ────── │ ─────────────│───────────────
                      │              │
        Bronze ────── │ ─────────────│───────────────
                      │              │
                 낮음 └──────────────┼──────────────→ DM (측정 신뢰 수준)
                                   DM-1           DM-2       DM-3
                              (내부 참고용)   (공식 공시 가능)  (완전 적합성)
```

진단 성숙도는 Q-Tier와 독립적으로 측정되며, 기관이 표준을 얼마나 폭넓게 적용하고 있는지를 나타낸다. Q-Tier 판정 기준 자체는 DM 수준과 무관하게 단일하게 유지된다.

**표 4.3 — 진단 성숙도 정의**

| DM 수준 | 조건 | Q-Tier 표기 방식 | 의미 |
|---|---|---|---|
| **DM-1** (기초) | 데이터 유형별 필수(●) 지표의 50% 이상 APPLIED | `Q-Tier (DM-1)` | 진단 시작 단계 |
| **DM-2** (표준) | 데이터 유형별 필수(●) 지표 **전체** APPLIED | `Q-Tier` | 정규 Q-Tier — 기관 간 비교 가능 |
| **DM-3** (완전) | 선택(○) 지표 포함 전체 APPLIED | `Q-Tier (DM-3)` | 완전 적합성 |

> - DM-2에서 산출된 Q-Tier만 공식 적합성 선언 및 기관 간 비교에 사용한다(SHALL).
> - DM-1 Q-Tier는 내부 진단 참고용으로만 사용하며, 공식 공시에 사용하여서는 안 된다(SHALL NOT).
> - 기관은 DM-1에서 시작하여 DM-2 달성을 목표로 단계적으로 전진한다. 전환 경로는 부속서 F 참조.

---

## 5. 품질 차원별 세부 지표 및 측정 공식

### 5.1 공통 규칙

1. 모든 측정 공식 출력값은 0.0–1.0 실수로 정규화한다.
2. 측정 대상 모집단이 0건이면 점수는 `null`로 기록하고 집계에서 제외한다.
3. 지표별 `applicability` 값은 다음 4가지 중 하나를 사용한다.

| 값 | 의미 |
|---|---|
| `APPLIED` | 측정 완료 |
| `N/A` | 해당 데이터 유형에 적용 불가 |
| `OPTIONAL_SKIPPED` | 선택 지표 — 이번 진단에서 생략 |
| `PRECONDITION_UNMET` | 전제 조건 미충족으로 측정 불가 |

4. **PRECONDITION_UNMET 선언 규칙**

   다음 3가지 조건을 모두 충족하는 경우에만 선언할 수 있다(SHALL).

   - 미충족 전제 조건 항목이 부속서 A의 전제 조건 체크리스트에 명시되어 있을 것
   - 미충족 사유가 리포트의 `preconditionNote` 필드에 자유 텍스트로 기록될 것
   - `preconditionNote`에 부속서 F의 해당 구축 단계를 참조 기록할 것 (예: "부속서 F 4단계 참조")

   **누적 규칙:**

   | 누적 횟수 | 조치 |
   |---|---|
   | 1회 | 허용. `preconditionNote` 기록 + 부속서 F 단계 참조 의무 |
   | 2회 연속 | 구축 계획서를 소관 전담 기관에 제출 의무(SHALL) |
   | **3회 연속** | **해당 차원의 Q-Tier 게이트 기준을 Tier 1(Bronze) 임계치로 고정. 실제 점수와 무관하게 그 차원은 Tier 1 수준을 상한으로 적용하고, 전체 Q-Tier 강등으로 이어진다(SHALL).** |

   > **3회 상한 제한의 취지:** FAIL 처리(점수 0)와 달리, 3회 제한은 "측정 인프라 부재"와 "데이터 품질 불량"을 구분한 채로 회피에 대한 실질적 압박을 부여한다. 기관이 전제 조건 구축을 미룰수록 Q-Tier 상승이 막히는 구조다.

5. 본문 공식 기호 정의

| 기호 | 정의 |
|---|---|
| N | 전체 레코드(또는 파일) 수 |
| n(조건) | 조건을 만족하는 레코드 수 |
| F_req | 필수(Required) 필드 집합 |

---

### 5.2 D1: 완전성 (Completeness)

**정의:** 필요한 데이터가 누락 없이 존재하는 정도.

#### D1-01: 필수 속성 충족도

| 항목        | 내용                                                   |     |     |
| --------- | ---------------------------------------------------- | --- | --- |
| 지표 ID     | D1-01                                                |     |     |
| 적용 유형     | STRUCT(●), TSERIES(●), TEXT(○), IMAGE(○), FT(●)      |     |     |
| **전제 조건** | 필수 필드 목록(F_req)이 스키마 또는 데이터 사전에 정의되어 있을 것            |     |     |
| 측정 공식     | `D1-01 = (1/F_req) × Σ [ n(f ≠ NULL ∧ f ≠ '') / N ]` |     |     |
| 해석        | 필수 필드 집합 내 각 필드의 유효값 비율의 평균                          |     |     |
| 컬럼수준      | `details.columnBreakdown`에 필드별 결측률 기록 가능(MAY)        |     |     |

#### D1-02: 시나리오 변수 충분성

| 항목 | 내용 |
|---|---|
| 지표 ID | D1-02 |
| 적용 유형 | STRUCT(●), TEXT(●), IMAGE(●), TSERIES(●), FT(●) |
| **전제 조건** | 활용 시나리오 문서 또는 AI-Ready Data Metadata Profile(AIRD-STD-002) Layer 2에 "요구 변수 목록"이 명시적으로 기록되어 있을 것. 미정의 시 `PRECONDITION_UNMET` 처리(SHALL). |
| 측정 공식 | `D1-02 = n(확보된 변수) / n(요구 변수)` |

#### D1-03: 데이터 다양성

| 항목 | 내용 |
|---|---|
| 지표 ID | D1-03 |
| 적용 유형 | STRUCT(●), IMAGE(●), TSERIES(●), TEXT(○), FT(○) |
| **전제 조건** | 없음 (자동 계산 가능) |
| 측정 공식 | `D1-03 = 1 − Gini(속성별 분포)` |
| **해석 주의** | Gini 계수는 불균형 측정 지표로, 자연스러운 불균형을 품질 저하로 오해할 수 있다. 이 지표는 "AI 학습 적합성 보조 지표"로만 해석하며 단독 판정 근거로 사용하지 않는다(SHALL NOT). |

#### D1-04: 라벨 다양성

| 항목 | 내용 |
|---|---|
| 지표 ID | D1-04 |
| 적용 유형 | STRUCT(●), TEXT(●), IMAGE(●), TSERIES(○), FT(●) |
| **전제 조건** | 없음 (자동 계산 가능) |
| 측정 공식 | `D1-04 = 1 − (max − min) / (max + min)` |
| 해석 | 클래스·라벨 분포의 균형도. 1에 가까울수록 균형 잡힌 분포. |

---

### 5.3 D2: 일관성 (Consistency)

**정의:** 동일 의미의 값이 모든 레코드에서 통일된 형식·규칙으로 기록된 정도.

#### D2-01: 관계 일관성

| 항목 | 내용 |
|---|---|
| 지표 ID | D2-01 |
| 적용 유형 | STRUCT(●), TSERIES(●) |
| **전제 조건** | 업무 규칙 목록이 데이터 사전 또는 AI-Ready Data Metadata Profile(AIRD-STD-002) 메타데이터에 기관 내부적으로 승인된 형태로 기록되어 있을 것. 미정의 시 `PRECONDITION_UNMET`. |
| 측정 공식 | `D2-01 = 1 − (n(규칙 위배 레코드) / N)` |
| 해석 | 종료일 ≥ 시작일, 합계 = 구성요소 합 등 사전 정의 업무 규칙 위배 비율. |

#### D2-02: 기준 정보 일관성

| 항목 | 내용 |
|---|---|
| 지표 ID | D2-02 |
| 적용 유형 | STRUCT(●), TSERIES(○) |
| **전제 조건** | 교차 참조 대상 데이터셋이 존재하고 접근 가능할 것. 없으면 N/A. |
| 측정 공식 | `D2-02 = 1 − (n(속성값 불일치 개체) / n(교차 참조 대상 개체))` |

#### D2-03: 참조 무결성

| 항목 | 내용 |
|---|---|
| 지표 ID | D2-03 |
| 적용 유형 | STRUCT(●), TSERIES(●) |
| **전제 조건** | 마스터 코드 테이블이 접근 가능할 것. 공개 코드는 전제 조건 충족으로 간주. |
| 측정 공식 | `D2-03 = 1 − (n(미매핑 코드 레코드) / N)` |
| 해석 | 1.0 = 모든 참조값이 유효한 마스터 코드에 매핑됨. |

#### D2-04: 인코딩 일관성

| 항목 | 내용 |
|---|---|
| 지표 ID | D2-04 |
| 적용 유형 | STRUCT(●), TEXT(●), TSERIES(●), IMAGE(○), FT(●) |
| **전제 조건** | 없음 (자동 계산 가능) |
| 측정 공식 | `D2-04 = n(기준 인코딩 준수 파일) / n(전체 파일)` |
| 해석 | 기준 인코딩(UTF-8)을 준수하는 파일 비율. |

---

### 5.4 D3: 정확성 (Accuracy)

**정의:** 데이터 값이 참조 기준과 일치하는 정도.

> D3 지표는 참조 기준이 존재하는 경우에만 적용한다(SHALL). 아래 표는 지표별 측정 가능성과 전제 조건을 명시한다. D3 전체 산정 규칙은 6.3절 참조.

**표 5.1 — D3 지표별 측정 가능성 분류**

| 지표 | 전제 조건 | 자동화 난이도 | 비고 |
|---|---|---|---|
| D3-01 기준 정합성 | 외부 참조 DB | 높음 | 참조 DB 구축 후 적용 |
| D3-02 규칙 정확성 | 스키마·계산 규칙 | 낮음 | 대부분 기관 즉시 적용 가능 |
| D3-03 라벨 정확성 | 전문 검수 인력 | 매우 높음 | Full 진단(DM-3) 목표 |
| D3-04 출처 신뢰성 | 메타데이터 | 중간 | 소관 적합율 항목은 수동 판단 필요 |

#### D3-01: 기준 정합성

| 항목 | 내용 |
|---|---|
| 지표 ID | D3-01 |
| 적용 유형 | STRUCT(●), TEXT(○), TSERIES(○) |
| **전제 조건** | 법령·고시·표준코드 등 공인 참조 테이블이 존재하고 접근 가능할 것. 미충족 시 `PRECONDITION_UNMET`. |
| 측정 공식 | `D3-01 = 1 − (n(기준 불일치 레코드) / n(기준 대조 대상))` |

#### D3-02: 규칙 정확성

| 항목 | 내용 |
|---|---|
| 지표 ID | D3-02 |
| 적용 유형 | STRUCT(●), TSERIES(●) |
| **전제 조건** | 계산 가능한 파생 값(합계·평균·비율 등)이 스키마에 정의되어 있을 것. 없으면 N/A. |
| 측정 공식 | `D3-02 = 1 − (n(산출 ≠ 저장) / n(검증 대상))` |

#### D3-03: 라벨 정확성

| 항목 | 내용 |
|---|---|
| 지표 ID | D3-03 |
| 적용 유형 | IMAGE(●), TEXT(○), FT(●) |
| **전제 조건** | 전문가 검수가 완료된 정답 라벨 집합이 존재할 것. 미충족 시 `PRECONDITION_UNMET`. |
| 측정 공식 | `D3-03 = n(일치) / n(검수 대상)` |
| 해석 | 이미지의 경우 IoU ≥ 0.5 기준 적용. |

#### D3-04: 출처 신뢰성

| 항목 | 내용 |
|---|---|
| 지표 ID | D3-04 |
| 적용 유형 | STRUCT(○), TEXT(●), IMAGE(○), TSERIES(○), FT(○) |
| **전제 조건** | 메타데이터에 출처 정보가 기록되어 있을 것. 없으면 `PRECONDITION_UNMET`. |
| 측정 공식 | `D3-04 = 0.4 × 출처기재율 + 0.3 × 소관적합율 + 0.3 × 링크유효율` |
| 해석 | 소관 적합율은 수동 판단 항목이므로, 미판단 시 해당 가중치를 출처기재율에 합산 가능(MAY). |

---

### 5.5 D4: 적시성 (Timeliness)

**정의:** 데이터가 현재 시점 기준으로 충분히 최신 상태인 정도.

#### D4-01: 최신성

| 항목 | 내용 |
|---|---|
| 지표 ID | D4-01 |
| 적용 유형 | STRUCT(●), TEXT(●), IMAGE(○), TSERIES(●), FT(●) |
| **전제 조건** | 메타데이터에 갱신일과 갱신 주기가 기록되어 있을 것. 없으면 `PRECONDITION_UNMET`. |
| 측정 공식 | `D4-01 = max(0, 1 − 경과일수 / 허용경과일수)` |
| 해석 | 허용경과일수 = 갱신 주기 × 1.5 (기본값). |

#### D4-02: 데이터 연속성

| 항목 | 내용 |
|---|---|
| 지표 ID | D4-02 |
| 적용 유형 | TSERIES(●), STRUCT(○) |
| **전제 조건** | 메타데이터에 갱신 주기가 명시되어 있을 것. |
| 측정 공식 | `D4-02 = n(실제 시점) / n(기대 시점)` |
| 해석 | 법정 공휴일 등 사전 공지된 비수집 기간은 제외 가능(MAY). 제외 시 사유를 리포트에 기록(SHALL). |

---

### 5.6 D5: 유효성 (Validity)

**정의:** 데이터 값이 정의된 형식·범위·규칙을 준수하는 정도.

#### D5-01: 형식 유효성

| 항목 | 내용 |
|---|---|
| 지표 ID | D5-01 |
| 적용 유형 | STRUCT(●), TEXT(●), TSERIES(●), FT(●) |
| **전제 조건** | 없음. 단, 정규식 패턴이 미정의된 컬럼은 해당 컬럼을 제외하고 측정. |
| 측정 공식 | `D5-01 = 1 − (n(형식 불일치) / N)` |

#### D5-02: 기술적 유효성

| 항목 | 내용 |
|---|---|
| 지표 ID | D5-02 |
| 적용 유형 | IMAGE(●), TEXT(○) |
| **전제 조건** | 없음 (자동 계산 가능) |
| 측정 공식 | `D5-02 = n(정상 ∧ 사양 충족) / n(전체 파일)` |

#### D5-03: 수치 범위 유효성

| 항목 | 내용 |
|---|---|
| 지표 ID | D5-03 |
| 적용 유형 | STRUCT(●), TSERIES(●) |
| **전제 조건** | 컬럼별 허용 범위가 스키마 또는 데이터 사전에 정의되어 있을 것. 미정의 컬럼은 제외하고 측정. 정의된 컬럼이 하나도 없으면 `PRECONDITION_UNMET`. |
| 측정 공식 | `D5-03 = 1 − (n(범위 초과 레코드) / N)` |

#### D5-04: 통계적 타당성

| 항목 | 내용 |
|---|---|
| 지표 ID | D5-04 |
| 적용 유형 | STRUCT(○), TSERIES(●) |
| **전제 조건** | 없음. IQR 방식 자동 적용. |
| 측정 공식 | `D5-04 = 1 − (n(이상치 레코드) / N)` |
| 해석 | IQR 방식: Q1−1.5×IQR 미만 또는 Q3+1.5×IQR 초과. 더미값(999999, 0000 등) 패턴도 포함. |

---

### 5.7 D6: 유일성 (Uniqueness)

**정의:** 동일한 개체가 중복 없이 한 번만 표현된 정도.

#### D6-01: 데이터 유일성

| 항목 | 내용 |
|---|---|
| 지표 ID | D6-01 |
| 적용 유형 | STRUCT(●), TEXT(○), TSERIES(●), FT(●) |
| **전제 조건** | 없음. 고유 식별자 미정의 시 전체 컬럼 조합을 키로 사용. |
| 측정 공식 | `D6-01 = n(유니크 레코드) / N` |

#### D6-02: 유사 중복 제어

| 항목 | 내용 |
|---|---|
| 지표 ID | D6-02 |
| 적용 유형 | TEXT(●), IMAGE(●), FT(●) |
| **전제 조건** | 없음. 단, 데이터 규모에 따라 아래 계산 방식 선택 필요. |
| 측정 공식 (텍스트·FT) | `D6-02 = 1 − (n(코사인 유사도 ≥ 0.85인 페어) / n(전체 페어))` |
| 측정 공식 (이미지) | `D6-02 = 1 − (n(pHash 해밍 거리 ≤ 10%인 페어) / n(전체 페어))` |

> **대용량 처리 규칙:** O(N²) 계산 회피를 위해 아래 방식 중 하나를 선택한다.
>
> - 10만 건 이하: 전체 페어 계산 가능
> - 10만 건 초과: **무작위 샘플링(기본값)**. 샘플 비율 10% 이상 권장(SHOULD)
> - LSH(Locality-Sensitive Hashing) 기반 근사 계산: 권장(SHOULD). 전체 계산을 대체 가능
>
> 적용 방식과 샘플 비율을 리포트 `samplingMethod` 필드에 기록하여야 한다(SHALL).

---

## 6. 점수 정규화 및 품질 지수 산정

### 6.1 차원별 점수 집계

```
Di = Σ_k (w_k × S_k) / Σ_k w_k
```

- `S_k` = 지표 k의 점수 (APPLIED인 것만 포함)
- `w_k` = 지표 k의 가중치 (기본: 균등 배분)
- APPLIED가 아닌 지표(N/A, OPTIONAL_SKIPPED, PRECONDITION_UNMET)는 분자·분모 모두에서 제외

차원 내 APPLIED 지표가 하나도 없으면 해당 차원 점수는 `null`로 처리한다.

### 6.2 품질 지수(QI) 산정

```
QI = Σ_{i=1}^{6} (W_i × D_i)   단, D_i ≠ null인 차원만 포함
```

**표 6.1 — 차원별 공식 가중치 (고정값)**

| 차원 | W_i (공식 기본값) | 조정 허용 범위 |
|---|---|---|
| D1: 완전성 | 0.20 | 0.10 – 0.30 |
| D2: 일관성 | 0.15 | 0.10 – 0.25 |
| D3: 정확성 | 0.25 | 0.15 – 0.35 |
| D4: 적시성 | 0.10 | 0.05 – 0.20 |
| D5: 유효성 | 0.15 | 0.10 – 0.25 |
| D6: 유일성 | 0.15 | 0.10 – 0.25 |
| 합계 | 1.00 | — |

> D3(정확성)의 가중치(0.25)가 가장 높은 이유는 AI 파이프라인에서 사실과 부합하지 않는 데이터의 학습이 모델 신뢰성에 직접적으로 영향을 미치기 때문이다.

### 6.3 D3 측정 불가 시 QI 산정 특례

D3는 전제 조건이 요구되는 지표 비중이 높아 별도 처리 규칙을 적용한다.

**Case A: D3 지표 중 1개 이상 APPLIED**

```
D3 차원 점수 = 측정된 지표만으로 산출
QI 산정 시 D3 가중치 0.25 유지
리포트에 "D3 부분 측정 (n/4 지표)" 표기 (SHALL)
```

**Case B: D3 지표 전체가 PRECONDITION_UNMET**

```
D3 차원 점수 = null
나머지 5개 차원 가중치를 Σ=1.0이 되도록 비례 재배분
  재배분 공식: W_i' = W_i / (1 − W_D3)
  재배분 예시: D1=0.267, D2=0.200, D4=0.133, D5=0.200, D6=0.200
Quality-Ready 판정 시 D3 게이트 자동 면제
Q-Tier 표기: Q-Tier (DM-1, D3 미측정)
리포트에 "D3 전체 미측정, 가중치 재배분" 명시 (SHALL)
```

> Case B가 2회 연속 발생하면 5.1절 4항에 따라 D3 구축 계획서 제출 의무 발생.

### 6.4 가중치 조정 규칙

**(1) 공식 가중치(Official Weight):** 표 6.1 기본값. 기관 간 비교 및 공식 Q-Tier 판정에 사용. 변경 불가(SHALL NOT).

**(2) 조정 가중치(Adjusted Weight):** 기관이 Purpose-Type에 따라 설정 가능(MAY). 표 6.1 허용 범위를 초과하지 않아야 한다(SHALL NOT).

**(3) Purpose-Type별 가중치 조정 방향 (권장)**

**표 6.2 — Purpose-Type별 가중치 조정 방향**

| Purpose-Type | 상향 조정 권장 차원 | 하향 조정 권장 차원 | 조정 근거 |
|---|---|---|---|
| ML/DL | D1(완전성), D5(유효성) | D4(적시성) | 결측·형식 오류가 모델 성능에 직접 영향 |
| RAG | D3(정확성), D1(완전성) | D6(유일성) | 검색 정확도가 응답 품질 결정 |
| 통계 분석 | D1(완전성), D2(일관성) | D4(적시성) | 집계 왜곡 방지 우선 |
| 실시간 운영 | D4(적시성), D2(일관성) | D6(유일성) | 최신성·일관성이 운영 안정성 핵심 |
| Fine-tuning | D1(완전성), D6(유일성) | D4(적시성) | 데이터 다양성·중복 제거가 일반화 성능 결정 |

> 조정 가중치 적용 결과는 `adjustedQI` 필드에 별도 기록하며, 공식 Q-Tier 판정은 항상 공식 가중치 기반 `qi`를 사용한다(SHALL).

**(4) 조정 기록 의무:** 조정 사유, 전후 값, 적용 프리셋 코드(해당 시)를 `weightAdjustment` 필드에 기록한다(SHALL).

---

## 7. 품질 등급(Q-Tier) 체계 및 판정 규칙

> **판정 원칙**
>
> **QI는 품질 수준을 나타내는 보조 지표이며, 최종 Quality-Ready 판정은 Mandatory Gate 조건에 의해 결정된다.**
> QI가 높더라도 하나 이상의 게이트를 통과하지 못하면 Q-Tier는 강등된다.
>
> 이 원칙은 두 가지 왜곡을 방지한다.
> 첫째, 특정 차원 점수를 집중적으로 올려 QI를 높이는 "점수 최적화" 행위.
> 둘째, 약한 차원이 강한 차원의 점수에 희석되어 실제 AI 사용 불가 데이터가 합격되는 "평균의 함정".
>
> **Q-Tier 판정 흐름:** QI → 후보 Tier 결정 → Mandatory Gate 검사 → 강등 또는 확정 → Quality-Ready 판정

### 7.1 등급 체계

**표 7.1 — Q-Tier 등급 정의**

| Q-Tier | 등급명 | QI 범위 | AI 활용 가능 수준 |
|---|---|---|---|
| Tier 4 | Platinum | QI ≥ 0.95 | 즉시 투입 가능. 최고 품질. |
| Tier 3 | Gold | 0.85 ≤ QI < 0.95 | 대부분의 AI 시나리오에 적합. |
| Tier 2 | Silver | 0.70 ≤ QI < 0.85 | 일부 전처리 후 AI 활용 가능. |
| Tier 1 | Bronze | 0.50 ≤ QI < 0.70 | 최소 기준 충족. 상당한 정제 필요. |
| Tier 0 | Unqualified | QI < 0.50 | Quality-Ready 기준 미달. |

### 7.2 필수 게이트 조건

QI 점수가 등급 범위에 해당하더라도 차원별 필수 게이트를 통과하지 못하면 통과 가능한 최고 Tier로 강등된다(부속서 B 참조).

### 7.3 Quality-Ready 판정 기준

다음 조건을 모두 충족하여야 Quality-Ready 판정을 받는다(SHALL).

1. 최종 Tier ≥ 1 (Bronze 이상)
2. 모든 측정된 차원이 Tier 1 게이트 조건 충족
3. D3(정확성) ≥ 0.65 **— 단, D3 Case B(전체 미측정) 시 자동 면제**

### 7.4 판정 알고리즘

```python
def determine_q_tier(QI, dimension_scores, d3_case):
    # Step 1: QI 기반 후보 Tier
    if QI >= 0.95:   candidate = 4
    elif QI >= 0.85: candidate = 3
    elif QI >= 0.70: candidate = 2
    elif QI >= 0.50: candidate = 1
    else:            return {"tier": 0, "qualityReady": False}

    # Step 2: 필수 게이트 확인 → 강등
    for tier in range(candidate, 0, -1):
        if all_gates_pass(dimension_scores, tier):
            final_tier = tier
            break
    else:
        return {"tier": 0, "qualityReady": False}

    # Step 3: Quality-Ready 판정
    d3_ok = (d3_case == "B") or (dimension_scores.get("D3", 0) >= 0.65)
    quality_ready = (final_tier >= 1) and d3_ok

    return {"tier": final_tier, "qualityReady": quality_ready}
```

### 7.5 Q-Tier 표기 방식 (DM 병기)

| 상황 | 표기 예시 |
|---|---|
| DM-2 정규 판정 | `Gold (Tier 3)` |
| DM-1 기초 판정 | `Gold (Tier 3, DM-1)` |
| D3 전체 미측정 | `Silver (Tier 2, DM-1, D3 미측정)` |
| DM-3 완전 판정 | `Gold (Tier 3, DM-3)` |

> DM-2 이상에서 산출된 Q-Tier만 공식 적합성 선언 및 공시에 사용 가능(SHALL).

### 7.6 판정 보조 정보

리포트에 다음 보조 정보를 포함하여야 한다(SHALL).

- **강등 사유:** 게이트 미통과 차원 및 실제 점수
- **개선 권고:** Tier 상승을 위한 핵심 개선 차원 (Gap 최대 차원)
- **이력 비교:** 직전 진단 대비 변화량 (최초 진단 시 null)
- **미측정 지표 목록:** PRECONDITION_UNMET 지표 ID 및 사유 요약

---

## 8. 데이터 유형별 진단 기준 차별화

### 8.1 유형별 적용 지표 매트릭스

**표 8.1 — 데이터 유형별 지표 적용표** (`●` 필수, `○` 선택, `—` 해당 없음)

| 지표 ID | 지표명         | STRUCT | TEXT | IMAGE | TSERIES | FT  |
| ----- | ----------- | ------ | ---- | ----- | ------- | --- |
| D1-01 | 필수 속성 충족도   | ●      | ○    | ○     | ●       | ●   |
| D1-02 | 시나리오 변수 충분성 | ●      | ●    | ●     | ●       | ●   |
| D1-03 | 데이터 다양성     | ●      | ○    | ●     | ●       | ○   |
| D1-04 | 라벨 다양성      | ●      | ●    | ●     | ○       | ●   |
| D2-01 | 관계 일관성      | ●      | —    | —     | ●       | —   |
| D2-02 | 기준 정보 일관성   | ●      | —    | —     | ○       | —   |
| D2-03 | 참조 무결성      | ●      | —    | —     | ●       | —   |
| D2-04 | 인코딩 일관성     | ●      | ●    | ○     | ●       | ●   |
| D3-01 | 기준 정합성      | ●      | ○    | —     | ○       | —   |
| D3-02 | 규칙 정확성      | ●      | —    | —     | ●       | —   |
| D3-03 | 라벨 정확성      | —      | ○    | ●     | —       | ●   |
| D3-04 | 출처 신뢰성      | ○      | ●    | ○     | ○       | ○   |
| D4-01 | 최신성         | ●      | ●    | ○     | ●       | ●   |
| D4-02 | 데이터 연속성     | ○      | —    | —     | ●       | —   |
| D5-01 | 형식 유효성      | ●      | ●    | —     | ●       | ●   |
| D5-02 | 기술적 유효성     | —      | ○    | ●     | —       | —   |
| D5-03 | 수치 범위 유효성   | ●      | —    | —     | ●       | —   |
| D5-04 | 통계적 타당성     | ○      | —    | —     | ●       | —   |
| D6-01 | 데이터 유일성     | ●      | ○    | —     | ●       | ●   |
| D6-02 | 유사 중복 제어    | —      | ●    | ●     | —       | ●   |

### 8.2 유형별 DM-2 달성을 위한 최소 측정 지표 수

**표 8.2 — 유형별 지표 수 및 DM-2 기준**

| 데이터 유형 | 전체 적용 가능 | 필수(●) | DM-2 기준 (●전체 APPLIED) |
|---|---|---|---|
| STRUCT | 17 | 14 | 14개 이상 |
| TEXT | 12 | 8 | 8개 이상 |
| IMAGE | 9 | 7 | 7개 이상 |
| TSERIES | 15 | 12 | 12개 이상 |
| FT | 11 | 9 | 9개 이상 |

> PRECONDITION_UNMET로 처리된 필수 지표는 DM-2 달성에서 제외되며 DM-1로 처리된다.
> 단, 해당 지표의 첫 번째 PRECONDITION_UNMET 선언인 경우에는 경고(Warning)로 처리하고 DM-2를 허용할 수 있다(MAY).

### 8.3 유형별 특화 기준

**STRUCT:** 스키마 정합성(DDL 대비 타입·Nullable 일치)을 D5-01의 보조 검사로 수행. 결측 패턴 분석(MCAR/MNAR)을 D1-01 보조 검사로 수행하고 체계적 결측 발견 시 경고 플래그 기록.

**TEXT:** 다음 보조 검사를 해당 지표 측정 시 함께 수행하여야 한다(SHALL).

1. **언어 일관성 (D2-04 보조):** 선언된 언어(예: `ko`, `en`)와 실제 텍스트 언어가 일치하는 비율을 측정한다. 언어 불일치 비율이 5%를 초과하면 경고 플래그를 리포트에 기록한다.
2. **토큰화 가능성 (D5-01 보조):** 표준 토크나이저(KoNLPy, SentencePiece 등)로 토큰화 실패율을 D5-01 측정값에 포함한다. `tokenFailRate = n(토큰화 실패 문서) / n(전체 문서)`.
3. **문장 완결성 (D5-01 보조):** 절삭(truncation) 또는 인코딩 오류로 인한 불완전 문장이 10% 초과 시 경고.
4. **유사 중복 임계치 (D6-02 적용):** 기본 코사인 유사도 임계치 0.85. 법령·규정·판례 등 구조적 유사성이 본질적으로 높은 도메인은 0.95로 상향 조정 가능(MAY). 조정 시 사유를 리포트에 기록(SHALL).

**IMAGE:** 다음 보조 검사를 해당 지표 측정 시 함께 수행하여야 한다(SHALL).

1. **최소 해상도 (D5-02 적용):** AI 태스크별 최소 해상도 기준을 적용한다.
   - 객체 탐지: 640×480 이상
   - 이미지 분류: 224×224 이상
   - OCR: 300 DPI 이상
   - 의료 영상: 512×512 이상 (권장)
2. **어노테이션 일관성 (D3-03 보조):** 동일 클래스 내 바운딩 박스 면적의 표준편차가 평균의 50%를 초과하면 어노테이션 일관성 경고를 기록한다. IoU ≥ 0.5 기준으로 라벨-이미지 정합성 판정.
3. **클래스 불균형 (D1-04 보조):** 전체 어노테이션 대비 최소 클래스의 비율이 5% 미만인 경우 극단적 불균형으로 판정하고 `classImbalanceAlert` 플래그를 기록한다. 불균형 자체가 Q-Tier를 강등시키지는 않으며 AI 활용자에 대한 정보 제공 목적이다.
4. **유사 중복 탐지 (D6-02 적용):** pHash(퍼셉추얼 해싱) 기반 해밍 거리 ≤ 10%를 중복 판정 기준으로 적용.

**TSERIES:** 타임스탬프 단조 증가(monotonically increasing) 여부를 D2-01 보조 검사로 수행. 갭 허용 정책 적용 시 비수집 기간 근거 기록 의무(SHALL).

**FT (Fine-tuning 데이터):** 다음 보조 검사를 해당 지표 측정 시 함께 수행하여야 한다(SHALL).

1. **페어 구조 검증 (D1-01 보조):** 모든 레코드가 `instruction`과 `response` 필드를 포함하는지 검사한다. `preference` 데이터의 경우 `chosen`과 `rejected` 필드가 존재하는지 확인한다.
2. **응답 길이 분포 (D1-04 보조):** 응답 길이(토큰 수)의 IQR 방식 분포를 측정한다. 응답 길이의 표준편차가 평균의 200%를 초과하면 경고 플래그를 기록한다.
3. **언어 일관성 (D2-04 보조):** 선언된 언어와 instruction·response 필드의 실제 언어가 일치하는 비율을 측정한다. 불일치 비율 5% 초과 시 경고.
4. **지시문-응답 정합성 (D3-03 보조):** 샘플링(전체의 5% 이상)을 통해 instruction의 의도와 response의 내용이 논리적으로 부합하는지 검수한다. 전문가 검수 또는 자동화 평가 도구를 사용할 수 있다(MAY).
5. **유사 중복 임계치 (D6-02 적용):** instruction 필드에 대해 코사인 유사도 0.90을 중복 판정 임계치로 적용한다. 일반 텍스트(0.85)보다 엄격한 기준을 적용하는 이유는 파인튜닝 데이터의 다양성 확보가 모델 일반화 성능에 직접 영향하기 때문이다.

---

## 9. 품질 진단 리포트 스키마

### 9.1 리포트 개요

품질 진단 결과는 JSON 포맷으로 출력하여야 한다(SHALL).

### 9.2 최상위 구조

**표 9.1 — 리포트 최상위 필드**

| 필드명 | 타입 | 필수 | 설명 |
|---|---|---|---|
| reportId | string | 필수 | UUID v4 |
| reportVersion | string | 필수 | 스키마 버전 (예: "1.0") |
| generatedAt | string (ISO 8601) | 필수 | 리포트 생성 일시 |
| datasetId | string | 필수 | 데이터셋 식별자 |
| datasetVersion | string | 필수 | 데이터셋 버전 |
| dataType | string | 필수 | STRUCT \| TEXT \| IMAGE \| TSERIES \| FT \| MIXED |
| recordCount | integer | 필수 | 전체 레코드 수 |
| diagnosticMaturity | string | 필수 | "DM-1" \| "DM-2" \| "DM-3" |
| dimensions | array[DimensionResult] | 필수 | 차원별 진단 결과 |
| qualityIndex | QualityIndexResult | 필수 | QI 산정 결과 |
| qTier | QTierResult | 필수 | 등급 판정 결과 |
| weightAdjustment | WeightAdjustment \| null | 선택 | 가중치 조정 내역 |
| metadata | object | 선택 | 진단 도구명, 버전 등 |

### 9.3 DimensionResult 구조

| 필드명 | 타입 | 필수 | 설명 |
|---|---|---|---|
| dimensionId | string | 필수 | D1–D6 |
| dimensionName | string | 필수 | 차원명 |
| score | number \| null | 필수 | 차원 점수 (0.0–1.0). 측정 불가 시 null |
| weight | number | 필수 | 적용된 공식 가중치 |
| effectiveWeight | number | 필수 | QI 산정에 실제 사용된 가중치 (재배분 후) |
| adjustedWeight | number \| null | 선택 | 조정 가중치 |
| indicators | array[IndicatorResult] | 필수 | 지표별 결과 |

### 9.4 IndicatorResult 구조

| 필드명 | 타입 | 필수 | 설명 |
|---|---|---|---|
| indicatorId | string | 필수 | 예: "D1-01" |
| indicatorName | string | 필수 | 지표명 |
| applicability | string | 필수 | APPLIED \| N/A \| OPTIONAL_SKIPPED \| PRECONDITION_UNMET |
| score | number \| null | 필수 | 지표 점수. 비APPLIED 시 null |
| weight | number | 필수 | 차원 내 가중치 |
| preconditionNote | string \| null | 조건부 필수 | PRECONDITION_UNMET 시 사유 기술 |
| preconditionGuideRef | string \| null | 조건부 필수 | PRECONDITION_UNMET 시 부속서 F 구축 단계 참조 (예: "부속서 F 4단계: 업무 규칙 정의") |
| preconditionCount | integer \| null | 조건부 필수 | 동일 지표의 누적 PRECONDITION_UNMET 선언 횟수 |
| samplingMethod | string \| null | 선택 | FULL \| RANDOM \| LSH \| TOP_K |
| samplingRatio | number \| null | 선택 | 샘플링 비율 |
| errorCount | integer \| null | 선택 | 오류 건수 |
| errorRate | number \| null | 선택 | 오류율 |
| details | object \| null | 선택 | 컬럼 수준 세부 결과 (부속서 E) |

### 9.5 QualityIndexResult 구조

| 필드명 | 타입 | 필수 | 설명 |
|---|---|---|---|
| qi | number | 필수 | 공식 가중치 기반 QI |
| adjustedQI | number \| null | 선택 | 조정 가중치 기반 QI |
| d3Case | string | 필수 | "A" (부분 측정) \| "B" (전체 미측정) \| "FULL" (전체 측정) |
| formula | string | 필수 | "QI = Σ(Wi × Di)" |
| dimensionWeights | object | 필수 | 공식 차원별 가중치 |
| effectiveWeights | object | 필수 | 실제 적용 가중치 (재배분 후) |
| dimensionScores | object | 필수 | 차원별 점수 |

### 9.6 QTierResult 구조

| 필드명 | 타입 | 필수 | 설명 |
|---|---|---|---|
| tier | integer | 필수 | 0–4 |
| tierName | string | 필수 | Unqualified \| Bronze \| Silver \| Gold \| Platinum |
| tierLabel | string | 필수 | DM 포함 표기 (예: "Gold (Tier 3, DM-1)") |
| qualityReady | boolean | 필수 | Quality-Ready 판정 |
| diagnosticMaturity | string | 필수 | DM-1 \| DM-2 \| DM-3 |
| candidateTier | integer | 필수 | QI 기반 후보 Tier |
| downgradeReason | string \| null | 필수 | 강등 사유 |
| d3Exempt | boolean | 필수 | D3 게이트 면제 여부 |
| gateResults | object | 필수 | 차원별 게이트 통과 결과 |
| unmeasuredIndicators | array[string] | 필수 | PRECONDITION_UNMET 지표 ID 목록 |
| improvementSuggestion | string \| null | 필수 | 개선 권고 |
| previousTier | integer \| null | 필수 | 직전 Tier (최초 시 null) |
| previousQI | number \| null | 필수 | 직전 QI |

### 9.7 리포트 예시

```json
{
  "reportId": "550e8400-e29b-41d4-a716-446655440000",
  "reportVersion": "1.0",
  "generatedAt": "2026-04-14T10:00:00Z",
  "datasetId": "ds-factory-2026",
  "datasetVersion": "1.2.0",
  "dataType": "STRUCT",
  "recordCount": 1250000,
  "diagnosticMaturity": "DM-2",
  "dimensions": [
    {
      "dimensionId": "D1",
      "dimensionName": "완전성",
      "score": 0.92,
      "weight": 0.20,
      "effectiveWeight": 0.20,
      "adjustedWeight": null,
      "indicators": [
        {
          "indicatorId": "D1-01",
          "indicatorName": "필수 속성 충족도",
          "applicability": "APPLIED",
          "score": 0.96,
          "weight": 0.25,
          "preconditionNote": null,
          "samplingMethod": "FULL",
          "samplingRatio": 1.0,
          "errorCount": 50000,
          "errorRate": 0.04,
          "details": {
            "columnBreakdown": [
              {"column": "종업원수", "nullRate": 0.04, "isCore": true},
              {"column": "사업자번호", "nullRate": 0.00, "isCore": true}
            ],
            "coreColumnNullRate": 0.010
          }
        },
        {
          "indicatorId": "D1-02",
          "indicatorName": "시나리오 변수 충분성",
          "applicability": "PRECONDITION_UNMET",
          "score": null,
          "weight": 0.25,
          "preconditionNote": "활용 시나리오 문서 미작성. 다음 진단 주기(2026-10)까지 작성 예정.",
          "preconditionGuideRef": "부속서 F 5단계: 활용 시나리오 문서 작성",
          "preconditionCount": 1
        }
      ]
    }
  ],
  "qualityIndex": {
    "qi": 0.88,
    "adjustedQI": null,
    "d3Case": "A",
    "formula": "QI = Σ(Wi × Di)",
    "dimensionWeights": {
      "D1": 0.20, "D2": 0.15, "D3": 0.25,
      "D4": 0.10, "D5": 0.15, "D6": 0.15
    },
    "effectiveWeights": {
      "D1": 0.20, "D2": 0.15, "D3": 0.25,
      "D4": 0.10, "D5": 0.15, "D6": 0.15
    },
    "dimensionScores": {
      "D1": 0.92, "D2": 0.85, "D3": 0.91,
      "D4": 0.78, "D5": 0.89, "D6": 0.88
    }
  },
  "qTier": {
    "tier": 3,
    "tierName": "Gold",
    "tierLabel": "Gold (Tier 3)",
    "qualityReady": true,
    "diagnosticMaturity": "DM-2",
    "candidateTier": 3,
    "downgradeReason": null,
    "d3Exempt": false,
    "gateResults": {
      "D1": {"required": 0.85, "actual": 0.92, "pass": true},
      "D2": {"required": 0.80, "actual": 0.85, "pass": true},
      "D3": {"required": 0.90, "actual": 0.91, "pass": true},
      "D4": {"required": 0.75, "actual": 0.78, "pass": true},
      "D5": {"required": 0.85, "actual": 0.89, "pass": true},
      "D6": {"required": 0.85, "actual": 0.88, "pass": true}
    },
    "unmeasuredIndicators": ["D1-02"],
    "improvementSuggestion": "D4(적시성) 개선 시 Platinum 도달 가능 (Gap: 0.07). D1-02 시나리오 변수 충분성 전제 조건 구축 권장.",
    "previousTier": 2,
    "previousQI": 0.81
  },
  "weightAdjustment": null
}
```

---

## 10. 적합성 및 운영 규칙

### 10.1 적합성 수준

**표 10.1 — 적합성 수준**

| 수준 | 명칭 | 조건 | Q-Tier 공식 인정 |
|---|---|---|---|
| Level A | 기초 적합성 | 데이터 유형별 필수(●) 지표 50% 이상 APPLIED (DM-1) | 공시 불가, 내부 참고용 |
| Level B | 표준 적합성 | 데이터 유형별 필수(●) 지표 전체 APPLIED (DM-2) | **공식 Q-Tier 인정** |
| Level C | 완전 적합성 | 선택(○) 포함 전체 지표 APPLIED (DM-3) | 공식 Q-Tier + 완전 적합성 마크 |

> PRECONDITION_UNMET로 처리된 지표는 APPLIED로 계산하지 않는다.
> 단, 해당 지표의 첫 번째 PRECONDITION_UNMET 선언인 경우 Level B 달성 허용(MAY).

### 10.2 적합성 선언

이 표준을 준수하는 시스템 또는 프로세스는 적합성 수준을 명시하여야 한다(SHALL).

적합성 선언문 포함 항목: 선언 주체, 적합성 수준(Level A/B/C), DM 수준, Q-Tier (DM-2 이상 시), 데이터셋 식별자, 진단 일시.

### 10.3 운영 규칙 (핵심 3개)

다음 3개 규칙은 이 표준에서 직접 규율한다. 그 외 세부 운영 사항은 AIRD-OPG-001에 위임한다.

**(a) 진단 의무 시점 (SHALL)**

데이터셋 최초 등록 시 및 데이터 내용 변경 시 품질 진단을 수행하여야 한다.

**(b) 책임 주체 (SHALL)**

품질 진단 실행의 1차 책임은 데이터 보유 기관에 있다. 결과 검증의 책임은 소관 전담 기관이 정하는 바에 따른다.

**(c) OPG 위임 (SHALL)**

진단 주기의 세부 기준, 결과 유효기간, 이의제기 절차, 도구 인증 기준은 AIRD-OPG-001(품질 진단 운영 지침)에서 정한다. 전담 기관은 OPG를 2년 주기로 검토하여야 한다.

---

## 11. 표준 간 연계 구조

### 11.1 역할 분리 원칙

| 표준 | 핵심 질문 | 역할 |
|---|---|---|
| **Quality-Ready Data Preparation Framework (본 표준)** | 무엇을 측정하고 어떻게 판정하는가? | 측정·판정 원칙·공식 |
| AI-Ready Data Metadata Profile | 측정 결과를 어떻게 기록하고 표현하는가? | 메타데이터 기술 스키마 |
| AI-Ready Data Transformation & Governance Specification | 어떻게 자동화하여 운영하고 Purpose-Ready로 전환하는가? | 실행 파이프라인·Pack 운영 |
| AI-Ready Data Discovery & Exchange Specification | Pack을 어떻게 탐색하고 교환하는가? | 탐색 API·교환 규격 |
| OPG-001 | 언제, 누가, 어떻게 운영하는가? | 운영 세부 지침 (예정) |

### 11.2 Quality-Ready Data Preparation Framework → AI-Ready Data Metadata Profile 연계

| 본 표준 절 | 연계 대상 (AI-Ready Data Metadata Profile) | 연계 내용 |
|---|---|---|
| 5장 전체 | Layer 2 (Understanding) | 지표 점수를 DQV 어휘로 기록 |
| 7장 | Layer 1 (Discovery) | Q-Tier + DM 수준을 Discovery 메타데이터에 기록 |
| 9장 details 필드 | Layer 2 `cr:Field` | 컬럼 수준 결과를 컬럼 메타데이터와 연결 |

### 11.3 Quality-Ready Data Preparation Framework → AI-Ready Data Transformation & Governance Specification 연계

| 본 표준 절 | 연계 대상 (AI-Ready Data Transformation & Governance Specification) | 연계 내용 |
|---|---|---|
| 9장 | Stage 2 출력 아티팩트 | 본 표준의 JSON 리포트를 Stage 2 산출물로 사용 |
| 7장 | Gate 2 판정 | Q-Tier 판정으로 Quality-Ready 전이 통제 |
| 6.4 | Stage 2 재진단 | 변환 후 재진단 시 가중치 조정 근거 연계 |

### 11.4 Quality-Ready Data Preparation Framework → AI-Ready Data Discovery & Exchange Specification 연계

| 본 표준 절 | 연계 대상 (AI-Ready Data Discovery & Exchange Specification) | 연계 내용 |
|---|---|---|
| 7장 | Discovery API 필터 | Q-Tier 기반 Pack 탐색 조건 제공 |
| 7장 | staleness 판단 | Q-Tier를 탐색 응답에 포함 (Stale 상태 관리는 AI-Ready Data Transformation & Governance Specification(AIRD-STD-003) 소관) |

---

## 부속서 A (규범적): 품질 지표별 측정 공식 및 전제 조건 요약표

**표 A.1 — 전체 지표 요약**

| 지표 ID | 지표명 | 측정 공식 | 전제 조건 | 자동화 난이도 |
|---|---|---|---|---|
| D1-01 | 필수 속성 충족도 | `(1/\\|F_req\\|) × Σ[n(f≠NULL ∧ f≠'')/N]` | 필수 필드 목록 정의 | 낮음 |
| D1-02 | 시나리오 변수 충분성 | `n(확보변수) / n(요구변수)` | 요구 변수 목록 명시 | 중간 |
| D1-03 | 데이터 다양성 | `1 − Gini(속성별 분포)` | 없음 | 낮음 |
| D1-04 | 라벨 다양성 | `1 − (max−min)/(max+min)` | 없음 | 낮음 |
| D2-01 | 관계 일관성 | `1 − n(규칙위배)/N` | 업무 규칙 정의서 | 중간 |
| D2-02 | 기준 정보 일관성 | `1 − n(불일치개체)/n(대조개체)` | 교차 참조 데이터셋 | 높음 |
| D2-03 | 참조 무결성 | `1 − n(미매핑)/N` | 마스터 코드 테이블 | 낮음 |
| D2-04 | 인코딩 일관성 | `n(준수파일)/n(전체파일)` | 없음 | 낮음 |
| D3-01 | 기준 정합성 | `1 − n(불일치)/n(대조대상)` | 공인 참조 테이블 | 높음 |
| D3-02 | 규칙 정확성 | `1 − n(산출≠저장)/n(검증대상)` | 계산 규칙 스키마 정의 | 중간 |
| D3-03 | 라벨 정확성 | `n(일치)/n(검수대상)` | 전문가 검수 완료 | 매우 높음 |
| D3-04 | 출처 신뢰성 | `0.4×출처기재율+0.3×소관적합율+0.3×링크유효율` | 메타데이터 출처 기록 | 중간 |
| D4-01 | 최신성 | `max(0, 1−경과일수/허용경과일수)` | 갱신일·갱신주기 메타데이터 | 낮음 |
| D4-02 | 데이터 연속성 | `n(실제시점)/n(기대시점)` | 갱신 주기 메타데이터 | 낮음 |
| D5-01 | 형식 유효성 | `1 − n(형식불일치)/N` | 없음 (정규식 미정의 컬럼 제외) | 낮음 |
| D5-02 | 기술적 유효성 | `n(정상∧사양충족)/n(전체파일)` | 없음 | 낮음 |
| D5-03 | 수치 범위 유효성 | `1 − n(범위초과)/N` | 컬럼별 허용 범위 정의 | 중간 |
| D5-04 | 통계적 타당성 | `1 − n(이상치)/N` | 없음 (IQR 자동 적용) | 낮음 |
| D6-01 | 데이터 유일성 | `n(유니크레코드)/N` | 없음 | 낮음 |
| D6-02 | 유사 중복 제어 | `1 − n(유사중복페어)/n(전체페어)` | 없음 (대용량 시 샘플링) | 중간 |

> **즉시 측정 가능 지표 (전제 조건 없음 + 자동화 난이도 낮음):** D1-03, D1-04, D2-04, D4-01, D4-02, D5-01, D5-02, D5-04, D6-01 → 총 9개. 기관이 별도 인프라 구축 없이 첫 진단에서 측정 가능한 지표.

---

## 부속서 B (규범적): 품질 등급 매트릭스

**표 B.1 — 차원별 게이트 임계치**

| 차원 | Tier 0 | Tier 1 (Bronze) | Tier 2 (Silver) | Tier 3 (Gold) | Tier 4 (Platinum) |
|---|---|---|---|---|---|
| D1: 완전성 | < 0.60 | ≥ 0.60 | ≥ 0.75 | ≥ 0.85 | ≥ 0.95 |
| D2: 일관성 | < 0.50 | ≥ 0.50 | ≥ 0.70 | ≥ 0.80 | ≥ 0.90 |
| D3: 정확성 | < 0.65 | ≥ 0.65 | ≥ 0.80 | ≥ 0.90 | ≥ 0.95 |
| D4: 적시성 | < 0.40 | ≥ 0.40 | ≥ 0.60 | ≥ 0.75 | ≥ 0.85 |
| D5: 유효성 | < 0.60 | ≥ 0.60 | ≥ 0.75 | ≥ 0.85 | ≥ 0.95 |
| D6: 유일성 | < 0.60 | ≥ 0.60 | ≥ 0.75 | ≥ 0.85 | ≥ 0.95 |
| QI | < 0.50 | ≥ 0.50 | ≥ 0.70 | ≥ 0.85 | ≥ 0.95 |

> D3 게이트는 D3 Case B(전체 미측정) 시 자동 면제된다.

---

## 부속서 C (규범적): 품질 진단 리포트 JSON 스키마

전체 JSON Schema는 `https://datahub.kr/schemas/quality-report/v1.0`에서 제공한다.

**스키마 주요 필드 설명:**

- `IndicatorResult.preconditionGuideRef`: PRECONDITION_UNMET 선언 시 부속서 F 해당 구축 단계를 자동 참조
- `IndicatorResult.preconditionCount`: 동일 지표의 누적 선언 횟수 추적 (3회 상한 규칙 적용)
- `QTierResult.preconditionUpperBoundApplied`: 3회 상한 제한 적용 여부 및 대상 차원 기록

---

## 부속서 D (참고): 데이터 유형별 진단 시나리오 예시

### D.1 정형 데이터(STRUCT) — 공장 현황 데이터셋 (DM-2 달성 예시)

- 데이터셋: 전국 산업단지 공장 현황 (CSV, 125만 건)
- 적합성 수준: Level B (DM-2)

| 지표 | 전제 조건 상태 | 결과 |
|---|---|---|
| D1-01 필수 속성 충족도 | APPLIED | 0.96 (종업원수 4% 결측) |
| D1-02 시나리오 변수 충분성 | PRECONDITION_UNMET | null — 시나리오 문서 미작성 |
| D2-01 관계 일관성 | APPLIED | 0.99 |
| D2-03 참조 무결성 | APPLIED | 0.99 |
| D3-01 기준 정합성 | APPLIED | 0.98 |
| D3-02 규칙 정확성 | APPLIED | 0.97 |
| D6-01 데이터 유일성 | APPLIED | 0.997 |

- D3 Case: A (2개 지표 측정)
- 진단 성숙도: DM-2 (D1-02 첫 번째 PRECONDITION_UNMET이므로 DM-2 허용)
- 최종 Q-Tier: `Gold (Tier 3)`

### D.2 정형 데이터(STRUCT) — 노후 데이터셋 (DM-1 진입 예시)

- 데이터셋: 구형 업무 시스템 데이터 (수동 입력, 데이터 사전 없음)
- 즉시 측정 가능 지표(전제 조건 없음): D1-03, D1-04, D2-04, D4-01, D5-01, D5-04, D6-01 = 7개
- 진단 성숙도: DM-1 (필수 14개 중 7개 측정 = 50%)
- Q-Tier: `Silver (Tier 2, DM-1)` → 공식 공시 불가, 내부 개선 참고용

---

## 부속서 E (참고): 컬럼 수준 진단 결과 확장 가이드

### E.1 목적

Dataset-level QI는 "어느 차원이 낮은가"를 알려주지만, "어느 컬럼이 원인인가"는 알려주지 않는다. 컬럼 수준 진단은 원인 진단과 자동 개선 액션 연결을 위한 기반이다.

### E.2 적용 원칙

- 컬럼 수준 진단은 선택(MAY). Level C(DM-3) 적합성 달성 시 권장(SHOULD)으로 격상.
- 결과는 `IndicatorResult.details` 필드에 기록.
- AI-Ready Data Metadata Profile(AIRD-STD-002) `cr:Field`(Column Registry)와 연결 가능한 경우 컬럼 식별자를 함께 기록(SHALL).

### E.3 지표별 details 스키마 예시

**D1-01 details:**
```json
{
  "columnBreakdown": [
    {"column": "종업원수", "columnId": "cr:field:001", "nullRate": 0.04, "isCore": true},
    {"column": "사업자번호", "columnId": "cr:field:002", "nullRate": 0.00, "isCore": true}
  ],
  "coreColumnNullRate": 0.010,
  "concentrationAlert": false
}
```

**D5-03 details:**
```json
{
  "columnBreakdown": [
    {"column": "종업원수", "min": 0, "max": 9999, "violationRate": 0.001},
    {"column": "매출액", "min": 0, "max": null, "violationRate": 0.0}
  ]
}
```

**D6-02 details:**
```json
{
  "samplingMethod": "RANDOM",
  "samplingRatio": 0.10,
  "duplicatePairCount": 142,
  "totalPairsSampled": 5000000
}
```

### E.4 AI-Ready Data Metadata Profile 연결을 통한 확장 가능성

컬럼 수준 결과 + AI-Ready Data Metadata Profile(AIRD-STD-002) `cr:Field` 연결 시:
- **Explainable Quality:** "D1 완전성 0.92 = 종업원수 컬럼 결측 4%"를 자동 설명문 생성
- **자동 개선 액션 연결:** AI-Ready Data Transformation & Governance Specification(AIRD-STD-003) Stage 2에서 컬럼별 처리 방법 파이프라인 전달

---

## 부속서 F (참고): 전제 조건 구축 가이드 및 템플릿

> **본 부속서는 기관이 DM-1에서 DM-2로 전환하기 위한 최소 실행 경로를 제공한다.**
> 진단 리포트의 `preconditionGuideRef` 필드가 아래 단계를 자동 참조하도록 설계되어 있으므로, 리포트를 받은 담당자는 해당 단계부터 구축 작업을 시작하면 된다.

### F.1 전제 조건별 구축 우선순위

기관의 데이터 인프라 성숙도에 따라 아래 순서로 구축을 권장한다.

| 단계 | 구축 항목 | 영향 지표 | 예상 소요 | 효과 |
|---|---|---|---|---|
| 1단계 | 필수 필드 목록 정의 | D1-01 | 1–2주 | 즉시 측정 가능 |
| 2단계 | 메타데이터 갱신일·주기 기록 | D4-01 | 1주 | 적시성 측정 가능 |
| 3단계 | 컬럼별 허용 범위 정의 (데이터 사전) | D5-03 | 2–4주 | 유효성 강화 |
| 4단계 | 업무 규칙 목록 정의 | D2-01 | 2–6주 | 일관성 측정 가능 |
| 5단계 | 활용 시나리오 문서 작성 | D1-02 | 2–4주 | 완전성 강화 |
| 6단계 | 참조 코드 테이블 연동 | D2-03, D3-01 | 1–3개월 | 정확성 일부 측정 |
| 7단계 | 전문가 라벨 검수 체계 구축 | D3-03 | 장기 | 정확성 완전 측정 |

### F.2 PRECONDITION_UNMET 선언 기록 템플릿

```
지표 ID: [예: D2-01]
선언 일시: [ISO 8601]
누적 선언 횟수: [1 / 2 / 3]
참조 단계: [예: 4단계 — 업무 규칙 정의]
미충족 전제 조건: [예: 업무 규칙 정의서 미작성]
현재 상태: [예: 담당 부서 협의 중]
구축 계획: [예: 2026-10-01까지 업무 규칙 정의서 초안 작성]
구축 책임자: [성명 및 직위]
적용 조치: [1회: 기록만 / 2회: 계획서 제출 / 3회: Q-Tier 상한 제한 적용]
```

> 동일 지표에 2회 연속 PRECONDITION_UNMET 선언 시 이 템플릿을 소관 전담 기관에 제출하여야 한다(SHALL).
> 3회 연속 시 해당 차원의 Q-Tier 게이트 기준이 Tier 1로 고정되며, 전체 Q-Tier 강등으로 이어진다(5.1절 4항 참조).
> 리포트의 `preconditionGuideRef` 필드 값을 이 템플릿의 "참조 단계" 필드에 그대로 기입하면 된다.

*— 끝 —*
