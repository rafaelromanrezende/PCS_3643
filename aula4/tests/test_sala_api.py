"""CRUD de /salas via endpoints. Siga o estilo de tests/test_filme_api.py."""

import unittest

from tests.base import ApiTestCase


class TestSalaAPI(ApiTestCase):

    # --- CREATE ---------------------------------------------------------
    def test_post_sala_retorna_201_com_os_campos(self):
        resposta = self.client.post("/salas", json={
            "numero": 1, "capacidade": 100, "tipo": "3D",
        })

        self.assertEqual(resposta.status_code, 201)
        self.assertEqual(
            resposta.json(), {"numero": 1, "capacidade": 100, "tipo": "3D"}
        )

    def test_post_sala_tipo_invalido_retorna_422(self):
        resposta = self.client.post("/salas", json={
            "numero": 1, "capacidade": 100, "tipo": "IMAX",
        })

        self.assertEqual(resposta.status_code, 422)

    def test_post_sala_numero_repetido_retorna_409(self):
        self.criar_sala(numero=1)

        resposta = self.client.post("/salas", json={
            "numero": 1, "capacidade": 80, "tipo": "2D",
        })

        self.assertEqual(resposta.status_code, 409)

    # --- READ -----------------------------------------------------------
    def test_get_salas_lista_as_cadastradas(self):
        self.criar_sala(numero=1)
        self.criar_sala(numero=2, capacidade=150, tipo="2D")

        resposta = self.client.get("/salas")

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(len(resposta.json()), 2)

    def test_get_sala_por_numero_retorna_a_sala_persistida(self):
        sala = self.criar_sala(numero=7, capacidade=120, tipo="2D")

        resposta = self.client.get(f"/salas/{sala['numero']}")

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json(), sala)

    def test_get_sala_inexistente_retorna_404(self):
        resposta = self.client.get("/salas/99")

        self.assertEqual(resposta.status_code, 404)

    # --- UPDATE ---------------------------------------------------------
    def test_put_sala_atualiza_capacidade(self):
        sala = self.criar_sala(numero=3, capacidade=100)

        resposta = self.client.put(
            f"/salas/{sala['numero']}",
            json={"capacidade": 200},
        )

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["capacidade"], 200)

        consulta = self.client.get(f"/salas/{sala['numero']}")
        self.assertEqual(consulta.status_code, 200)
        self.assertEqual(consulta.json()["capacidade"], 200)

    # --- DELETE ---------------------------------------------------------
    def test_delete_sala_retorna_204(self):
        sala = self.criar_sala(numero=4)

        resposta = self.client.delete(f"/salas/{sala['numero']}")

        self.assertEqual(resposta.status_code, 204)
        self.assertEqual(resposta.content, b"")

        consulta = self.client.get(f"/salas/{sala['numero']}")
        self.assertEqual(consulta.status_code, 404)


if __name__ == "__main__":
    unittest.main()
