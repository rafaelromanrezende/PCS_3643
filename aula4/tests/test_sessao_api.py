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
        # TODO(sessao): ha UniqueConstraint (sala_numero, data, hora_inicio).
        # Reaproveite o filme/sala da primeira sessao nos campos da segunda.
        self.skipTest("TODO: sessao duplicada na mesma sala/data/hora deve dar 409")

    def test_post_sessao_mesma_sala_horario_diferente_eh_permitido(self):
        # TODO(sessao): mesma sala, hora_inicio "18:00:00" -> 201
        self.skipTest("TODO: mesma sala em horario diferente deve dar 201")

    # --- READ -----------------------------------------------------------
    def test_get_sessoes_filtra_por_data(self):
        # TODO(sessao): GET /sessoes?data=2026-03-15 -- o controller aceita esse
        # query param. Criar sessoes em datas diferentes e conferir o filtro.
        self.skipTest("TODO: GET /sessoes?data=... deve filtrar pela data")

    def test_get_sessao_inexistente_retorna_404(self):
        # TODO(sessao): GET /sessoes/999
        self.skipTest("TODO: GET de codigo inexistente deve responder 404")

    # --- UPDATE ---------------------------------------------------------
    def test_put_sessao_atualiza_hora_inicio(self):
        # TODO(sessao): PUT mudando hora_inicio e conferindo no corpo
        self.skipTest("TODO: PUT deve atualizar hora_inicio")

    # --- DELETE ---------------------------------------------------------
    def test_delete_sessao_remove_os_assentos_em_cascata(self):
        # TODO(sessao): o relacionamento tem cascade="all, delete-orphan".
        # Apagar a sessao e confirmar 404 no GET seguinte.
        self.skipTest("TODO: DELETE deve responder 204 e apagar os assentos")


if __name__ == "__main__":
    unittest.main()
