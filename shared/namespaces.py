"""
AI-Ready Data 공통 네임스페이스 정의

모든 도구에서 import 하여 사용한다.
네임스페이스 URI 변경 시 이 파일만 수정하면 전체 반영됨.
"""

from rdflib import Namespace
from rdflib.namespace import RDF, RDFS, XSD, DCTERMS, FOAF, SKOS

# AI-Ready Data 커스텀 어휘
AIRD = Namespace("http://datahub.kr/ns/aird#")

# 표준 어휘
DCAT = Namespace("http://www.w3.org/ns/dcat#")
VCARD = Namespace("http://www.w3.org/2006/vcard/ns#")
SCHEMA = Namespace("http://schema.org/")
ADMS = Namespace("http://www.w3.org/ns/adms#")
DQV = Namespace("http://www.w3.org/ns/dqv#")

# 공공데이터포털 리소스 URI 베이스 (실제 포털 주소)
DATA_GO_KR = "https://data.go.kr"


def bind_common_prefixes(graph):
    """RDF 그래프에 공통 prefix를 바인딩한다."""
    graph.bind("aird", AIRD)
    graph.bind("dcat", DCAT)
    graph.bind("dct", DCTERMS)
    graph.bind("vcard", VCARD)
    graph.bind("foaf", FOAF)
    graph.bind("schema", SCHEMA)
    graph.bind("adms", ADMS)
    graph.bind("dqv", DQV)
    graph.bind("skos", SKOS)
    return graph
