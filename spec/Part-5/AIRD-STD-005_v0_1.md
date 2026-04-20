# AI-Ready Data Discovery & Exchange Specification
## AI-Ready 데이터 팩 탐색·교환 규격

| 항목 | 내용 |
|---|---|
| 문서 번호 | AIRD-STD-005 |
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
| AIRD-STD-003 | AI-Ready Data Transformation & Governance Specification | ETL 파이프라인·AIRD Pack·거버넌스 — 실행·운영 |
| **AIRD-STD-005** | **AI-Ready Data Discovery & Exchange Specification (본 표준)** | **Pack 탐색·교환·에이전트 인터페이스 — 탐색·유통** |
| AIRD-OPG-001 | 품질 진단 운영 지침 *(예정)* | 진단 주기·유효기간·이의제기·도구 인증 — 운영 세부 |
| AIRD-TR-001 | 가중치 설계 기술 보고서 *(예정)* | Purpose-Type별 가중치 수치 근거 |

> **설계 원칙**
>
> 이 표준은 AI-Ready Data Transformation & Governance Specification(AIRD-STD-003)이 생성한 AIRD Pack을 소비자(사람·AI 시스템·에이전트)에게 **전달하는(deliver)** 표준이다. Pack의 내부 구조와 데이터 내용은 건드리지 않는다.
>
> 세 가지 원칙이 전반을 관통한다.
>
> 첫째, **내용 중립 원칙을 준수한다.** 이 표준은 Pack을 어떻게 찾고 전달하는가를 규정하며, Pack 안의 데이터 구조·메타데이터 스키마·품질 기준은 선행 표준(AIRD-STD-001~003)의 소관이다. 선행 표준이 정의한 내용을 재정의하지 않는다.
>
> 둘째, **기술 스택 중립 원칙을 준수한다.** 에이전트 인터페이스·A2A·MCP 등 특정 구현 기술을 규범적으로 강제하지 않는다. 추상 인터페이스 요건을 정의하고 구체적 구현은 참고 부속서로 처리한다.
>
> 셋째, **계보 연속성 원칙을 준수한다.** Pack이 교환되는 과정에서 AIRD-STD-003이 생성한 Provenance(`provenance.jsonld`)가 단절되지 않도록 한다. 소비자 측에서 발생하는 파생 계보는 원본 Pack의 계보에 연결되어야 한다.

---

## 서문

AI-Ready 데이터 표준 시리즈(AIRD)는 공공데이터를 Raw 상태에서 Quality-Ready·Purpose-Ready 상태로 전환하는 전 과정을 규율한다. AIRD-STD-001~003이 데이터를 **만드는** 체계를 정의한다면, 이 표준(AIRD-STD-005)은 만들어진 AIRD Pack을 소비자에게 **유통하는** 체계를 정의한다.

현재 공공데이터 유통의 구조적 한계는 두 가지다. 첫째, Pack이 존재하더라도 소비자가 그것을 탐색할 방법이 없다. 둘째, Pack을 찾았더라도 신뢰를 확인하고 교환하는 표준 방식이 없어 소비자가 자체적으로 검증 과정을 반복해야 한다.

이 표준은 다음 세 가지 목적을 위해 제정한다.

1. **탐색 가능성(Discoverability):** 소비자가 목적·품질·접근 조건에 따라 Pack을 정확하게 찾을 수 있도록 레지스트리와 탐색 인터페이스를 정의한다.
2. **교환 가능성(Interoperability):** Pack이 공급자에서 소비자로 안전하게 전달되도록 물리적 교환 규격을 정의한다.
3. **계보 연속성(Provenance Continuity):** Pack 교환 이후 소비자 측에서 생성되는 파생 계보가 원본 계보와 연결되도록 규칙을 정의한다.

이 표준의 기술 내용은 데이터의 출처(공공/민간)나 보유 주체의 성격과 무관하게 적용 가능하다.

---

## 머리말

이 표준은 AI-Ready Data Transformation & Governance Specification(AIRD-STD-003)이 생성한 AIRD Pack의 물리적 교환 규격, 레지스트리 구조 및 탐색 인터페이스, 에이전트 소비 프로토콜, 소비자 피드백 루프 API, 그리고 교환 이후 계보 연속성 보장 규칙을 규정한다.

이 표준은 AIRD-STD-003 1.2절(적용 범위 외)에서 "Pack 탐색 API·에이전트 인터페이스·배포 규격"으로 위임한 사항을 수신한다.

---

## 목차

1. 적용 범위
2. 인용 표준
3. 용어 및 정의
4. 표준 시리즈에서의 위치
5. Pack 물리적 교환 규격
6. Pack 레지스트리
7. Pack 탐색 인터페이스
8. 에이전트 소비 프로토콜
9. 소비자 피드백 루프 API
10. 교환 후 계보 연속성
11. 접근 제어 및 이용 조건
12. 적합성

**부속서**
- 부속서 A (규범적): Pack 교환 검증 절차서
- 부속서 B (규범적): 계보 연속성 JSON-LD 예시
- 부속서 C (참고): 탐색 API 요청·응답 예시
- 부속서 D (참고): 에이전트 소비 시나리오
- 부속서 E (참고): 표준 간 참조 매트릭스
- 부속서 F (참고): 구현 기술 스택 가이드

---

## 1. 적용 범위

### 1.1 목적 및 적용 대상

이 표준은 AIRD-STD-003이 생성한 AIRD Pack의 탐색·교환·소비에 대하여 다음 사항을 규정한다.

**(a)** AIRD Pack의 물리적 교환 포맷, 네이밍 컨벤션, 무결성 전달 보장 규칙

**(b)** Pack 레지스트리의 최소 요건 및 Pack 등록·갱신·폐기 절차

**(c)** 소비자(사람·AI 시스템·에이전트)가 Pack을 탐색하기 위한 인터페이스 요건

**(d)** AI 에이전트가 Pack을 자율적으로 탐색·선택·검증·소비하는 상호작용 흐름

**(e)** AIRD-STD-003 10.4절에서 정의한 소비자 피드백 신호(유형 A/B/C)를 공급자 파이프라인에 전달하는 API 규격

**(f)** Pack 교환 이후 소비자 측 파생 계보가 원본 계보와 연결되는 규칙

**적용 대상:**

| 구분 | 대상 | 적용 의무 |
|---|---|---|
| 필수 적용 | AIRD-STD-003을 필수 적용하는 공공기관이 Pack을 외부에 공개하는 경우 | SHALL |
| 준용 권장 | 민간 데이터 플랫폼, 연구기관 데이터 저장소, 기업 내부 데이터 마켓플레이스 | MAY |

### 1.2 적용 범위 외

| 사항 | 담당 문서 |
|---|---|
| Pack 내부 데이터 구조 및 메타데이터 스키마 | AI-Ready Data Metadata Profile (AIRD-STD-002), AI-Ready Data Transformation & Governance Specification (AIRD-STD-003) |
| 품질 측정 공식·QI 산정·Q-Tier 판정 | Quality-Ready Data Preparation Framework (AIRD-STD-001) |
| Pack 생성 파이프라인 및 Gate 판정 절차 | AI-Ready Data Transformation & Governance Specification (AIRD-STD-003) |
| 적합성 인증 절차·인증 마크·검토 위원회 | AIRD-STD-004 (예정) |
| 진단 주기·결과 유효기간·이의제기·도구 인증 | AIRD-OPG-001 (예정) |
| 에이전트가 Pack을 소비한 이후의 행동(학습 실행·추론 등) | MLOps 표준 / 도메인 기술규격 |
| 특정 클라우드 스토리지·API 프레임워크의 구현 명세 | 구현 기술 스택 가이드 (부속서 F) |

