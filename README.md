# aird-tools

AI-Ready Data 표준 기반의 공공데이터 메타데이터 변환 도구

## 배경

공공데이터 품질 관리는 주로 기관 내부 데이터베이스 중심으로 이루어져 왔습니다. 그러나 시민과 AI가 실제로 사용하는 것은 개방된 데이터이며, 내부 DB 품질과 개방 데이터 품질 사이에는 구조적인 간극이 존재합니다. 인력, 예산, 도구가 충분하지 않은 환경에서 개방 데이터까지 동시에 고도화하는 것은 쉽지 않기 때문입니다.

이 프로젝트는 이러한 간극을 줄이기 위해, 단순한 품질 진단을 넘어 **데이터 개선과 AI 활용 구조까지 직접 연결**하는 접근을 시도합니다. 진단 결과를 제공하는 데서 끝나는 것이 아니라, 메타데이터 강화, 데이터 구조 정비, 표준화 과정을 거쳐 AI가 바로 활용할 수 있는 형태로 전환하는 것이 목표입니다.

```
품질개선 항목선정          Quality-Ready             Purpose-Ready (활용 예시)
┌─────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│ 메타데이터 강화     │   │ 고품질 데이터 생성   │   │ ML/DL  질의응답    │
│ 데이터값 구조 정합성  │ → │ 품질지표 메타데이터  │ → │ 지식그래프  LLM    │
│ 참조/코드체계 정비   │   │ 활용 목적별 변환    │   │ 검색·추천 에이전트  │
└─────────────────┘   └──────────────────┘   └──────────────────┘
```

## AI-Ready Data 표준

한국정보통신기술협회(TTA)에서 2026년 제정을 목표로 3개의 AI-Ready Data 표준을 개발 중입니다.

| 표준 | 명칭 | 범위 |
|------|------|------|
| Part 1 | AI-Ready 데이터 품질 진단 프레임워크 | 품질 차원(완전성, 일관성, 정확성, 적시성, 유효성, 유일성 등)을 정량 공식으로 전환하여, 비교 가능한 단일 척도와 자동화 가능한 등급 판정 체계 |
| Part 2 | AI-Ready 데이터 메타데이터 프로파일 | 메타데이터를 3계층(Discovery, Understanding, Operability)으로 구조화하고, ML/RAG/KG/Stats 등 목적별 프로파일 스키마를 국제 표준 어휘 기반으로 정의 |
| Part 3 | AI-Ready 데이터 변환 및 거버넌스 규격 | Raw 데이터를 Quality-Ready를 거쳐 Purpose-Ready 상태로 전환하는 3단계 파이프라인의 실행 절차, 품질 게이트 판정 기준, 데이터 계보 기록 방식, 확장 프로파일 등록 거버넌스 |

표준 초안은 확정되는 대로 공개하여 커뮤니티 의견을 수렴할 예정입니다.

## 도구

표준 확정 전이라도 활용 가능한 도구를 먼저 오픈소스로 제공하고, 표준이 완성되면 업데이트합니다.

| 도구 | 관련 표준 | 설명 | 상태 |
|------|----------|------|------|
| [catalog-converter](tools/catalog-converter/) | Part 2 | 공공데이터포털 목록개방현황 CSV → DCAT 기반 RDF(JSON-LD, Turtle, N-Triples) 변환 | v0.1 |
| quality-evaluator | Part 1 | 품질 차원별 정량 진단 및 등급 판정 | 계획 |
| metadata-validator | Part 2 | SHACL 기반 메타데이터 프로파일 검증 | 계획 |
| transform-pipeline | Part 3 | Raw → Quality-Ready → Purpose-Ready 변환 파이프라인 (ML/RAG/KG/Stats 목적별) | 계획 |

## 프로젝트 구조

```
aird-tools/
├── shared/                  # 공통 네임스페이스, 어휘 정의
├── tools/
│   └── catalog-converter/   # 카탈로그 변환기
│       ├── src/             #   변환 코드
│       ├── data/            #   원본 데이터
│       ├── docs/            #   매핑 명세, 정제 계획
│       └── examples/        #   샘플 출력
└── (향후 추가 도구)
```

## 네임스페이스

| Prefix | URI | 용도 |
|--------|-----|------|
| `aird` | `http://datahub.kr/ns/aird#` | AI-Ready Data 커스텀 어휘 |
| `dcat` | `http://www.w3.org/ns/dcat#` | 데이터 카탈로그 |
| `dct` | `http://purl.org/dc/terms/` | 메타데이터 속성 |

전체 어휘 목록은 [`shared/namespaces.py`](shared/namespaces.py) 참조.

## 데이터 출처

이 프로젝트에서 사용하는 데이터는 공공데이터포털에서 제공하는 공개 데이터입니다.

- **데이터명**: 공공데이터활용지원센터_공공데이터포털 목록개방현황
- **출처**: https://www.data.go.kr/data/15062804/fileData.do
- **이용조건**: 공공누리(KOGL)

원본 CSV 파일(126MB)은 저장소에 포함되어 있지 않습니다. 위 링크에서 직접 다운로드하여 `tools/catalog-converter/data/` 디렉터리에 배치하세요.

## 참여

이슈와 PR을 환영합니다. 현재는 catalog-converter 관련 이슈(매핑 오류, 누락 필드, 정제 개선 등)를 우선 수렴하고 있습니다. 매핑 명세는 [tools/catalog-converter/docs/](tools/catalog-converter/docs/)에서 확인할 수 있습니다.

표준 초안이 공개되면 상세 기여 가이드와 함께 의견 수렴 채널(GitHub Discussions)을 열 예정입니다.
