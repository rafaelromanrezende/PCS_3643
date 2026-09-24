# PCS3643 - Laboratorio de Engenharia de Software

[![Testes](https://github.com/rafaelromanrezende/PCS_3643/actions/workflows/ci.yml/badge.svg)](https://github.com/rafaelromanrezende/PCS_3643/actions/workflows/ci.yml)

Sistema de venda de ingressos de cinema, desenvolvido ao longo das aulas.

## Grupo

| Nome | NUSP |
| --- | --- |
| Eduardo Gobbi Jorge | 5980278 |
| Marcelo Olivetti Franca Neri de Almeida | 15474654 |
| Rafael Romanello Rezende | 15485490 |
| Vinicius Akira Durante Tahara | 12547002 |

## Organizacao do repositorio

| Pasta | Conteudo |
| --- | --- |
| `aula2/` | Modelo procedural do cinema (listas em memoria) |
| `aula3/` | REST API com FastAPI + SQLAlchemy |
| `aula4/` | **Entrega atual**: interface web consumindo a API + testes de endpoint no CI |

A entrega da aula 4 esta em [`aula4/`](aula4/) -- veja o [README de lá](aula4/README.md)
para instrucoes de execucao.

## Integracao continua

O workflow [`.github/workflows/ci.yml`](.github/workflows/ci.yml) roda os testes de
endpoint do `aula4/` a cada push e pull request. O badge acima reflete o resultado
da ultima execucao na branch `main`.