> **설계 원칙**
>
> **내용 중립:** 이 표준은 Pack을 어디서 찾고 어떻게 전달하는가를 규정한다. Pack 안의 데이터 내용, 품질 기준, 메타데이터 스키마는 선행 표준의 소관이며, 이 표준은 그것을 건드리지 않는다.
>
> **기술 스택 중립:** A2A, MCP, REST, GraphQL 등 특정 구현 기술을 규범적으로 강제하지 않는다. 추상 인터페이스 요건을 규정하고, 구현 예시는 참고 부속서(부속서 F)로 처리한다. 기술 환경 변화에 따라 부속서만 개정하는 구조를 유지한다.
>
> **계보 단절 방지:** Pack 교환은 단순한 파일 전달이 아니다. AIRD-STD-003이 생성한 Provenance 체인이 교환 이후에도 유지되어야 공급자-소비자 간 감사 추적이 가능하다.

---

## 2. 인용 표준

### 2.1 내부 표준

| 표준번호 | 표준명 | 버전 | 비고 |
|---|---|---|---|
| AIRD-STD-001 | Quality-Ready Data Preparation Framework | v0.1 | Q-Tier 판정 기준 |
| AIRD-STD-002 | AI-Ready Data Metadata Profile | v0.1 | 메타데이터 스키마·purposeReadinessVector |
| AIRD-STD-003 | AI-Ready Data Transformation & Governance Specification | v0.1 | Pack 구조·Provenance·피드백 루프 정의 |

### 2.2 외부 표준

| 표준 / 규격 | 발행 기관 | 적용 내용 |
|---|---|---|
| DCAT v3 | W3C | 데이터 카탈로그 어휘. Pack 레지스트리 메타데이터 기반 |
| PROV-O: The PROV Ontology | W3C | 계보 연속성 기록 기반 |
| RFC 9110 | IETF | HTTP 시맨틱스. 탐색 API 기반 프로토콜 |
| RFC 8785 | IETF | JSON Canonicalization Scheme (JCS). 교환 무결성 검증 |
| RFC 6920 | IETF | Named Information URI. Pack 식별자 체계 |
| ISO 8601:2019 | ISO | 일시 표기 |
| SemVer 2.0.0 | semver.org | Pack 버전 체계 |
| OpenAPI 3.1 | OpenAPI Initiative | 탐색 API 명세 포맷 (참고) |

---

## 3. 용어 및 정의

이 표준에서 사용하는 용어 중 Quality-Ready Data Preparation Framework(AIRD-STD-001), AI-Ready Data Metadata Profile(AIRD-STD-002), AI-Ready Data Transformation & Governance Specification(AIRD-STD-003)에서 정의된 용어는 해당 표준의 정의를 따른다.

> **승계 용어:** AIRD Pack, Purpose-Type, Quality-Ready, Purpose-Ready, Q-Tier, purposeReadinessVector, agentAccessible, modelDataCoupling, packCompleteness, sourceDataVersion, Stale, 소비자 피드백 루프(유형 A/B/C), Provenance, prov:wasGeneratedBy, prov:wasDerivedFrom, aird:PreprocessingActivity, aird:TransformationActivity

이 표준에서 추가로 정의하는 용어는 다음과 같다.

### 3.1 Pack 레지스트리 (Pack Registry)

Purpose-Ready 상태의 AIRD Pack 목록을 관리하고 탐색 가능하게 하는 카탈로그 시스템. 중앙집중식 또는 연합형(federated)으로 운영될 수 있다.

### 3.2 탐색 인터페이스 (Discovery Interface)

소비자가 레지스트리에서 Pack을 검색·필터링·조회하는 데 사용하는 API 또는 프로토콜의 총칭.

### 3.3 교환 단위 (Exchange Unit)

단일 교환 트랜잭션에서 전달되는 최소 단위. 완전한 Pack 디렉터리 또는 메타데이터-only 교환이 허용되는 부분 교환 단위를 포함한다.

### 3.4 에이전트 소비자 (Agent Consumer)

`agentAccessible: true`인 Pack을 사람의 개입 없이 자율적으로 탐색·선택·검증·소비하는 AI 시스템 또는 자동화 파이프라인.

### 3.5 파생 계보 (Derived Provenance)

소비자가 Pack을 받아 추가 변환·활용 시 생성하는 Provenance 기록. 원본 Pack의 `provenance.jsonld`와 `prov:wasDerivedFrom`으로 연결되어야 한다.

### 3.6 메타데이터-only 교환 (Metadata-only Exchange)

Pack의 `metadata.json`과 `manifest.json`만 전달하는 부분 교환. 소비자가 Pack을 평가하고 수신 여부를 결정하는 목적으로 사용한다. 데이터 파일(`data/`)은 포함되지 않는다.

### 3.7 Pack URI

Pack을 전역적으로 고유하게 식별하는 URI. 레지스트리에 등록 시 발급되며, 소비자가 Pack을 직접 참조하거나 파생 계보에서 원본을 참조하는 데 사용된다.

### 3.8 교환 이력 (Exchange Record)

단일 교환 트랜잭션의 공급자·소비자·일시·Pack URI·무결성 검증 결과를 기록한 구조. Provenance 체인의 일부로 기록된다.

### 3.9 탐색 필터 (Discovery Filter)

탐색 인터페이스에서 Pack을 좁히기 위해 사용하는 조건. `purposeType`, `qualityTier`, `agentAccessible`, `modelDataCoupling` 등 manifest.json 필드를 기반으로 한다.

### 3.10 Stale 신호 (Stale Signal)

소비자가 Pack의 원본 데이터 갱신 또는 노후화를 감지하여 공급자에게 전달하는 피드백 신호. AIRD-STD-003 유형 C 피드백에 해당한다.

---

## 4. 표준 시리즈에서의 위치

### 4.1 전체 흐름에서의 역할

이 표준은 AIRD 표준 시리즈의 소비 단계를 담당한다.

```
[원천 데이터]
      │
      ▼
AIRD-STD-001 — 품질 측정·판정 (무엇을 측정하는가)
AIRD-STD-002 — 메타데이터 스키마 (어떻게 기록하는가)
AIRD-STD-003 — 파이프라인·Pack 생성 (어떻게 만드는가)
AIRD-STD-004 — 적합성 인증 (신뢰할 수 있는가) ← 예정
      │
      ▼
   [AIRD Pack — Purpose-Ready]
      │
      ▼
AIRD-STD-005 — 탐색·교환·소비 (어떻게 유통하는가) ← 본 표준
      │
      ▼
[소비자: 사람·AI 시스템·에이전트]
```

### 4.2 선행 표준으로부터 수신하는 위임

| 위임 출처 | 위임 내용 |
|---|---|
| AIRD-STD-003 1.2절 (적용 범위 외) | Pack 탐색 API·에이전트 인터페이스·배포 규격 |
| AIRD-STD-003 1.2절 설계 원칙 | AI 에이전트·A2A·MCP 등 소비 방식의 기술 스택 중립 선언 |
| AIRD-STD-003 7.4절 (AIRD Pack 구조) | Pack의 물리적 패키징 형식(압축·번들링 규칙) |
| AIRD-STD-003 10.4절 (소비자 피드백 루프) | 유형 A/B/C 피드백 신호 API 명세 |

### 4.3 AIRD-STD-004와의 관계

AIRD-STD-004(예정)가 Pack의 신뢰를 **보증**하고, 이 표준은 신뢰 보증된 Pack을 **유통**한다.

