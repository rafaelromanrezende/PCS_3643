"""CRUD de /filmes via endpoints.

Os 3 primeiros estao implementados como referencia de estilo.
Os marcados com TODO sao os slots a preencher -- troque o self.skipTest
pelo corpo do teste.
"""

import unittest

from tests.base import ApiTestCase


class TestFilmeAPI(ApiTestCase):

    # --- CREATE ---------------------------------------------------------
    def test_post_filme_retorna_201_e_codigo(self):
        resposta = self.client.post("/filmes", json={
            "nome": "King Kong",
            "data_estreia": "10/03/2026",
            "data_saida": "10/05/2026",
            "duracao": 120,
        })

        self.assertEqual(resposta.status_code, 201)
        self.assertEqual(resposta.json()["codigo"], 1)

    def test_post_filme_guarda_cartaz_url(self):
        filme = self.criar_filme(cartaz_url="https://exemplo.com/poster.jpg")

        self.assertEqual(filme["cartaz_url"], "https://exemplo.com/poster.jpg")

    def test_post_filme_sem_cartaz_url_fica_none(self):
        resposta = self.client.post("/filmes", json={
            "nome": "Star Wars",
            "data_estreia": "15/03/2026",
            "data_saida": "15/05/2026",
            "duracao": 130,
        })

        self.assertIsNone(resposta.json()["cartaz_url"])

    def test_post_filme_nome_repetido_retorna_409(self):
        # TODO(filme): criar o mesmo nome duas vezes e conferir 409
        self.skipTest("TODO: POST duplicado deve responder 409")

    def test_post_filme_duracao_invalida_retorna_422(self):
        # TODO(filme): duracao=0 e duracao=-1 devem cair na validacao do Pydantic
        self.skipTest("TODO: POST com duracao <= 0 deve responder 422")

    # --- READ -----------------------------------------------------------
    def test_get_filmes_lista_vazia(self):
        resposta = self.client.get("/filmes")

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json(), [])

    def test_get_filme_por_codigo_retorna_o_filme(self):
        # TODO(filme): criar via criar_filme() e buscar GET /filmes/{codigo}
        self.skipTest("TODO: GET /filmes/{codigo} deve devolver o filme criado")

    def test_get_filme_inexistente_retorna_404(self):
        # TODO(filme): GET /filmes/999
        self.skipTest("TODO: GET de codigo inexistente deve responder 404")

    # --- UPDATE ---------------------------------------------------------
    def test_put_filme_atualiza_cartaz_url(self):
        # TODO(filme): PUT trocando so' o cartaz_url; os outros campos ficam iguais
        self.skipTest("TODO: PUT deve atualizar cartaz_url sem apagar o resto")

    def test_put_filme_inexistente_retorna_404(self):
        # TODO(filme): PUT /filmes/999
        self.skipTest("TODO: PUT de codigo inexistente deve responder 404")

    # --- DELETE ---------------------------------------------------------
    def test_delete_filme_retorna_204_e_remove_da_listagem(self):
        # TODO(filme): DELETE e depois GET /filmes conferindo lista vazia
        self.skipTest("TODO: DELETE deve responder 204 e sumir da listagem")

    def test_delete_filme_inexistente_retorna_404(self):
        # TODO(filme): DELETE /filmes/999
        self.skipTest("TODO: DELETE de codigo inexistente deve responder 404")


if __name__ == "__main__":
    unittest.main()
