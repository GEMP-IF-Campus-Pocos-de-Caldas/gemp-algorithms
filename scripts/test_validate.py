from pathlib import Path

import validate


def _mk_leaf(root: Path, category: str, algo: str, lang: str, filename: str, content: str) -> Path:
    d = root / category / algo / lang
    d.mkdir(parents=True)
    (root / category / algo / "README.md").write_text("# " + algo, encoding="utf-8")
    f = d / filename
    f.write_text(content, encoding="utf-8")
    return f


GOOD_HEADER = (
    "// Nome: Dijkstra\n"
    "// Categoria: grafos\n"
    "// Descrição: caminho mínimo.\n"
    "// Complexidade: O(E log V) tempo, O(V) espaço.\n"
    "// Autor: Fulano\n"
    "// Data: 2026-10-12\n"
)


def test_unknown_category_is_rejected(tmp_path):
    (tmp_path / "temp").mkdir()
    errors = validate.validate_repo(tmp_path)
    assert any("temp" in e for e in errors)


def test_leaf_dir_must_be_kebab(tmp_path):
    _mk_leaf(tmp_path, "grafos", "Dijkstra", "cpp", "dijkstra.cpp", GOOD_HEADER)
    errors = validate.validate_repo(tmp_path)
    assert any("Dijkstra" in e for e in errors)


def test_java_pascalcase_file_is_allowed(tmp_path):
    _mk_leaf(tmp_path, "grafos", "dijkstra", "java", "Dijkstra.java", GOOD_HEADER)
    (tmp_path / "grafos" / "dijkstra" / "java" / "TestDijkstra.java").write_text(
        GOOD_HEADER, encoding="utf-8"
    )
    assert validate.validate_repo(tmp_path) == []


def test_missing_header_is_reported(tmp_path):
    _mk_leaf(tmp_path, "grafos", "dijkstra", "cpp", "dijkstra.cpp", "int main(){return 0;}\n")
    (tmp_path / "grafos" / "dijkstra" / "cpp" / "test_dijkstra.cpp").write_text(
        GOOD_HEADER, encoding="utf-8"
    )
    errors = validate.validate_repo(tmp_path)
    assert errors and all("dijkstra.cpp" in e for e in errors)


def test_bad_date_format_is_reported(tmp_path):
    content = GOOD_HEADER.replace("2026-10-12", "12/10/2026")
    _mk_leaf(tmp_path, "grafos", "dijkstra", "cpp", "dijkstra.cpp", content)
    errors = validate.validate_repo(tmp_path)
    assert any("Data" in e for e in errors)


def test_is_kebab():
    assert validate.is_kebab("estruturas-de-dados")
    assert not validate.is_kebab("Dijkstra")
    assert not validate.is_kebab("ordenacao ")


def test_missing_test_is_reported(tmp_path):
    _mk_leaf(tmp_path, "grafos", "dijkstra", "cpp", "dijkstra.cpp", GOOD_HEADER)
    errors = validate.validate_repo(tmp_path)
    assert any("test_" in e for e in errors)


def test_sem_verificacao_allows_missing_test(tmp_path):
    _mk_leaf(tmp_path, "grafos", "dijkstra", "cpp", "dijkstra.cpp", GOOD_HEADER)
    (tmp_path / "grafos" / "dijkstra" / "README.md").write_text(
        "**Status de teste:** sem verificação", encoding="utf-8"
    )
    assert validate.validate_repo(tmp_path) == []


def test_present_test_passes(tmp_path):
    _mk_leaf(tmp_path, "grafos", "dijkstra", "cpp", "dijkstra.cpp", GOOD_HEADER)
    (tmp_path / "grafos" / "dijkstra" / "cpp" / "test_dijkstra.cpp").write_text(
        GOOD_HEADER, encoding="utf-8"
    )
    assert validate.validate_repo(tmp_path) == []


def test_to_pascal_and_java_test_filename():
    assert validate.to_pascal("busca-binaria") == "BuscaBinaria"
    assert validate.test_filename("java", "busca-binaria") == "TestBuscaBinaria.java"
    assert validate.test_filename("python", "busca-binaria") == "test_busca-binaria.py"