AIRD-STD-004가 발행하는 인증 마크 및 적합성 수준(Level A/B/C)은 이 표준의 탐색 필터 조건으로 활용될 수 있다. 이 표준은 AIRD-STD-004의 인증 정보를 탐색 API 응답에 노출하되, 인증 판정 자체를 수행하지 않는다(SHALL NOT).

---

## 5. Pack 물리적 교환 규격

### 5.1 목적

AIRD-STD-003이 정의한 AIRD Pack 디렉터리를 공급자에서 소비자로 안전하게 전달하기 위한 물리적 포맷, 네이밍 컨벤션, 무결성 보장 규칙을 정의한다.

### 5.2 완전 교환 포맷

완전한 Pack 전달 시 다음 포맷을 적용한다(SHALL).

#### 5.2.1 번들링 규칙

**(a) 압축 포맷** — Pack 디렉터리를 `.tar.gz`(기본) 또는 `.zip`으로 번들링한다. 두 포맷 모두 허용하되, 공급자는 지원하는 포맷을 레지스트리 메타데이터에 명시하여야 한다(SHALL).

**(b) 디렉터리 루트 보존** — 압축 해제 시 `{dataset-id}-{purpose-type}-pack-v{version}/` 디렉터리가 최상위에 위치하여야 한다(SHALL).

**(c) 심볼릭 링크 금지** — 번들 내 심볼릭 링크는 허용하지 않는다(SHALL NOT). 보안 및 재현성 확보를 위한 조치이다.

**(d) 파일 인코딩** — 번들 내 모든 텍스트 파일은 UTF-8 without BOM으로 인코딩되어야 한다(SHALL).

#### 5.2.2 네이밍 컨벤션

번들 파일명은 다음 패턴을 따른다(SHALL).

```
{dataset-id}-{purpose-type}-pack-v{version}.tar.gz
```

- `dataset-id`: AIRD-STD-002 `dct:identifier`에서 파생한 슬러그. 소문자 영숫자와 하이픈만 허용.
- `purpose-type`: `ml`, `dl`, `rag`, `kg`, `stats`, `ft` 중 하나.
- `version`: SemVer 2.0.0 형식.

**예시:**
```
factory-data-ml-pack-v1.0.0.tar.gz
admin-text-rag-pack-v2.1.0.zip
```

#### 5.2.3 무결성 보장

**(a) 체크섬 동반 전달** — 번들 파일과 함께 SHA-256 체크섬 파일(`.sha256`)을 동반 전달하여야 한다(SHALL).

```
factory-data-ml-pack-v1.0.0.tar.gz
factory-data-ml-pack-v1.0.0.tar.gz.sha256
```

`.sha256` 파일의 내용 형식:
```
a3f2c1d8e4b7... factory-data-ml-pack-v1.0.0.tar.gz
```

**(b) 내부 무결성 일치** — 압축 해제 후 `manifest.json`의 각 파일 SHA-256이 실제 파일과 일치하여야 한다(SHALL). AIRD-STD-003 9.2절 Canonical Serialization 원칙이 교환 이후에도 유지된다.

**(c) 검증 의무** — 소비자는 Pack 수신 즉시 SHA-256 체크섬을 검증하여야 한다(SHALL). 검증 실패 시 해당 Pack을 사용하여서는 안 된다(SHALL NOT).

### 5.3 메타데이터-only 교환

소비자가 Pack 수신 여부를 사전 평가하는 목적으로 메타데이터-only 교환이 허용된다(MAY).

**(a) 포함 파일** — `metadata.json`과 `manifest.json`만 전달한다. `data/`, `quality-report.json`, `provenance.jsonld`는 포함하지 않는다.

**(b) 명시 의무** — 공급자는 메타데이터-only 교환임을 응답 헤더 또는 교환 레코드에 명시하여야 한다(SHALL).

```json
{
  "exchangeType": "metadata-only",
  "packURI": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0",
  "fullPackAvailable": true,
  "fullPackDownloadURL": "https://..."
}
```

**(c) 사용 제한** — 메타데이터-only 교환으로 수신한 데이터는 평가 목적으로만 사용하여야 하며, AI 학습·추론·서비스 운영에 직접 사용하여서는 안 된다(SHALL NOT).

### 5.4 대용량 Pack 분할 전달

단일 번들 크기가 10 GB를 초과하는 경우 분할 전달을 허용한다(MAY).

**(a) 분할 파일 명명:**
```
factory-data-dl-pack-v1.0.0.tar.gz.part00
factory-data-dl-pack-v1.0.0.tar.gz.part01
factory-data-dl-pack-v1.0.0.tar.gz.part.manifest.json
```

**(b) 분할 매니페스트** — 각 파트 파일의 SHA-256, 바이트 크기, 순서를 기록한 `.part.manifest.json`을 동반 전달하여야 한다(SHALL).

**(c) 재조합 검증** — 소비자는 재조합 후 전체 번들의 SHA-256을 검증하여야 한다(SHALL).

### 5.5 교환 이력 기록

모든 교환 트랜잭션은 교환 이력(Exchange Record)으로 기록되어야 한다(SHALL).

```json
{
  "exchangeId": "aird:exchange/20260414-factory-ml-001",
  "packURI": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0",
  "exchangeType": "full",
  "supplier": "aird:agent/data-portal-go-kr",
  "consumer": "aird:agent/research-institute-xyz",
  "timestamp": "2026-04-14T09:00:00+09:00",
  "integrityVerified": true,
  "bundleChecksum": "a3f2c1d8e4b7..."
}
```

이 기록은 소비자 측 파생 계보(`provenance.jsonld`)의 `prov:wasAssociatedWith` 참조 대상이 된다. 10장 참조.

---

## 6. Pack 레지스트리

### 6.1 목적

AIRD Pack을 등록·관리·공시하여 소비자가 탐색 가능하도록 하는 카탈로그 시스템의 최소 요건을 정의한다.

### 6.2 레지스트리 유형

| 유형 | 설명 | 적용 예시 |
|---|---|---|
| **중앙집중형** | 단일 레지스트리에 모든 Pack이 등록됨 | 국가 공공데이터 포털 |
| **연합형** | 기관별 로컬 레지스트리가 상위 레지스트리와 연동됨 | 부처별 데이터 포털 → 중앙 포털 |
| **자율형** | 공급자가 독립 레지스트리를 운영하고 표준 인터페이스를 노출함 | 민간 데이터 플랫폼 |

연합형 운영 시 하위 레지스트리는 상위 레지스트리와 DCAT 카탈로그 어휘 기반으로 동기화하여야 한다(SHALL).

### 6.3 레지스트리 최소 요건

레지스트리는 다음 기능을 제공하여야 한다(SHALL).

**(a) Pack 등록** — Purpose-Ready 상태(`aird:metadataStatus = "Purpose-Ready"`)의 Pack만 등록 가능하다. 등록 시 Pack URI를 발급한다.

**(b) Pack URI 발급** — 전역 고유 URI를 발급하여야 한다. URI 패턴:

```
https://{registry-domain}/packs/{dataset-id}-{purpose-type}-pack-v{version}
```

**(c) 메타데이터 색인** — 다음 필드를 색인하여 탐색 필터로 사용 가능하도록 하여야 한다(SHALL).

| 필드 출처 | 필드 | 색인 의무 |
|---|---|---|
| manifest.json | `purposeType` | SHALL |
| manifest.json | `qualityTier` | SHALL |
| manifest.json | `diagnosticMaturity` | SHALL |
| manifest.json | `agentAccessible` | SHALL |
| manifest.json | `modelDataCoupling` | SHALL |
| manifest.json | `packCompleteness` | SHALL |
| manifest.json | `sourceDataVersion` | SHALL |
| metadata.json | `aird:purposeReadinessVector` | SHALL |
| metadata.json | `dct:language` | SHALL |
| metadata.json | `dct:temporal` | SHOULD |
| metadata.json | `dct:spatial` | SHOULD |
| AIRD-STD-004 | `certificationLevel` | SHOULD (AIRD-STD-004 제정 후) |

