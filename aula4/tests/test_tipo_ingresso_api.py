"""CRUD de /tipos-ingresso via endpoints. tipo 0 = inteira, 1 = meia."""

import unittest

from tests.base import ApiTestCase


class TestTipoIngressoAPI(ApiTestCase):

    # --- CREATE ---------------------------------------------------------
    def test_post_tipo_ingresso_retorna_201(self):
        resposta = self.client.post("/tipos-ingresso", json={
            "tipo": 0, "preco": 50.0,
        })

        self.assertEqual(resposta.status_code, 201)
        self.assertEqual(resposta.json()["preco"], 50.0)

    def test_post_tipo_fora_do_dominio_retorna_422(self):
        resposta = self.client.post("/tipos-ingresso", json={
            "tipo": 2, "preco": 50.0,
        })

        self.assertEqual(resposta.status_code, 422)

    def test_post_tipo_repetido_retorna_409(self):
        # TODO(ingresso): o model tem unique em `tipo` -- confirmar o 409
        self.skipTest("TODO: POST com tipo repetido deve responder 409")

    def test_post_preco_negativo_deve_ser_rejeitado(self):
        # TODO(ingresso): ATENCAO -- TipoIngressoBase em view/ nao tem Field(gt=0),
        # entao hoje preco=-10 passa. Decidam: adicionar a validacao no schema
        # (recomendado) e este teste espera 422.
        self.skipTest("TODO: preco <= 0 deve responder 422 (falta Field(gt=0) no schema)")

    # --- READ -----------------------------------------------------------
    def test_get_tipos_ingresso_lista_os_cadastrados(self):
        # TODO(ingresso): criar inteira e meia, conferir len == 2
        self.skipTest("TODO: GET /tipos-ingresso deve listar os dois tipos")

    def test_get_tipo_ingresso_inexistente_retorna_404(self):
        # TODO(ingresso): GET /tipos-ingresso/999
        self.skipTest("TODO: GET de codigo inexistente deve responder 404")

    # --- UPDATE ---------------------------------------------------------
    def test_put_tipo_ingresso_atualiza_preco(self):
        # TODO(ingresso): PUT mudando preco para 30.0
        self.skipTest("TODO: PUT deve atualizar o preco")

    # --- DELETE ---------------------------------------------------------
    def test_delete_tipo_ingresso_retorna_204(self):
        # TODO(ingresso): DELETE e confirmar remocao
        self.skipTest("TODO: DELETE deve responder 204")


if __name__ == "__main__":
    unittest.main()
