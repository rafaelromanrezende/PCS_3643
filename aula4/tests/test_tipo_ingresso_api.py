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
        self.criar_tipo_ingresso(tipo=0, preco=50.0)

        resposta = self.client.post("/tipos-ingresso", json={
            "tipo": 0, "preco": 60.0,
        })

        self.assertEqual(resposta.status_code, 409)

    def test_post_preco_negativo_deve_ser_rejeitado(self):
        resposta = self.client.post("/tipos-ingresso", json={
            "tipo": 0, "preco": -10.0,
        })

        self.assertEqual(resposta.status_code, 422)

    # --- READ -----------------------------------------------------------
    def test_get_tipos_ingresso_lista_os_cadastrados(self):
        self.criar_tipo_ingresso(tipo=0, preco=50.0)
        self.criar_tipo_ingresso(tipo=1, preco=25.0)

        resposta = self.client.get("/tipos-ingresso")

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(len(resposta.json()), 2)
        self.assertEqual({item["tipo"] for item in resposta.json()}, {0, 1})

    def test_get_tipo_ingresso_inexistente_retorna_404(self):
        resposta = self.client.get("/tipos-ingresso/999")

        self.assertEqual(resposta.status_code, 404)

    # --- UPDATE ---------------------------------------------------------
    def test_put_tipo_ingresso_atualiza_preco(self):
        ingresso = self.criar_tipo_ingresso(tipo=0, preco=50.0)

        resposta = self.client.put(f"/tipos-ingresso/{ingresso['codigo']}", json={
            "preco": 30.0,
        })

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["preco"], 30.0)

    # --- DELETE ---------------------------------------------------------
    def test_delete_tipo_ingresso_retorna_204(self):
        ingresso = self.criar_tipo_ingresso(tipo=0, preco=50.0)

        resposta = self.client.delete(f"/tipos-ingresso/{ingresso['codigo']}")
        lista = self.client.get("/tipos-ingresso")

        self.assertEqual(resposta.status_code, 204)
        self.assertEqual(lista.json(), [])


if __name__ == "__main__":
    unittest.main()