**(d) 상태 관리** — 레지스트리는 Pack의 생애주기 상태를 관리하여야 한다.

| 상태 | 설명 | 소비자 접근 |
|---|---|---|
| `Active` | 정상 유통 중 | 허용 |
| `Stale` | 원본 데이터 갱신으로 노후화됨 | 허용 (Stale 표기 필수) |
| `Suspended` | 공급자 또는 인증 기관에 의해 일시 중단 | 불허 |
| `Deprecated` | 신규 버전으로 대체됨 | 허용 (Deprecated 표기 및 후속 버전 안내 필수) |
| `Withdrawn` | 취소됨 (오류·법적 사유 등) | 불허 |

**(e) 버전 관리** — 동일 Pack의 복수 버전을 관리하고, 최신 버전과 버전 히스토리를 조회 가능하도록 하여야 한다(SHALL).

### 6.4 Pack 등록 절차

```
[공급자: Gate 3 PASS 후]
      │
      ▼
① 레지스트리에 Pack 등록 요청
   (manifest.json + metadata.json 제출)
      │
      ▼
② 레지스트리: 필수 필드 완비 확인
   (6.3절 (c) 색인 필수 필드)
      │ 미충족 → 등록 거부 (사유 반환)
      ▼
③ AIRD-STD-004 인증 상태 확인 (SHOULD)
   (AIRD-STD-004 제정 이전: 생략 가능)
      │
      ▼
④ Pack URI 발급 + 레지스트리 색인 등록
      │
      ▼
⑤ 공급자에게 Pack URI 반환
   (이후 소비자 탐색 가능)
```

### 6.5 Stale 처리

레지스트리는 다음 조건 중 하나라도 충족되면 해당 Pack을 `Stale` 상태로 전환하여야 한다(SHALL).

**(a) 소비자 유형 C 피드백 수신 후 공급자 확인** — AIRD-STD-003 10.4절 절차에 따라 공급자가 Stale 전이를 결정한 경우.

**(b) 공급자 직접 선언** — 공급자가 `manifest.json`의 `sourceDataVersion` 갱신 없이 원본 데이터를 갱신한 사실을 레지스트리에 통보한 경우.

**(c) 유효기간 경과** — AIRD-OPG-001이 정하는 Pack 유효기간이 경과한 경우.

Stale 상태 Pack은 탐색 결과에 포함되되, `"packStatus": "Stale"` 필드를 응답에 반드시 포함하여야 한다(SHALL).

---

## 7. Pack 탐색 인터페이스

### 7.1 목적

소비자가 레지스트리에서 목적·품질·접근 조건에 따라 Pack을 정확하게 찾을 수 있는 인터페이스 요건을 정의한다. 특정 API 기술을 강제하지 않고 추상 인터페이스 수준에서 규정한다.

### 7.2 필수 탐색 기능

레지스트리는 다음 탐색 기능을 제공하여야 한다(SHALL).

#### 7.2.1 필터 탐색 (Filter Search)

6.3절 (c)에서 정의한 색인 필드를 조건으로 Pack 목록을 조회하는 기능.

**필수 필터 조건 (SHALL):**

| 필터 | 값 유형 | 설명 |
|---|---|---|
| `purposeType` | 열거형 | `ml`, `dl`, `rag`, `kg`, `stats`, `ft` |
| `qualityTier` | 열거형 | `Bronze`, `Silver`, `Gold`, `Platinum` |
| `qualityTierMin` | 열거형 | 해당 등급 이상의 Pack만 반환 |
| `agentAccessible` | boolean | `true`이면 에이전트 소비 가능 Pack만 반환 |
| `packStatus` | 열거형 | `Active`, `Stale`, `Deprecated` 등 |
| `diagnosticMaturity` | 열거형 | `DM-1`, `DM-2`, `DM-3` |
| `modelDataCoupling` | 열거형 | `loose`, `derived` |

**권장 필터 조건 (SHOULD):**

| 필터 | 값 유형 | 설명 |
|---|---|---|
| `language` | ISO 639-1 | 데이터 언어 |
| `temporalFrom` / `temporalTo` | ISO 8601 | 시간 범위 |
| `spatial` | GeoJSON Polygon 또는 코드 | 공간 범위 |
| `certificationLevel` | 열거형 | AIRD-STD-004 제정 후: `A`, `B`, `C` |
| `purposeReadiness.{type}` | 열거형 | 특정 Purpose-Type의 Tier 조건 |

#### 7.2.2 단건 조회 (Pack Detail)

Pack URI로 단일 Pack의 상세 정보를 조회하는 기능.

응답에는 다음이 포함되어야 한다(SHALL).
- `manifest.json` 전체 내용
- `metadata.json` 전체 내용
- `packStatus` (현재 상태)
- `downloadURL` (완전 교환 번들 URL, Active 상태 시)
- `metadataOnlyURL` (메타데이터-only 교환 URL)

#### 7.2.3 버전 히스토리 조회

동일 Pack의 버전 목록과 각 버전의 상태를 조회하는 기능.

#### 7.2.4 계보 탐색 (Provenance Traversal)

특정 원본 데이터셋에서 파생된 모든 Pack을 조회하거나, Pack 간 `prov:wasDerivedFrom` 관계를 탐색하는 기능(SHOULD).

### 7.3 탐색 응답 형식

탐색 인터페이스는 다음 요건을 충족하는 응답을 제공하여야 한다(SHALL).

**(a)** 기계 판독 가능한 정형 포맷(JSON-LD 또는 JSON)으로 응답한다.

**(b)** 응답 내 각 Pack 항목에 Pack URI를 포함한다.

**(c)** 페이지네이션을 지원하고 전체 결과 수를 반환한다.

**(d)** `packStatus`가 `Stale` 또는 `Deprecated`인 Pack은 응답 내에 해당 상태와 이유를 명시한다.

**응답 예시 (JSON):**

```json
{
  "totalCount": 42,
  "page": 1,
  "pageSize": 10,
  "packs": [
    {
      "packURI": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0",
      "purposeType": "ML",
      "qualityTier": "Gold",
      "diagnosticMaturity": "DM-2",
      "agentAccessible": true,
      "modelDataCoupling": "loose",
      "packStatus": "Active",
      "sourceDataVersion": "1.2.0",
      "purposeReadinessVector": {
        "ML": "Gold",
        "DL": "Silver",
        "RAG": "N/A"
      },
      "downloadURL": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0.tar.gz",
      "metadataOnlyURL": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0/metadata"
    }
  ]
}
```

### 7.4 DCAT 카탈로그 연계

