# Aula 4 - Interface web + testes de endpoint no CI

[![Testes](https://github.com/rafaelromanrezende/PCS_3643/actions/workflows/ci.yml/badge.svg)](https://github.com/rafaelromanrezende/PCS_3643/actions/workflows/ci.yml)

Backend herdado do `aula3/` (FastAPI + SQLAlchemy), agora com:

- interface web em `static/` que le filmes (com cartaz), sessoes, salas e tipos de
  ingresso **via REST API** (`fetch()`), sem nenhum dado embutido no HTML;
- campo `cartaz_url` no filme;
- testes de endpoint em `tests/`, executados pelo CI a cada commit.

## Requisitos

- Python 3.10 ou superior (o CI roda 3.12)
- `pip`

## Como rodar

```bash
cd aula4
python -m venv .venv
.venv\Scripts\activate         # Windows;  no Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

| Endereco | O que e' |
| --- | --- |
| http://127.0.0.1:8000/ | interface web |
| http://127.0.0.1:8000/docs | documentacao interativa da API (Swagger) |

O `cinema.db` (SQLite) e' criado automaticamente na primeira execucao. Para comecar
de zero, apague o arquivo.

## Como rodar os testes

```bash
cd aula4
python -m unittest discover -s tests -t . -v
```

Os testes usam um banco SQLite **em memoria** -- nao encostam no `cinema.db`. Isso
depende de `tests/base.py` definir `CINEMA_DB_URL=sqlite://` **antes** de importar
`app`, entao nao importe `app` direto num arquivo de teste.

## Estrutura

```
aula4/
├── app.py                  # FastAPI: routers + serve a interface estatica
├── model/                  # tabelas SQLAlchemy (filme tem cartaz_url)
├── view/                   # schemas Pydantic (validacao de entrada/saida)
├── controller/             # routers REST: /filmes /salas /sessoes /tipos-ingresso
├── static/
│   ├── index.html          # abas das 4 entidades
│   ├── app.js              # helper api() + carregarX() por entidade
│   ├── style.css
│   └── sem-cartaz.svg      # placeholder quando o filme nao tem cartaz
└── tests/
    ├── base.py             # ApiTestCase: TestClient + banco limpo + fixtures
    ├── test_filme_api.py
    ├── test_sala_api.py
    ├── test_sessao_api.py
    └── test_tipo_ingresso_api.py
```
