# 🧮 GEMP Algorithms

> Repositório acadêmico dedicado ao estudo e à implementação de algoritmos.

**GEMP-IF · IFSULDEMINAS**

---

## 📖 Sobre

O **GEMP Algorithms** é um projeto desenvolvido pelo **GEMP-IF — Grupo de Estudos em Métodos de Programação**, do Instituto Federal de Educação, Ciência e Tecnologia do Sul de Minas Gerais — Campus Poços de Caldas.

Este repositório reúne implementações de algoritmos estudados e desenvolvidos no contexto acadêmico, proporcionando um espaço organizado para consulta, estudo e compartilhamento de conhecimento em programação e resolução de problemas computacionais.

Os conteúdos são desenvolvidos de forma progressiva, acompanhando os diferentes conceitos e técnicas abordados ao longo da formação acadêmica.

---

## 🎯 Objetivos

- 📚 Manter um acervo organizado das implementações desenvolvidas pelos integrantes do GEMP-IF;
- 🔍 Registrar e catalogar os algoritmos estudados nas atividades do grupo;
- 🧠 Servir como material de apoio ao aprendizado e à revisão de conteúdo;
- 🤝 Estimular a colaboração entre integrantes e a prática de versionamento de código.

---

## 🗂️ Organização do repositório

O repositório é organizado por categorias de algoritmos:

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
├── Agents.md
├── README.md
└── LICENSE
```

Cada algoritmo fica em uma folha com a convenção
`categoria/algoritmo/<linguagem>/`, com uma subpasta por linguagem oficial
(Python, C, Java, C++):

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

Cada implementação deve conter, em comentários no próprio código, o header de
metadados obrigatório:

- **Nome**;
- **Categoria**;
- **Descrição**;
- **Complexidade**;
- **Autor**;
- **Data** (formato `AAAA-MM-DD`).

Quando o algoritmo ainda não tiver verificação automatizada, o `README.md` da
folha deve declarar explicitamente o marcador:

```markdown
**Status de teste:** sem verificação
```

---

## 💻 Tecnologias

**Linguagens utilizadas:**

- Python
- C
- Java
- C++

> A lista de linguagens será atualizada conforme novas implementações forem adicionadas ao repositório.

---

## 🤝 Como contribuir

Contribuições dos integrantes do GEMP-IF são sempre bem-vindas!

Siga os passos abaixo:

### 1. Faça um fork do repositório ou clone-o

```bash
git clone https://github.com/[usuario]/gemp-algorithms.git
```

### 2. Crie uma branch para sua contribuição

```bash
git checkout -b meu-algoritmo
```

### 3. Adicione sua implementação

Siga os padrões de organização descritos neste README.

### 4. Faça o commit das alterações

```bash
git commit -m "Adiciona implementação do [algoritmo]"
```

### 5. Envie um Pull Request

Envie sua contribuição para revisão dos demais integrantes.

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT** — consulte o arquivo `LICENSE` para mais detalhes.