레지스트리는 DCAT v3 기반 카탈로그 메타데이터를 노출하여야 한다(SHALL). 이를 통해 공공데이터포털 등 기존 데이터 카탈로그에서 AIRD Pack을 `dcat:distribution`으로 참조 가능하게 한다.

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "aird": "http://data.go.kr/ns/aird#"
  },
  "@type": "dcat:Dataset",
  "dct:identifier": "https://data.go.kr/pid/ds-factory-2026",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:format": "AIRD-ML-Pack",
      "dcat:downloadURL": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0.tar.gz",
      "aird:purposeType": "ML",
      "aird:qualityTier": "Gold",
      "aird:agentAccessible": true
    }
  ]
}
```

---

## 8. 에이전트 소비 프로토콜

### 8.1 목적

AI 에이전트가 사람의 개입 없이 AIRD Pack을 자율적으로 탐색·선택·검증·소비하는 상호작용 흐름을 추상 인터페이스 수준에서 정의한다. 특정 에이전트 프레임워크(A2A, MCP 등)를 강제하지 않는다.

### 8.2 에이전트 소비 가능 Pack 조건

에이전트가 자율 소비할 수 있는 Pack은 다음 조건을 모두 충족하여야 한다(SHALL).

| 조건 | 판정 기준 |
|---|---|
| `agentAccessible: true` | manifest.json에 명시 |
| `packStatus: "Active"` | 레지스트리 상태 |
| `diagnosticMaturity` | DM-2 이상 (DM-1은 에이전트 자율 소비 불허) |
| 무결성 검증 통과 | SHA-256 일치 확인 완료 |

> **DM-1 Pack의 에이전트 소비 금지:** DM-1으로 생성된 Pack은 `officialPublicationBlocked: true`가 설정되어 있으며, 에이전트가 이를 감지하여 소비를 자동 거부하여야 한다(SHALL). AIRD-STD-003 10.1절 (c) 참조.

### 8.3 에이전트 소비 흐름

에이전트는 다음 순서로 Pack을 소비하여야 한다(SHALL).

```
① 탐색 (Discover)
   레지스트리 탐색 인터페이스에 필터 조건 전달
   (purposeType, qualityTierMin, agentAccessible=true 등)
      │
      ▼
② 선택 (Select)
   응답된 Pack 목록에서 목적에 맞는 Pack URI 선택
   purposeReadinessVector의 해당 Purpose-Type Tier 확인
      │
      ▼
③ 사전 평가 (Pre-evaluate)
   메타데이터-only 교환으로 metadata.json, manifest.json 수신
   다음 항목 자율 평가:
   - qualityTier가 최소 요건 충족 여부
   - rai:dataBiases (편향성 위험 수준)
   - modelDataCoupling이 사용 목적에 적합한지
   - bronzeUsageNote 존재 시 사용 제한 확인
   - officialPublicationBlocked 플래그 확인
      │ 평가 불합격 → 다른 Pack 선택 또는 사람 에스컬레이션
      ▼
④ 수신 (Receive)
   완전 교환 번들 다운로드
      │
      ▼
⑤ 검증 (Verify)
   SHA-256 체크섬 검증 (번들 + 내부 파일 모두)
      │ 검증 실패 → 유형 A 피드백 신호 발송 + 소비 중단
      ▼
⑥ 소비 (Consume)
   목적에 맞는 방식으로 데이터 활용
   (ML 학습, RAG 인덱스 마운트, KG 로드 등)
      │
      ▼
⑦ 피드백 (Feedback)
   소비 중 문제 감지 시 해당 유형 피드백 신호 발송
   (유형 A: 구조 오류, 유형 B: 품질 저하, 유형 C: 노후화)
```

### 8.4 에이전트 자율 판단 한계

에이전트는 다음 행동을 수행하여서는 안 된다(SHALL NOT).

**(a) 파이프라인 자동 재실행 요청** — 피드백 신호 발송만 허용하며, 공급자 파이프라인의 재실행을 직접 트리거하여서는 안 된다. AIRD-STD-003 10.4.3절 참조.

**(b) Pack 내부 데이터 임의 수정** — 에이전트는 Pack의 내용을 수정하지 않고 원본 그대로 사용하여야 한다.

**(c) DM-1 Pack 자율 소비** — 8.2절 조건 미충족 Pack의 자율 소비를 자동으로 진행하여서는 안 된다. 사람 에스컬레이션이 필요하다.

### 8.5 에이전트 소비 기록 의무

에이전트는 소비 이력을 다음 항목과 함께 기록하여야 한다(SHALL). 이 기록은 10장의 파생 계보에 연결된다.

| 항목 | 설명 |
|---|---|
| 소비 에이전트 식별자 | URI 형식의 에이전트 식별자 |
| 소비 Pack URI | 레지스트리에서 발급된 Pack URI |
| 소비 일시 | ISO 8601 |
| 무결성 검증 결과 | `true` / `false` |
| 소비 목적 | 학습·추론·RAG 인덱스 등 |

---

## 9. 소비자 피드백 루프 API

### 9.1 목적

AIRD-STD-003 10.4절에서 정의한 소비자 피드백 루프(유형 A/B/C)를 실제로 전달하는 API 규격을 정의한다. AIRD-STD-003이 신호 유형과 후속 조치를 정의하였다면, 이 표준은 그 신호를 어떻게 전달하는가를 정의한다.

### 9.2 피드백 신호 구조

피드백 신호는 다음 공통 구조를 따른다(SHALL).

```json
{
  "signalId": "aird:signal/20260414-factory-ml-a-001",
  "signalType": "A",
  "packURI": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0",
  "consumer": "aird:agent/research-institute-xyz",
  "detectedAt": "2026-04-14T14:30:00+09:00",
  "description": "manifest.json의 SHA-256이 실제 train.csv와 불일치",
  "evidence": {
    "file": "data/train.csv",
    "expectedChecksum": "a3f2c1...",
    "actualChecksum": "b9e4d7..."
  }
}
```

**유형별 필수 필드:**

| 필드 | 유형 A (구조 오류) | 유형 B (품질 저하) | 유형 C (노후화) |
|---|---|---|---|
| `signalType` | `"A"` | `"B"` | `"C"` |
| `packURI` | SHALL | SHALL | SHALL |
| `consumer` | SHALL | SHALL | SHALL |
| `detectedAt` | SHALL | SHALL | SHALL |
| `description` | SHALL | SHALL | SHALL |
| `evidence.file` | SHALL | SHOULD | 해당없음 |
| `evidence.performanceMetric` | 해당없음 | SHOULD | 해당없음 |
| `evidence.sourceUpdateURL` | 해당없음 | 해당없음 | SHOULD |

### 9.3 피드백 전달 엔드포인트

레지스트리는 피드백 신호 수신 엔드포인트를 운영하여야 한다(SHALL). 엔드포인트 URI 패턴:

```
POST https://{registry-domain}/packs/{pack-id}/feedback
```

응답 코드:

| HTTP 상태 | 의미 |
|---|---|
| 202 Accepted | 신호 수신 완료. 처리는 비동기적으로 진행됨. |
| 400 Bad Request | 필수 필드 누락 또는 형식 오류 |
| 404 Not Found | Pack URI가 레지스트리에 없음 |
| 429 Too Many Requests | 동일 Pack에 대한 과도한 신호 발송 |

### 9.4 피드백 처리 원칙

**(a)** 수신된 피드백 신호는 파이프라인 운영자에게 전달되어야 한다(SHALL).

**(b)** 피드백 신호만으로 파이프라인이 자동 재실행되어서는 안 된다(SHALL NOT). AIRD-STD-003 10.4.3절 준수.

**(c)** 신호 수신부터 조치 완료까지의 이력을 Provenance에 기록하여야 한다(SHALL).

**(d)** 유형 A 신호 수신 시 레지스트리는 해당 Pack의 탐색 결과에 `"signalPending": true`를 즉시 표시하여야 한다(SHALL). 파이프라인 운영자의 조치 전까지 소비자에게 문제 가능성을 고지한다.

### 9.5 피드백 이력 공개

레지스트리는 Pack별 피드백 수신 이력(익명화된 신호 유형 및 처리 상태)을 탐색 응답에 포함하여야 한다(SHOULD). 소비자가 Pack 선택 시 과거 피드백 이력을 참고할 수 있도록 한다.

```json
{
  "packURI": "...",
  "feedbackHistory": [
    {
      "signalType": "A",
      "receivedAt": "2026-03-15",
      "resolution": "RESOLVED",
      "resolvedAt": "2026-03-16"
    }
  ]
}
```

---

## 10. 교환 후 계보 연속성

### 10.1 목적

Pack 교환 이후 소비자가 데이터를 추가 변환하거나 활용할 때 생성되는 파생 계보가 AIRD-STD-003이 생성한 원본 계보(`provenance.jsonld`)와 단절되지 않도록 연결 규칙을 정의한다.

### 10.2 계보 역할 분담

| 계보 구간 | 생성 주체 | 규율 표준 |
|---|---|---|
| Raw → Quality-Ready → Purpose-Ready | 공급자 파이프라인 | AIRD-STD-003 8장 |
| Pack 교환 트랜잭션 | 레지스트리 / 공급자 | **본 표준 10.3절** |
| Purpose-Ready 이후 소비자 활용 | 소비자 | **본 표준 10.4절** |

이 표준은 교환 트랜잭션과 소비자 활용 구간의 계보 기록 규칙을 정의한다. AIRD-STD-003이 생성한 계보 내용은 변경하지 않는다(SHALL NOT).

### 10.3 교환 트랜잭션 계보 기록

레지스트리는 Pack 교환 시 교환 이력(5.5절)을 W3C PROV-O 어휘로 기록하여야 한다(SHALL).

> **`aird:ExchangeActivity` 타입 안내:** 이 타입은 AIRD-STD-002 4.3절의 Activity 타입 목록에 추가 등록이 필요한 상태이다. v0.2에서 AIRD-STD-002와 정합성을 확인하여 정식 등록한다.

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "aird": "http://data.go.kr/ns/aird#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "aird:activity/exchange-20260414-factory-ml-001",
  "@type": ["prov:Activity", "aird:ExchangeActivity"],
  "prov:startedAtTime": { "@value": "2026-04-14T09:00:00+09:00", "@type": "xsd:dateTime" },
  "prov:endedAtTime":   { "@value": "2026-04-14T09:02:15+09:00", "@type": "xsd:dateTime" },
  "prov:wasAssociatedWith": { "@id": "aird:agent/data-portal-go-kr" },
  "aird:consumer": { "@id": "aird:agent/research-institute-xyz" },
  "prov:used": { "@id": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0" },
  "aird:integrityVerified": true,
  "aird:exchangeType": "full"
}
```

