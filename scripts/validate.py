"""Validador de estrutura e cabeçalhos de metadados do repositório GEMP Algorithms."""

from __future__ import annotations

import re
import sys
from pathlib import Path

OFFICIAL_CATEGORIES: list[str] = [
    "ordenacao",
    "busca",
    "estruturas-de-dados",
    "grafos",
    "matematica",
    "strings",
    "dinamica",
    "geometria",
    "competicao",
    "ml",
    "geneticos",
    "robotica",
]

LANGUAGE_DIRS: dict[str, str] = {
    "c": ".c",
    "cpp": ".cpp",
    "python": ".py",
    "java": ".java",
}

REQUIRED_HEADER_KEYS: list[str] = [
    "Nome",
    "Categoria",
    "Descrição",
    "Complexidade",
    "Autor",
    "Data",
]

RESERVED_DIRS: set[str] = {"docs", "scripts", ".git", ".github"}

_KEBAB_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")

_HEADER_RE = re.compile(
    r"^\s*[-*]?\s*(Nome|Categoria|Descrição|Complexidade|Autor|Data|Uso/Referência):\s*(.+)$"
)

_COMMENT_PREFIX_RE = re.compile(r"^\s*(?://+|#+|\*+|/\*+)\s*")

_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def is_kebab(name: str) -> bool:
    return bool(_KEBAB_RE.fullmatch(name))


def to_pascal(name: str) -> str:
    return "".join(part.capitalize() for part in name.split("-"))


def test_filename(lang: str, algorithm: str) -> str:
    if lang == "java":
        return f"Test{to_pascal(algorithm)}.java"
    if lang == "cpp":
        return f"test_{algorithm}.cpp"
    if lang == "c":
        return f"test_{algorithm}.c"
    if lang == "python":
        return f"test_{algorithm}.py"
    raise ValueError(f"linguagem desconhecida: {lang}")


def has_sem_verificacao(readme_text: str) -> bool:
    return "sem verificação" in readme_text


def _find_header_fields_with_lines(text: str) -> tuple[dict[str, str], dict[str, int]]:
    fields: dict[str, str] = {}
    lines: dict[str, int] = {}
    for number, line in enumerate(text.splitlines()[:30], start=1):
        match = _HEADER_RE.match(_COMMENT_PREFIX_RE.sub("", line))
        if match:
            key, value = match.group(1), match.group(2).strip()
            fields[key] = value
            lines[key] = number
    return fields, lines


def find_header_fields(text: str) -> dict[str, str]:
    fields, _ = _find_header_fields_with_lines(text)
    return fields


def _validate_code_file(root: Path, path: Path) -> list[str]:
    errors: list[str] = []
    relpath = path.relative_to(root)
    text = path.read_text(encoding="utf-8")
    fields, lines = _find_header_fields_with_lines(text)
    first_line = min(lines.values()) if lines else 1
    for key in REQUIRED_HEADER_KEYS:
        if key not in fields:
            errors.append(f"{relpath}:{first_line}: campo ausente: {key}")
    data = fields.get("Data")
    if data is not None and not _DATE_RE.fullmatch(data):
        errors.append(f"{relpath}:{lines['Data']}: Data fora do formato AAAA-MM-DD: {data}")
    return errors


def validate_repo(root: Path) -> list[str]:
    errors: list[str] = []
    for entry in sorted(root.iterdir()):
        if entry.name.startswith("."):
            continue
        if not entry.is_dir():
            continue
        if entry.name in RESERVED_DIRS:
            continue
        if entry.name not in OFFICIAL_CATEGORIES:
            errors.append(f"{entry.name}: categoria não oficial")
            continue
        for leaf in sorted(entry.iterdir()):
            if leaf.name.startswith("."):
                continue
            if not leaf.is_dir():
                continue
            relleaf = leaf.relative_to(root)
            if not is_kebab(leaf.name):
                errors.append(f"{relleaf}: folha deve ser kebab-case")
            readme = leaf / "README.md"
            if not readme.is_file():
                errors.append(f"{relleaf}: README.md ausente")
                readme_text = ""
            else:
                readme_text = readme.read_text(encoding="utf-8")
            for lang, ext in LANGUAGE_DIRS.items():
                lang_dir = leaf / lang
                if not lang_dir.is_dir():
                    continue
                for path in sorted(lang_dir.iterdir()):
                    if not path.is_file():
                        continue
                    if path.suffix != ext:
                        continue
                    if path.name.startswith("test_") or path.name.startswith("Test"):
                        continue
                    errors.extend(_validate_code_file(root, path))
                if not has_sem_verificacao(readme_text):
                    expected = test_filename(lang, leaf.name)
                    if not (lang_dir / expected).is_file():
                        errors.append(f"{lang_dir.relative_to(root)}: teste ausente: {expected}")
    return errors


def main(argv: list[str] | None = None) -> int:
    root = Path(argv[0]) if argv else repo_root()
    errors = validate_repo(root)
    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
