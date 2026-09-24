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
        # TODO(sala): mesmo numero duas vezes
        self.skipTest("TODO: POST com numero repetido deve responder 409")

    # --- READ -----------------------------------------------------------
    def test_get_salas_lista_as_cadastradas(self):
        # TODO(sala): criar 2 salas e conferir len == 2 no GET /salas
        self.skipTest("TODO: GET /salas deve listar todas as salas")

    def test_get_sala_inexistente_retorna_404(self):
        # TODO(sala): GET /salas/99
        self.skipTest("TODO: GET de numero inexistente deve responder 404")

    # --- UPDATE ---------------------------------------------------------
    def test_put_sala_atualiza_capacidade(self):
        # TODO(sala): PUT /salas/{numero} mudando capacidade
        self.skipTest("TODO: PUT deve atualizar a capacidade")

    # --- DELETE ---------------------------------------------------------
    def test_delete_sala_retorna_204(self):
        # TODO(sala): DELETE /salas/{numero} e confirmar 404 no GET seguinte
        self.skipTest("TODO: DELETE deve responder 204")


if __name__ == "__main__":
    unittest.main()