### 10.4 소비자 파생 계보 기록 규칙

소비자가 Pack을 활용하여 추가 처리(모델 학습, 추가 변환, 서비스 운영 등)를 수행하는 경우, 파생 계보를 기록하여야 한다(SHOULD).

파생 계보는 다음 규칙을 따른다(SHALL).

**(a) 원본 Pack URI 참조** — `prov:wasDerivedFrom`으로 원본 Pack URI를 반드시 참조하여야 한다.

**(b) 교환 Activity 참조** — `prov:wasInformedBy`로 교환 트랜잭션 Activity를 참조하여야 한다.

**(c) 소비자 측 변환 내용 기록** — 소비자가 수행한 추가 변환(Fine-tuning, 추가 필터링, 서브셋 추출 등)을 기록하여야 한다.

> **`aird:ConsumerActivity` 타입 안내:** 이 타입은 AIRD-STD-002 4.3절의 Activity 타입 목록에 추가 등록이 필요한 상태이다. v0.2에서 AIRD-STD-002와 정합성을 확인하여 정식 등록한다.

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "aird": "http://data.go.kr/ns/aird#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "aird:activity/consumer-transform-20260414-xyz-001",
  "@type": ["prov:Activity", "aird:ConsumerActivity"],
  "prov:startedAtTime": { "@value": "2026-04-14T10:00:00+09:00", "@type": "xsd:dateTime" },
  "prov:endedAtTime":   { "@value": "2026-04-14T12:00:00+09:00", "@type": "xsd:dateTime" },
  "prov:wasAssociatedWith": { "@id": "aird:agent/research-institute-xyz" },
  "prov:used": { "@id": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0" },
  "prov:wasInformedBy": { "@id": "aird:activity/exchange-20260414-factory-ml-001" },
  "prov:generated": {
    "@id": "aird:entity/factory-ml-finetuned-model-v1.0",
    "prov:wasDerivedFrom": { "@id": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0" }
  },
  "aird:parameters": {
    "consumerAction": "model-training",
    "framework": "PyTorch",
    "frameworkVersion": "2.3.0"
  }
}
```

### 10.5 피드백 루프 계보 연결

AIRD-STD-003 10.4절에 따라 피드백 신호가 발송되고 처리된 경우, 그 이력은 원본 Pack의 `provenance.jsonld`에 추가 기록되어야 한다(SHALL).

```json
{
  "@id": "aird:activity/feedback-resolution-20260414-001",
  "@type": ["prov:Activity", "aird:FeedbackResolutionActivity"],
  "aird:signalType": "A",
  "aird:signalId": "aird:signal/20260414-factory-ml-a-001",
  "prov:used": { "@id": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0" },
  "aird:resolution": "Stage3Repackaged",
  "prov:endedAtTime": { "@value": "2026-04-15T09:00:00+09:00", "@type": "xsd:dateTime" }
}
```

---

## 11. 접근 제어 및 이용 조건

### 11.1 접근 수준 정의

레지스트리는 Pack별 접근 수준을 다음 중 하나로 분류하여 관리하여야 한다(SHALL).

| 접근 수준 | 설명 | 탐색 가능 | 다운로드 |
|---|---|---|---|
| `Open` | 누구나 접근 가능 | 모두 | 인증 불필요 |
| `Registered` | 등록 사용자만 접근 | 모두 (메타데이터) | 등록 후 가능 |
| `Restricted` | 특정 조건 충족자만 접근 | 메타데이터만 | 승인 후 가능 |
| `Confidential` | 레지스트리 내부 관리 | 탐색 불가 | 불가 |

`agentAccessible: true`인 Pack은 `Open` 또는 `Registered` 접근 수준이어야 한다(SHALL).

### 11.2 이용 조건 전달

Pack의 이용 조건(`dct:license`, `dct:rights`, AIRD-STD-002 Layer 1 권리·이용 메타데이터)은 탐색 응답 및 교환 시 소비자에게 전달되어야 한다(SHALL).

소비자(에이전트 포함)는 이용 조건을 확인하고 준수하여야 한다(SHALL).

### 11.3 DM-1 Pack 공시 차단

AIRD-STD-003 10.1절 (c)에 따라 `officialPublicationBlocked: true`인 Pack은 레지스트리의 공식 탐색 경로에서 반환하여서는 안 된다(SHALL NOT). 내부 테스트 및 운영자 검토 목적으로만 접근을 허용할 수 있다(MAY).

### 11.4 Q-Bronze Pack 이용 고지

`qualityTier: "Bronze"`인 Pack은 탐색 응답에 AIRD-STD-003 7.6절 (b)의 `bronzeUsageNote`를 포함하여야 한다(SHALL). 소비자는 이 고지를 확인 후 활용 여부를 결정하여야 한다.

---

## 12. 적합성

> **운영 상태와 적합성은 독립적인 두 축이다.**
>
> `aird:metadataStatus = "Purpose-Ready"`인 Pack이 레지스트리에 등록되어 있다고 해서 이 표준의 적합성 수준을 자동으로 달성하는 것은 아니다. 이 표준의 적합성은 탐색·교환·소비 과정의 절차 준수를 선언한다.

### 12.1 적합성 수준

**표 12.1 — 적합성 수준**

| 수준 | 명칭 | 요구사항 |
|---|---|---|
| Level X1 | 교환 적합성 | 5장의 물리적 교환 규격을 준수하여 Pack을 전달한다 |
| Level X2 | 레지스트리 적합성 | Level X1 + 6장의 레지스트리 최소 요건을 충족하여 Pack을 등록·관리한다 |
| Level X3 | 완전 적합성 | Level X2 + 7~11장의 탐색·에이전트·피드백·계보 전 요건을 충족한다 |

### 12.2 전체 표준 시리즈 적합성 매핑

| 본 표준 (AIRD-STD-005) | AIRD-STD-003 전제 | AIRD-STD-004 전제 | 달성 상태 |
|---|---|---|---|
| Level X1 | Level C (목적 적합성) | — | Pack 교환 가능 |
| Level X2 | Level C | — | 레지스트리 공시 가능 |
| Level X3 | Level C | Level A 이상 (권장) | 에이전트 자율 소비 가능 |

### 12.3 적합성 선언

적합성 선언문에는 다음을 포함하여야 한다(SHALL).

- 선언 주체 (기관명·담당자)
- 적합성 수준 (Level X1 / X2 / X3)
- 레지스트리 URI (Level X2 이상)
- 선언 일시 (ISO 8601)

**적합성 선언 예시 (Level X3):**

```yaml
Conformance:
  Standard: AIRD-STD-005
  Version: v0.1
  Level: X3
  Registry: "https://registry.data.go.kr"
  AgentInterfaceSupported: true
  FeedbackLoopEnabled: true
  ProvenanceContinuityEnforced: true
  DeclarationDate: "2026-04-14"
  DeclaredBy: "〈기관명〉"
```

---

## 부속서 A (규범적): Pack 교환 검증 절차서

> **이 부속서는 규범적(normative)이다.**

### A.1 공급자 측 송신 검증 체크리스트

| 번호 | 검증 항목 | 기준 | 결과 |
|---|---|---|---|
| S-01 | Pack 상태 확인 | `aird:metadataStatus = "Purpose-Ready"` | □ |
| S-02 | 번들 포맷 | `.tar.gz` 또는 `.zip` | □ |
| S-03 | 번들 네이밍 | 5.2.2절 패턴 준수 | □ |
| S-04 | 체크섬 파일 동반 | `.sha256` 파일 존재 | □ |
| S-05 | 내부 무결성 | manifest.json 내 전 파일 SHA-256 일치 | □ |
| S-06 | 심볼릭 링크 없음 | 번들 내 심볼릭 링크 부재 | □ |
| S-07 | 이용 조건 포함 | `dct:license` 기록 완료 | □ |
| S-08 | DM-1 차단 | `officialPublicationBlocked: true` 시 공식 배포 경로 차단 | □ |

### A.2 소비자 측 수신 검증 체크리스트

| 번호 | 검증 항목 | 기준 | 결과 |
|---|---|---|---|
| R-01 | 번들 체크섬 | 번들 `.sha256`와 실제 파일 일치 | □ |
| R-02 | 압축 해제 | 오류 없이 완료 | □ |
| R-03 | 디렉터리 구조 | AIRD-STD-003 7.4절 구조 충족 | □ |
| R-04 | 내부 무결성 | manifest.json 내 전 파일 SHA-256 일치 | □ |
| R-05 | Pack 상태 확인 | 레지스트리에서 `Active` 상태 확인 | □ |
| R-06 | 이용 조건 확인 | `dct:license` 내용 확인 및 준수 서약 | □ |
| R-07 | 에이전트 소비 조건 | 에이전트 소비 시 8.2절 조건 충족 확인 | □ |

### A.3 판정 기준

| 판정 | 조건 | 후속 조치 |
|---|---|---|
| **PASS** | 공급자는 A.1 전 항목, 소비자는 A.2 전 항목 충족 | 정상 진행 |
| **FAIL** | 하나 이상 미충족 | 유형 A 피드백 신호 발송 후 중단 |

---

## 부속서 B (규범적): 계보 연속성 JSON-LD 예시

> **이 부속서는 규범적(normative)이다.** 10장의 계보 기록 규칙을 구현할 때 이 예시를 준수하여야 한다.

### B.1 교환 트랜잭션 계보 전체 예시

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "aird": "http://data.go.kr/ns/aird#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@graph": [
    {
      "@id": "aird:activity/exchange-20260414-factory-ml-001",
      "@type": ["prov:Activity", "aird:ExchangeActivity"],
      "prov:startedAtTime": {"@value": "2026-04-14T09:00:00+09:00", "@type": "xsd:dateTime"},
      "prov:endedAtTime":   {"@value": "2026-04-14T09:02:15+09:00", "@type": "xsd:dateTime"},
      "prov:wasAssociatedWith": {"@id": "aird:agent/data-portal-go-kr"},
      "aird:consumer": {"@id": "aird:agent/research-institute-xyz"},
      "prov:used": {"@id": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0"},
      "aird:integrityVerified": true,
      "aird:exchangeType": "full",
      "aird:bundleChecksum": "a3f2c1d8e4b7..."
    },
    {
      "@id": "aird:entity/factory-data-ml-pack-v1.0.0-copy-xyz",
      "@type": "prov:Entity",
      "prov:wasDerivedFrom": {"@id": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0"},
      "prov:wasGeneratedBy": {"@id": "aird:activity/exchange-20260414-factory-ml-001"}
    }
  ]
}
```

### B.2 소비자 파생 계보 연결 예시

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "aird": "http://data.go.kr/ns/aird#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "aird:activity/consumer-train-20260414-xyz-001",
  "@type": ["prov:Activity", "aird:ConsumerActivity"],
  "prov:startedAtTime": {"@value": "2026-04-14T10:00:00+09:00", "@type": "xsd:dateTime"},
  "prov:endedAtTime":   {"@value": "2026-04-14T18:00:00+09:00", "@type": "xsd:dateTime"},
  "prov:wasAssociatedWith": {"@id": "aird:agent/research-institute-xyz"},
  "prov:used": {"@id": "aird:entity/factory-data-ml-pack-v1.0.0-copy-xyz"},
  "prov:wasInformedBy": {"@id": "aird:activity/exchange-20260414-factory-ml-001"},
  "prov:generated": {
    "@id": "aird:entity/factory-compliance-model-v1.0",
    "prov:wasDerivedFrom": {"@id": "https://registry.data.go.kr/packs/factory-data-ml-pack-v1.0.0"},
    "aird:trainedOn": "factory-data-ml-pack-v1.0.0"
  },
  "aird:parameters": {
    "consumerAction": "model-training",
    "framework": "PyTorch",
    "frameworkVersion": "2.3.0",
    "epochs": 50,
    "randomSeed": 42
  }
}
```

---

## 부속서 C (참고): 탐색 API 요청·응답 예시

> **이 부속서는 참고(informative)이다.**

### C.1 필터 탐색 요청 예시

```http
GET /api/v1/packs?purposeType=RAG&qualityTierMin=Silver&agentAccessible=true&language=ko&pageSize=10
Accept: application/json
```

### C.2 필터 탐색 응답 예시

```json
{
  "totalCount": 7,
  "page": 1,
  "pageSize": 10,
  "packs": [
    {
      "packURI": "https://registry.data.go.kr/packs/admin-text-rag-pack-v1.0.0",
      "purposeType": "RAG",
      "qualityTier": "Silver",
      "diagnosticMaturity": "DM-2",
      "agentAccessible": true,
      "modelDataCoupling": "derived",
      "packStatus": "Active",
      "profileStatus": "Candidate",
      "sourceDataVersion": "1.0.0",
      "language": "ko",
      "purposeReadinessVector": { "RAG": "Silver" },
      "feedbackHistory": [],
      "downloadURL": "https://registry.data.go.kr/packs/admin-text-rag-pack-v1.0.0.tar.gz",
      "metadataOnlyURL": "https://registry.data.go.kr/packs/admin-text-rag-pack-v1.0.0/metadata"
    }
  ]
}
```

### C.3 피드백 신호 발송 요청 예시

```http
POST /api/v1/packs/factory-data-ml-pack-v1.0.0/feedback
Content-Type: application/json

{
  "signalType": "A",
  "consumer": "aird:agent/research-institute-xyz",
  "detectedAt": "2026-04-14T14:30:00+09:00",
  "description": "manifest.json의 SHA-256이 data/train.csv와 불일치",
  "evidence": {
    "file": "data/train.csv",
    "expectedChecksum": "a3f2c1d8e4b7...",
    "actualChecksum": "b9e4d7f2c1a3..."
  }
}
```

### C.4 피드백 수신 응답 예시

```http
HTTP/1.1 202 Accepted
Content-Type: application/json

{
  "signalId": "aird:signal/20260414-factory-ml-a-001",
  "status": "received",
  "message": "피드백이 접수되었습니다. 파이프라인 운영자 검토 후 조치됩니다.",
  "estimatedResponseTime": "2026-04-15T09:00:00+09:00"
}
```

---

## 부속서 D (참고): 에이전트 소비 시나리오

> **이 부속서는 참고(informative)이다.**

### D.1 시나리오 1: RAG 파이프라인 에이전트의 자율 데이터 소비

**상황:** 행정 규정 질의응답 시스템의 RAG 에이전트가 최신 Pack을 탐색하여 인덱스를 자동 갱신하는 시나리오.

```
① 에이전트: 레지스트리 탐색
   GET /api/v1/packs?purposeType=RAG&qualityTierMin=Silver&agentAccessible=true&language=ko
   → 3개의 Active Pack 반환

② 에이전트: 메타데이터-only 수신 (3개 Pack 평가)
   - Pack A: Q-Silver, DM-2, RAG Tier=Silver, 편향성 없음 → 선택
   - Pack B: Q-Bronze → bronzeUsageNote 있음, 고위험 용도 부적합 → 제외
   - Pack C: Stale → 제외

③ 에이전트: Pack A 완전 수신
   GET https://registry.data.go.kr/packs/admin-text-rag-pack-v1.0.0.tar.gz

④ 에이전트: SHA-256 검증 → 통과

⑤ 에이전트: chunks.jsonl + vectors.bin → FAISS 인덱스 마운트

⑥ 에이전트: 소비 기록 (aird:ConsumerActivity) 생성
   prov:wasDerivedFrom → admin-text-rag-pack-v1.0.0 URI
```

### D.2 시나리오 2: 유형 A 피드백 자동 발송

**상황:** 에이전트가 Pack 수신 후 무결성 검증에 실패하는 시나리오.

```
① 에이전트: Pack 수신 및 SHA-256 검증 실행
② 검증 실패: data/chunks.jsonl 체크섬 불일치 감지
③ 에이전트: 소비 즉시 중단 (Pack 사용 금지)
④ 에이전트: 유형 A 피드백 신호 자동 발송
   POST /api/v1/packs/{pack-id}/feedback
   {signalType: "A", evidence: {file: "data/chunks.jsonl", ...}}
⑤ 레지스트리: signalPending: true 표시
⑥ 에이전트: 다른 Pack 탐색 또는 사람 에스컬레이션
```

---

## 부속서 E (참고): 표준 간 참조 매트릭스

> **이 부속서는 참고(informative)이다.**

### E.1 AIRD-STD-005 → AIRD-STD-003 참조

| 본 표준 절 | AIRD-STD-003 참조 절 | 참조 내용 |
|---|---|---|
| 3장 (용어) | 3.10절, 7.4절 | AIRD Pack 정의 및 구조 |
| 5.2절 (교환 포맷) | 7.4절 (manifest.json 구조) | Pack 필수 파일 목록 |
| 5.3절 (메타데이터-only) | 7.4절 (metadata.json) | 메타데이터 파일 정의 |
| 6.3절 (레지스트리 색인) | 7.4절 (manifest.json 필드) | 색인 대상 필드 출처 |
| 8.2절 (에이전트 조건) | 3.12절, 10.4절 | 소비자 피드백 루프 정의 |
| 9장 (피드백 API) | 10.4절 | 피드백 신호 유형 A/B/C 정의 |
| 10장 (계보 연속성) | 8장 (Provenance 규격) | 원본 계보 기록 규격 |
| 11.3절 (DM-1 차단) | 10.1절 (c) | DM-1 공식 공시 차단 규칙 |

### E.2 AIRD-STD-005 → AIRD-STD-002 참조

| 본 표준 절 | AIRD-STD-002 참조 절 | 참조 내용 |
|---|---|---|
| 6.3절 (레지스트리 색인) | 4.4절 (purposeReadinessVector) | 탐색 필터 조건 |
| 7.4절 (DCAT 연계) | 3장 (Layer 1 Discovery) | DCAT 카탈로그 어휘 |
| 11.2절 (이용 조건) | 3.4절 (권리·이용 메타데이터) | 이용 조건 필드 출처 |

### E.3 AIRD-STD-005 → AIRD-STD-004 참조 (AIRD-STD-004 제정 후)

| 본 표준 절 | AIRD-STD-004 참조 절 (예정) | 참조 내용 |
|---|---|---|
| 6.4절 (등록 절차 ③) | 인증 상태 확인 절차 | 인증 마크 유무 확인 |
| 7.2.1절 (탐색 필터) | 인증 수준 정의 | `certificationLevel` 필터 값 범위 |
| 12.2절 (적합성 매핑) | AIRD-STD-004 적합성 수준 | Level A/B/C 매핑 |

---

## 부속서 F (참고): 구현 기술 스택 가이드

> **이 부속서는 참고(informative)이다.** 특정 기술 스택을 규범적으로 요구하지 않으며, 구현 참고 목적으로만 제공한다. 기술 환경 변화에 따라 이 부속서는 독립적으로 개정될 수 있다.

### F.1 탐색 API 구현 기술

| 구현 방식 | 적용 적합성 | 비고 |
|---|---|---|
| REST API (OpenAPI 3.1) | 높음 | 범용성 최고. 공공데이터 포털 연계 용이 |
| GraphQL | 중간 | 복잡한 계보 탐색 쿼리에 유리 |
| SPARQL (RDF) | 중간 | DCAT·PROV-O 연계 시 자연스러운 선택 |
| OAI-PMH | 낮음 | 레거시 카탈로그 연동 시 한시적 활용 |

### F.2 에이전트 인터페이스 구현 기술

| 구현 방식 | 적용 적합성 | 비고 |
|---|---|---|
| MCP (Model Context Protocol) | 높음 | AI 에이전트의 도구 호출 표준으로 확산 중 |
| A2A (Agent-to-Agent) | 높음 | 에이전트 간 직접 통신. 멀티에이전트 시나리오에 적합 |
| REST API (agentAccessible 엔드포인트) | 중간 | 단순하고 범용적. 현 단계 최소 구현에 적합 |

### F.3 레지스트리 스토리지 구현

| 스토리지 유형 | 적용 적합성 | 비고 |
|---|---|---|
| CKAN 기반 | 높음 | 공공데이터포털 현행 시스템. DCAT 플러그인 지원 |
| Triple Store (RDF) | 중간 | PROV-O·DCAT 네이티브 지원. 계보 탐색에 강점 |
| 관계형 DB + 검색 엔진 | 높음 | 필터 탐색 성능 우수. 범용적 구현 가능 |

*— 끝 —*
