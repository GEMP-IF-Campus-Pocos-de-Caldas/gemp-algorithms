# Repository Overview

GEMP Algorithms is a community algorithm collection maintained by **GEMP-IF**
(Grupo de Estudos em Métodos de Programação) at **IFSULDEMINAS — Campus Poços
de Caldas**.

The repository has a **hybrid role**:

- didactic study material for GEMP-IF members;
- a reusable library for other projects.

The audience is GEMP-IF members and the external community. This document is the
conduct guide for every AI agent that works in this repository. It is written in
English; the rest of the repository follows the language matrix in
`# Code Standards`.

Four languages are official:

- **Python**
- **C**
- **Java**
- **C++**

A language outside this list requires approval and an update to the spec and to
this guide.

# Repository Layout

The domain sits at the top. The repository root contains one directory per
official category (12 categories), plus reserved directories:

```text
gemp-algorithms/
├── ordenacao/
├── busca/
├── estruturas-de-dados/
├── grafos/
├── matematica/
├── strings/
├── dinamica/
├── geometria/
├── competicao/
├── ml/
├── geneticos/
├── robotica/
├── docs/
├── scripts/
├── .github/
├── .clang-format
├── .gitignore
├── pyproject.toml
├── Agents.md
├── README.md
└── LICENSE
```

The category list is **closed**: `ordenacao`, `busca`, `estruturas-de-dados`,
`grafos`, `matematica`, `strings`, `dinamica`, `geometria`, `competicao`, `ml`,
`geneticos`, `robotica`. `scripts/validate.py` rejects any top-level directory
outside it (and outside the reserved set `docs`, `scripts`, `.git`, `.github`).

Each algorithm lives in a **leaf** with the layout
`category/algorithm/<language>/`, with one subdirectory per language:

```text
grafos/
└── dijkstra/
    ├── README.md
    ├── c/dijkstra.c
    ├── c/test_dijkstra.c
    ├── cpp/dijkstra.cpp
    ├── cpp/test_dijkstra.cpp
    ├── python/dijkstra.py
    ├── python/test_dijkstra.py
    └── java/Dijkstra.java
```

Rules for the leaf:

- every leaf has a mandatory `README.md`;
- the leaf directory name is kebab-case and free of accents and spaces;
- tests live next to the code, inside the language directory.

# Naming Conventions

- Domain and folder names: **kebab-case** in Portuguese, no accent, no space
  (e.g. `estruturas-de-dados`, `busca-binaria`).
- A code file is named after the algorithm using the language convention.
- Java is the only exception: the file name must match the public class exactly,
  so it uses **PascalCase** (e.g. `Dijkstra.java`, `TestDijkstra.java`).

| Language | Code file | Test file |
|---|---|---|
| C / C++ (`.c`, `.cpp`) | `kebab-case.ext` (e.g. `dijkstra.cpp`) | `test_<algorithm>.<ext>` (e.g. `test_dijkstra.cpp`) |
| Python (`.py`) | `kebab-case.py` (e.g. `dijkstra.py`) | `test_<algorithm>.py` |
| Java (`.java`) | `PascalCase.java` (e.g. `Dijkstra.java`) | `Test<Algorithm>.java` (e.g. `TestDijkstra.java`) |

# Code Standards

## Language matrix

| Element | Language |
|---|---|
| `Agents.md` | English |
| `docs/`, READMEs, spec | Portuguese |
| Metadata header and code comments | Portuguese |
| Code identifiers | English |

## Mandatory metadata header

Every code file starts with a comment block in the language's syntax, holding
the fields below in `Key: Value` form, one per line. A list marker is optional
(both `- Nome: ...` and `Nome: ...` are accepted).

| Field | Required | Value |
|---|---|---|
| `Nome` | yes | algorithm name |
| `Categoria` | yes | domain |
| `Descrição` | yes | what it solves, 1–2 lines |
| `Complexidade` | yes | `O(...)` time, `O(...)` space |
| `Autor` | yes | author name |
| `Data` | yes | `YYYY-MM-DD` |
| `Uso/Referência` | optional | link or source problem |

Block style per language:

- C / C++ / Java: a `/* ... */` block at the top of the file;
- Python: `#` comment lines at the top of the file. The Python header does
  **not** use a `"""` docstring, so `scripts/validate.py` can parse it with a
  simple regex instead of an AST.

Example (C++):

```cpp
/*
 * Nome: Dijkstra
 * Categoria: grafos
 * Descrição: Caminho mínimo de fonte única em grafo com pesos não-negativos.
 * Complexidade: O((V+E) log V) tempo, O(V) espaço.
 * Autor: Nome Sobrenome
 * Data: 2026-10-12
 * Uso/Referência: https://... (opcional)
 */
```

Example (Python):

```python
# Nome: Dijkstra
# Categoria: grafos
# Descrição: Caminho mínimo de fonte única em grafo com pesos não-negativos.
# Complexidade: O((V+E) log V) tempo, O(V) espaço.
# Autor: Nome Sobrenome
# Data: 2026-10-12
```

Additional rules:

- Big-O complexity is mandatory when applicable;
- identifiers in English; comments and header in Portuguese;
- no dead code; no `print`/debug log outside an example block;
- reusable code isolated in pure functions where possible;
- formatting guaranteed by the standard formatter (see `# Testing and CI`).

Formatters:

| Language | Formatter | Config |
|---|---|---|
| C / C++ | `clang-format` | `.clang-format` |
| Python | `black` | `pyproject.toml` |
| Java | `google-java-format` | defaults |

# Testing and CI

A test is **mandatory when there is real reuse**:

- code meant to be imported or used by another project (library);
- every new category — the first algorithm defines that category's test pattern.

Isolated didactic code and competition snippets may skip tests. When no test
exists, the leaf `README.md` must declare the marker in its own line:

```markdown
**Status de teste:** sem verificação
```

`scripts/validate.py` looks for the substring `sem verificação` in the leaf
README to allow the missing test file.

Convention:

- tests live next to the code, inside the language directory, named
  `test_<algorithm>.<ext>` (Java: `Test<Algorithm>.java`);
- cases are input/expected-output pairs; include the original problem case when
  one exists.

## Local commands

```bash
python scripts/validate.py   # structure, names, header, README, test checks
bash scripts/lint.sh         # formatting gate
```

Tests per language:

```bash
pytest -q                                   # Python
gcc -std=c11 -Wall -Wextra test_x.c -o /tmp/test_x && /tmp/test_x      # C
g++ -std=c++17 -Wall -Wextra test_x.cpp -o /tmp/test_x && /tmp/test_x  # C++
javac -d /tmp/classes java/*.java && java -cp /tmp/classes TestX       # Java
```

## CI (GitHub Actions)

`.github/workflows/ci.yml` runs on **pull request** and on **push to main**, in
three jobs:

1. **python** — `python scripts/validate.py`, `pytest -q`, `bash scripts/lint.sh`
   (black).
2. **c-cpp** — compiles and runs C and C++ tests, `python3 scripts/validate.py`,
   `bash scripts/lint.sh` (clang-format).
3. **java** — compiles and runs Java tests, `python3 scripts/validate.py`,
   `bash scripts/lint.sh` (google-java-format).

Compiled tests (C, C++, Java) are **executed**, not only compiled. Any failing
step makes the PR red. Tool versions are pinned in the workflow so local and
remote formatting checks agree.

# Git Workflow

- **Conventional Commits** with scope = category, e.g.
  `feat(grafos): adiciona dijkstra em cpp`.
- Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`, `perf`.
- Branch: `<type>/<category>-<algorithm>`, e.g. `feat/grafos-dijkstra`,
  `fix/busca-binaria`.
- **Never commit directly to `main`**; always open a pull request.
- PR title in Conventional Commits; the description states the problem solved,
  the category, the languages, and the pre-PR checklist.
- Review: 1 approval from a GEMP-IF member. No per-file CODEOWNERS.
- Commits are small and atomic; one algorithm per PR when possible.

# Agent Scope and Autonomy

The central rule is **strict scope**.

- An agent only creates or edits the files and folders the task explicitly
  authorizes or clearly implies. Scope is **inferred from the prompt**.
- Production is **independent**: each algorithm does not depend on editing
  another. Correcting, moving, or refactoring a file outside scope is forbidden.
- If work needs a file outside scope, **stop and ask for authorization**. Never
  "fix it along the way".
- When in doubt about scope, ask; do not assume.
- Before creating a new file outside the authorized paths, ask.
- Forbidden: pushing directly to `main`, rewriting history, deleting third-party
  authorship, and altering CI, `Agents.md`, or `scripts/` outside an explicit
  task.
- **Never dispatch subagents** unless the task explicitly instructs it; do the
  work yourself.

# Implementation Rules

- Only use the standard library of each language (C++ STL, Java JDK/`java.util`, Python/C stdlib). External dependencies (e.g. numpy, boost) are forbidden unless the task explicitly authorizes them.
- Never remove, reorder, or reformat the metadata header when fixing code or applying a linter. The header only changes in a task that explicitly edits it.
- Do not leave debug output (`print`, `std::cout`, `System.out.println`) inside the algorithm's main functions. Debug output belongs only to example or test blocks/files.

# Security and License

- **No secrets** in the repository: keys, tokens, `.env`, credentials.
- License: **MIT** (see `LICENSE`). Every algorithm is under MIT unless the file
  states otherwise explicitly.
- Attribution: the `Autor` header field. Material adapted from an external
  source cites the origin in `Uso/Referência`.
- Copying proprietary code or code without a compatible license is forbidden.
- Third-party dependencies record their origin and a license compatible with
  MIT.

# Recipes

## Add an algorithm

1. Confirm the authorized category and name (otherwise, ask).
2. Create the leaf `category/algorithm/<language>/`.
3. Fill the mandatory header (Portuguese).
4. Create the leaf `README.md`.
5. Create a test if there is real reuse; otherwise mark `sem verificação`.
6. Run `python scripts/validate.py` and `bash scripts/lint.sh`.
7. Commit with Conventional Commits, on its own branch, and open a PR.

## Fix a bug

- Fix only in the files cited by or related to the task.
- If the root cause is outside scope, **report it**, do not fix it.

## Pre-PR checklist

- [ ] header complete and in Portuguese;
- [ ] complexity documented;
- [ ] standard library only (no external dependency);
- [ ] header preserved (not removed or reformatted);
- [ ] neutral output (no debug in the main functions);
- [ ] test present or `sem verificação` marker;
- [ ] `scripts/validate.py` green;
- [ ] `scripts/lint.sh` green;
- [ ] no secret committed;
- [ ] one algorithm per PR.
