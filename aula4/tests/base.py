"""Base dos testes de endpoint.

IMPORTANTE: o CINEMA_DB_URL e' definido antes de importar `app`, senao a
aplicacao criaria/usaria o cinema.db de verdade. Todo teste novo deve
herdar de ApiTestCase e nunca importar `app` por conta propria.
"""

import os

os.environ.setdefault("CINEMA_DB_URL", "sqlite://")  # banco em memoria

import unittest

from fastapi.testclient import TestClient

from app import app
from model.database import Base, engine


class ApiTestCase(unittest.TestCase):
    """Cliente HTTP + banco em memoria zerado antes de cada teste."""

    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def setUp(self):
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

    # --- fixtures -------------------------------------------------------
    # Cada helper cria o recurso via POST (nao mexe no banco direto) e
    # devolve o corpo da resposta. Sobrescreva campos por keyword.

    def criar_filme(self, **campos):
        corpo = {
            "nome": "King Kong",
            "data_estreia": "10/03/2026",
            "data_saida": "10/05/2026",
            "duracao": 120,
            "cartaz_url": "https://exemplo.com/kingkong.jpg",
            **campos,
        }
        resposta = self.client.post("/filmes", json=corpo)
        self.assertEqual(resposta.status_code, 201, resposta.text)
        return resposta.json()

    def criar_sala(self, **campos):
        corpo = {"numero": 1, "capacidade": 100, "tipo": "3D", **campos}
        resposta = self.client.post("/salas", json=corpo)
        self.assertEqual(resposta.status_code, 201, resposta.text)
        return resposta.json()

    def criar_tipo_ingresso(self, **campos):
        corpo = {"tipo": 0, "preco": 50.0, **campos}
        resposta = self.client.post("/tipos-ingresso", json=corpo)
        self.assertEqual(resposta.status_code, 201, resposta.text)
        return resposta.json()

    def criar_sessao(self, **campos):
        """Cria filme e sala se nao vierem informados nos campos."""
        if "filme_codigo" not in campos:
            campos["filme_codigo"] = self.criar_filme()["codigo"]
        if "sala_numero" not in campos:
            campos["sala_numero"] = self.criar_sala()["numero"]

        corpo = {
            "data": "2026-03-15",       # sessao usa ISO, filme usa dd/mm/aaaa
            "hora_inicio": "12:00:00",
            "quantidade_assentos": 10,
            **campos,
        }
        resposta = self.client.post("/sessoes", json=corpo)
        self.assertEqual(resposta.status_code, 201, resposta.text)
        return resposta.json()
