"""CRUD de /sessoes via endpoints.

Cuidado com os formatos: sessao usa data ISO ("2026-03-15") e hora_inicio
"HH:MM:SS"; filme usa dd/mm/aaaa. O POST cria os assentos a partir de
quantidade_assentos.
"""

import unittest

from tests.base import ApiTestCase


class TestSessaoAPI(ApiTestCase):

    # --- CREATE ---------------------------------------------------------
    def test_post_sessao_retorna_201_e_cria_os_assentos(self):
        sessao = self.criar_sessao(quantidade_assentos=10)

        self.assertEqual(len(sessao["assentos"]), 10)
        self.assertEqual([a["numero"] for a in sessao["assentos"]], list(range(1, 11)))

    def test_post_sessao_assentos_comecam_desocupados(self):
        sessao = self.criar_sessao(quantidade_assentos=3)

        self.assertTrue(all(a["ocupado"] is False for a in sessao["assentos"]))

    def test_post_sessao_mesma_sala_data_hora_retorna_409(self):
        primeira = self.criar_sessao()
        resposta = self.client.post("/sessoes", json={
 "sala_numero": primeira["sala_numero"],
            "filme_codigo": primeira["filme_codigo"],
            "data": primeira["data"],
            "hora_inicio": primeira["hora_inicio"],
            "quantidade_assentos": 10,
        })

        self.assertEqual(resposta.status_code, 409)
        self.assertIn("detail", resposta.json())

    def test_post_sessao_mesma_sala_horario_diferente_eh_permitido(self):
        primeira = self.criar_sessao()
        resposta = self.client.post("/sessoes", json={
            "sala_numero": primeira["sala_numero"],
            "filme_codigo": primeira["filme_codigo"],
            "data": primeira["data"],
            "hora_inicio": "18:00:00",
            "quantidade_assentos": 5,
        })

        self.assertEqual(resposta.status_code, 201, resposta.text)
        self.assertEqual(resposta.json()["hora_inicio"], "18:00:00")
        self.assertEqual(resposta.json()["sala_numero"], primeira["sala_numero"])

    def test_get_sessoes_filtra_por_data(self):
        primeira = self.criar_sessao(data="2026-03-15")
        self.criar_sessao(
            filme_codigo=primeira["filme_codigo"],
            sala_numero=primeira["sala_numero"],
            data="2026-03-16",
        )

        resposta = self.client.get("/sessoes?data=2026-03-15")

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(len(resposta.json()), 1)
        self.assertEqual(resposta.json()[0]["codigo"], primeira["codigo"])

    def test_get_sessao_inexistente_retorna_404(self):
        resposta = self.client.get("/sessoes/999")

        self.assertEqual(resposta.status_code, 404)
        self.assertIn("detail", resposta.json())

    def test_put_sessao_atualiza_hora_inicio(self):
        sessao = self.criar_sessao()
        resposta = self.client.put(
            f"/sessoes/{sessao['codigo']}",
            json={"hora_inicio": "18:00:00"},
        )

        self.assertEqual(resposta.status_code, 200, resposta.text)
        self.assertEqual(resposta.json()["hora_inicio"], "18:00:00")
        self.assertEqual(resposta.json()["filme_codigo"], sessao["filme_codigo"])

        consulta = self.client.get(f"/sessoes/{sessao['codigo']}")
        self.assertEqual(consulta.status_code, 200)
        self.assertEqual(consulta.json()["hora_inicio"], "18:00:00")

    def test_delete_sessao_remove_os_assentos_em_cascata(self):
        sessao = self.criar_sessao(quantidade_assentos=3)
        resposta = self.client.delete(f"/sessoes/{sessao['codigo']}")

        self.assertEqual(resposta.status_code, 204)
        self.assertEqual(resposta.content, b"")

        consulta = self.client.get(f"/sessoes/{sessao['codigo']}")
        self.assertEqual(consulta.status_code, 404)


if __name__ == "__main__":
    unittest.main()
