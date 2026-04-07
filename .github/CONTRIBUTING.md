# 기여 가이드

이 프로젝트는 AI 활용에 적합한 공공데이터 표준(AIRD)을 개발하고 참조 구현을 제공하는 오픈소스 프로젝트입니다.

## 기여할 수 있는 영역

| 영역 | 설명 |
|------|------|
| **표준 피드백** | AIRD 스펙(Part 1/2/3) 내용에 대한 의견 |
| **버그 수정** | 참조 구현(catalog-converter 등) 버그 수정 |
| **기능 개선** | 기존 도구의 기능 추가 또는 개선 |
| **새 도구** | AIRD 표준을 구현하는 새로운 도구 기여 |
| **문서** | README, 매핑 스펙, 사용 가이드 개선 |

## 기여 전에 먼저 논의해주세요

코드나 문서를 바로 PR로 올리기 전에, **Issue 또는 Discussion에서 먼저 논의**하는 것을 권장합니다.
특히 아래의 경우는 사전 논의가 필요합니다:

- 표준 스펙 내용 변경
- 새로운 도구 추가
- 기존 도구의 인터페이스 변경

## 기여 워크플로우

```
1. 이 레포지토리를 Fork합니다
2. 기능/수정 단위의 브랜치를 생성합니다
   git checkout -b fix/catalog-converter-null-handling
3. 변경 후 커밋합니다
4. Fork한 레포지토리에 Push합니다
5. 원본 레포지토리로 Pull Request를 엽니다
```

## 로컬 개발 환경 세팅

```bash
# 레포지토리 클론
git clone https://github.com/hike-lab/aird-tools.git
cd aird-tools

# 의존성 설치 (catalog-converter 기준)
pip install -r tools/catalog-converter/requirements.txt
```

> **참고:** `data/` 폴더는 git에서 제외되어 있습니다.
> 공공데이터 포털에서 원본 데이터를 별도로 다운로드해야 합니다.
> 자세한 내용은 [`tools/catalog-converter/README.md`](../tools/catalog-converter/README.md)를 참고하세요.

## 코드 스타일

- Python: [PEP 8](https://peps.python.org/pep-0008/) 준수
- RDF 네임스페이스 및 URI 정의는 `shared/namespaces.py` 활용
- 커밋 메시지: `fix:`, `feat:`, `docs:`, `spec:` 등 [Conventional Commits](https://www.conventionalcommits.org/) 권장

## 도메인 배경 자료

AIRD Tools는 W3C Linked Data 표준을 기반으로 합니다. 아래 자료가 도움이 될 수 있습니다:

- [DCAT (Data Catalog Vocabulary)](https://www.w3.org/TR/vocab-dcat-3/)
- [RDF 1.1 Primer](https://www.w3.org/TR/rdf11-primer/)
- [공공데이터 포털](https://www.data.go.kr)
- [한국정보통신기술협회 (TTA)](https://www.tta.or.kr)
