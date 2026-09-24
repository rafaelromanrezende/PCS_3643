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

## Estado do esqueleto (o que falta preencher)

Isto e' um esqueleto: a estrutura e os padroes estao definidos, o conteudo nao.
Procure por `TODO` no codigo.

**Frontend** -- `carregarFilmes()` em `static/app.js` esta completo e serve de
referencia. `carregarSessoes()`, `carregarSalas()` e `carregarIngressos()` ainda
despejam o JSON cru; falta montar as tabelas.

**Testes** -- 35 slots nomeados, 10 implementados e 25 marcados com
`self.skipTest("TODO: ...")`. Para preencher, apague a linha do `skipTest` e
escreva o corpo. O enunciado pede no minimo 20 implementados.

| Arquivo | Implementados | TODO |
| --- | --- | --- |
| `test_filme_api.py` | 4 | 8 |
| `test_sala_api.py` | 2 | 5 |
| `test_sessao_api.py` | 2 | 6 |
| `test_tipo_ingresso_api.py` | 2 | 6 |

Convencao de nome: `test_<metodo>_<recurso>_<comportamento esperado>`, e o teste
verifica **status code + corpo**, sempre pelo endpoint (nunca mexendo no banco
direto). Fixtures compartilhadas vao em `ApiTestCase` (`criar_filme`,
`criar_sala`, `criar_sessao`, `criar_tipo_ingresso`).

### Pendencia conhecida no backend

`TipoIngressoBase` em `view/tipo_ingresso_schema.py` nao valida `preco > 0`
(diferente de `FilmeBase.duracao`, que usa `Field(gt=0)`). Hoje um POST com
`preco: -10` e' aceito. O teste `test_post_preco_negativo_deve_ser_rejeitado`
esta reservado para isso -- adicionem `Field(gt=0)` no schema antes de
implementa-lo.

## Formatos de data (pegadinha)

Os dois recursos usam formatos diferentes, herdado do `aula3`:

| Recurso | Campo | Formato |
| --- | --- | --- |
| filme | `data_estreia`, `data_saida` | `dd/mm/aaaa` (ex: `10/03/2026`) |
| sessao | `data` | ISO `aaaa-mm-dd` (ex: `2026-03-15`) |
| sessao | `hora_inicio` | `HH:MM:SS` (ex: `12:00:00`) |
