#Eduardo Gobbi Jorge | NUSP: 5980278
#Marcelo Olivetti França Neri de Almeida | NUSP: 15474654
#Rafael Romanello Rezende | NUSP: 15485490
#Vinícius Akira Durante Tahara | NUSP: 12547002


import unittest
from cinema import *

class TestModelo(unittest.TestCase):

    def setUp(self):
        filmes.clear()
        salas.clear()
        sessoes.clear()
        tipo_sala.clear()

    def test_cadastrar_filme_retorna_objeto_filme(self):
        filme = cadastrar_filme('King Kong', '10/03/2026', '10/05/2026', 120)
        self.assertIsInstance(filme, Filme)

    def test_cadastrar_filme_atributos_corretos(self):
        filme = cadastrar_filme('King Kong', '10/03/2026', '10/05/2026', 120)
        self.assertEqual(filme.nome, 'King Kong')
        self.assertEqual(filme.data_estreia, '10/03/2026')
        self.assertEqual(filme.data_saida, '10/05/2026')
        self.assertEqual(filme.duracao, 120)

    def test_cadastrar_filme_primeiro_codigo_eh_1(self):
        filme = cadastrar_filme('King Kong', '10/03/2026', '10/05/2026', 120)
        self.assertEqual(filme.codigo, 1)

    def test_cadastrar_filme_codigos_incrementam(self):
        filme1 = cadastrar_filme('King Kong', '10/03/2026', '10/05/2026', 120)
        filme2 = cadastrar_filme('Star Wars', '15/03/2026', '15/05/2026', 130)
        self.assertEqual(filme1.codigo, 1)
        self.assertEqual(filme2.codigo, 2)

    def test_cadastrar_filme_data_estreia_invalida_retorna_none(self):
        filme = cadastrar_filme('King Kong', '31/13/2026', '10/05/2026', 120)
        self.assertIsNone(filme)

    def test_cadastrar_filme_data_saida_invalida_retorna_none(self):
        filme = cadastrar_filme('King Kong', '10/03/2026', 'data invalida', 120)
        self.assertIsNone(filme)

    def test_cadastrar_filme_invalido_nao_entra_na_lista(self):
        cadastrar_filme('King Kong', '31/13/2026', '10/05/2026', 120)
        self.assertEqual(len(filmes), 0)

    def test_cadastrar_filme_nome_vazio_retorna_none(self):
        filme = cadastrar_filme('', '10/03/2026', '10/05/2026', 120)
        self.assertIsNone(filme)

    def test_cadastrar_filme_duracao_zero_retorna_none(self):
        filme = cadastrar_filme('King Kong', '10/03/2026', '10/05/2026', 0)
        self.assertIsNone(filme)

    def test_cadastrar_filme_duracao_negativa_retorna_none(self):
        filme = cadastrar_filme('King Kong', '10/03/2026', '10/05/2026', -1)
        self.assertIsNone(filme)

    def test_cadastrar_filme_data_estreia_depois_da_saida_retorna_none(self):
        filme = cadastrar_filme('King Kong', '10/05/2026', '10/03/2026', 120)
        self.assertIsNone(filme)

    def test_cadastrar_filme_nome_repetido_retorna_none(self):
        cadastrar_filme('King Kong', '10/03/2026', '10/05/2026', 120)
        filme2 = cadastrar_filme('King Kong', '15/03/2026', '15/05/2026', 130)
        self.assertIsNone(filme2)


    def test_cadastrar_sala_retorna_objeto_sala(self):
        sala = cadastrar_sala(1, 100, '2D')
        self.assertIsInstance(sala, Sala)

    def test_cadastrar_sala_atributos_corretos(self):
        sala = cadastrar_sala(1, 100, '2D')
        self.assertEqual(sala.numero, 1)
        self.assertEqual(sala.capacidade, 100)
        self.assertEqual(sala.tipo, '2D')

    def test_cadastrar_sala_numero_invalido_retorna_none(self):
        sala = cadastrar_sala(0, 100, '2D')
        self.assertIsNone(sala)

    def test_cadastrar_sala_capacidade_invalida_retorna_none(self):
        sala = cadastrar_sala(1, 0, '2D')
        self.assertIsNone(sala)

    def test_cadastrar_sala_numero_repetido_retorna_none(self):
        cadastrar_sala(1, 100, '2D')
        sala2 = cadastrar_sala(1, 200, '3D')
        self.assertIsNone(sala2)

    def test_cadastrar_sala_tipo_invalido_retorna_none(self):
        sala = cadastrar_sala(1, 100, 'IMAX')
        self.assertIsNone(sala)

    def test_pegar_sala_retorna_sala_cadastrada(self):
        cadastrar_sala(1, 100, '2D')
        sala2 = cadastrar_sala(2, 50, '3D')
        self.assertIs(pegar_sala(2), sala2)

    def test_pegar_sala_inexistente_retorna_none(self):
        self.assertIsNone(pegar_sala(99))


    # US02 - cadastrar valor do ingresso por tipo de sala

    def test_cadastrar_valor_ingresso_retorna_true(self):
        resultado = cadastrar_valor_ingresso('3D', 50)
        self.assertTrue(resultado)

    def test_cadastrar_valor_ingresso_atualiza_dicionario(self):
        cadastrar_valor_ingresso('3D', 50)
        self.assertEqual(tipo_sala['3D'], 50)

    def test_cadastrar_valor_ingresso_tipos_diferentes(self):
        cadastrar_valor_ingresso('2D', 30)
        cadastrar_valor_ingresso('3D', 50)
        self.assertEqual(tipo_sala['2D'], 30)
        self.assertEqual(tipo_sala['3D'], 50)

    def test_cadastrar_valor_ingresso_zero_retorna_false(self):
        resultado = cadastrar_valor_ingresso('3D', 0)
        self.assertFalse(resultado)

    def test_cadastrar_valor_ingresso_negativo_retorna_false(self):
        resultado = cadastrar_valor_ingresso('3D', -10)
        self.assertFalse(resultado)

    def test_cadastrar_valor_ingresso_invalido_nao_atualiza_dicionario(self):
        cadastrar_valor_ingresso('3D', -10)
        self.assertNotIn('3D', tipo_sala)

    def test_cadastrar_valor_ingresso_tipo_sala_invalido_retorna_false(self):
        resultado = cadastrar_valor_ingresso('IMAX', 50)
        self.assertFalse(resultado)


    def test_listar_filme_disponivel(self):
        tipo_sala['3D'] = 50

        filme = cadastrar_filme(
            'King Kong', '10/03/2026', '10/05/2026', 120
        )
        sala = cadastrar_sala(1, 100, '3D')

        sessao = Sessao(1, sala, filme, '15/03/2026', 12, 100)
        sessoes.append(sessao)

        resultado = listar_filmes_por_data('15/03/2026')

        self.assertEqual(
            resultado,
            '1: King Kong, sala 1 (3D), 12h, 50 reais.'
        )

    def test_listar_varias_sessoes(self):
        tipo_sala['3D'] = 50

        filme = cadastrar_filme(
            'King Kong', '10/03/2026', '10/05/2026', 120
        )
        sala = cadastrar_sala(1, 100, '3D')

        sessao1 = Sessao(
            1, sala, filme, '15/03/2026', 12, 100
        )
        sessao2 = Sessao(
            2, sala, filme, '15/03/2026', 18, 100
        )

        sessoes.append(sessao1)
        sessoes.append(sessao2)

        resultado = listar_filmes_por_data('15/03/2026')

        esperado = (
            '1: King Kong, sala 1 (3D), 12h, 50 reais.\n'
            '2: King Kong, sala 1 (3D), 18h, 50 reais.'
        )

        self.assertEqual(resultado, esperado)


    def test_nao_listar_sessao_lotada(self):
        tipo_sala['3D'] = 50

        filme = cadastrar_filme(
            'King Kong', '10/03/2026', '10/05/2026', 120
        )
        sala = cadastrar_sala(1, 3, '3D')

        sessao = Sessao(
            1, sala, filme, '15/03/2026', 12, 3
        )
        sessao.assentos = {1: 1, 2: 1, 3: 1}

        sessoes.append(sessao)

        resultado = listar_filmes_por_data('15/03/2026')

        self.assertEqual(
            resultado,
            'Nenhum filme no dia escolhido.'
        )
        
    def test_nenhum_filme_no_dia(self):
        resultado = listar_filmes_por_data('15/03/2026')

        self.assertEqual(
            resultado,
            'Nenhum filme no dia escolhido.'
        )

    def test_data_invalida(self):
        resultado = listar_filmes_por_data('31/02/2026')

        self.assertEqual(resultado, 'Data invalida.')

    def test_data_formato_invalido(self):
        resultado = listar_filmes_por_data('15-03-2026')
        self.assertEqual(resultado, 'Data invalida.')


    # US04 - cadastrar sessao

    def _criar_filme_e_sala(self):
        filme = cadastrar_filme('King Kong', '10/03/2026', '10/05/2026', 120)
        sala = cadastrar_sala(1, 100, '3D')
        return filme, sala

    def test_cadastrar_sessao_retorna_objeto_sessao(self):
        self._criar_filme_e_sala()
        sessao = cadastrar_sessao(1, 1, '15/03/2026', 12)
        self.assertIsInstance(sessao, Sessao)

    def test_cadastrar_sessao_atributos_corretos(self):
        filme, sala = self._criar_filme_e_sala()
        sessao = cadastrar_sessao(1, 1, '15/03/2026', 12)
        self.assertEqual(sessao.sala, sala)
        self.assertEqual(sessao.filme, filme)
        self.assertEqual(sessao.data, '15/03/2026')
        self.assertEqual(sessao.hora_inicio, 12)

    def test_cadastrar_sessao_primeiro_codigo_eh_1(self):
        self._criar_filme_e_sala()
        sessao = cadastrar_sessao(1, 1, '15/03/2026', 12)
        self.assertEqual(sessao.codigo, 1)

    def test_cadastrar_sessao_codigos_incrementam(self):
        self._criar_filme_e_sala()
        sessao1 = cadastrar_sessao(1, 1, '15/03/2026', 12)
        sessao2 = cadastrar_sessao(1, 1, '15/03/2026', 18)
        self.assertEqual(sessao1.codigo, 1)
        self.assertEqual(sessao2.codigo, 2)

    def test_cadastrar_sessao_assentos_desocupados_do_1_ate_capacidade(self):
        cadastrar_filme('King Kong', '10/03/2026', '10/05/2026', 120)
        cadastrar_sala(1, 3, '3D')
        sessao = cadastrar_sessao(1, 1, '15/03/2026', 12)
        self.assertEqual(sessao.assentos, {1: 0, 2: 0, 3: 0})

    def test_cadastrar_sessao_hora_negativa_retorna_none(self):
        self._criar_filme_e_sala()
        sessao = cadastrar_sessao(1, 1, '15/03/2026', -1)
        self.assertIsNone(sessao)

    def test_cadastrar_sessao_hora_maior_que_23_retorna_none(self):
        self._criar_filme_e_sala()
        sessao = cadastrar_sessao(1, 1, '15/03/2026', 24)
        self.assertIsNone(sessao)

    def test_cadastrar_sessao_data_invalida_retorna_none(self):
        self._criar_filme_e_sala()
        sessao = cadastrar_sessao(1, 1, '31/13/2026', 12)
        self.assertIsNone(sessao)

    def test_cadastrar_sessao_sala_inexistente_retorna_none(self):
        cadastrar_filme('King Kong', '10/03/2026', '10/05/2026', 120)
        sessao = cadastrar_sessao(99, 1, '15/03/2026', 12)
        self.assertIsNone(sessao)

    def test_cadastrar_sessao_filme_inexistente_retorna_none(self):
        cadastrar_sala(1, 100, '3D')
        sessao = cadastrar_sessao(1, 99, '15/03/2026', 12)
        self.assertIsNone(sessao)

    def test_cadastrar_sessao_invalida_nao_entra_na_lista(self):
        self._criar_filme_e_sala()
        cadastrar_sessao(1, 1, '31/13/2026', 12)
        self.assertEqual(len(sessoes), 0)

    def test_cadastrar_sessao_conflito_mesma_sala_dia_horario_retorna_none(self):
        self._criar_filme_e_sala()
        cadastrar_sessao(1, 1, '15/03/2026', 12)
        sessao2 = cadastrar_sessao(1, 1, '15/03/2026', 12)
        self.assertIsNone(sessao2)

    def test_cadastrar_sessao_mesma_sala_horario_diferente_eh_permitido(self):
        self._criar_filme_e_sala()
        sessao1 = cadastrar_sessao(1, 1, '15/03/2026', 12)
        sessao2 = cadastrar_sessao(1, 1, '15/03/2026', 18)
        self.assertIsNotNone(sessao1)
        self.assertIsNotNone(sessao2)

    def test_cadastrar_sessao_mesmo_horario_sala_diferente_eh_permitido(self):
        cadastrar_filme('King Kong', '10/03/2026', '10/05/2026', 120)
        cadastrar_sala(1, 100, '3D')
        cadastrar_sala(2, 100, '2D')
        sessao1 = cadastrar_sessao(1, 1, '15/03/2026', 12)
        sessao2 = cadastrar_sessao(2, 1, '15/03/2026', 12)
        self.assertIsNotNone(sessao1)
        self.assertIsNotNone(sessao2)

    def test_cadastrar_sessao_integra_com_listar_filmes_por_data(self):
        tipo_sala['3D'] = 50
        self._criar_filme_e_sala()
        cadastrar_sessao(1, 1, '15/03/2026', 12)

        resultado = listar_filmes_por_data('15/03/2026')

        self.assertEqual(
            resultado,
            '1: King Kong, sala 1 (3D), 12h, 50 reais.'
        )

    def test_cadastrar_sessao_integra_com_comprar_ingressos(self):
        tipo_sala['3D'] = 50
        self._criar_filme_e_sala()
        cadastrar_sessao(1, 1, '15/03/2026', 12)

        total = comprarIngressos(1, [1], [0])

        self.assertEqual(total, 50)


    # US06 - comprar ingressos

    def _criar_sessao_padrao(self, capacidade=100):
        tipo_sala['3D'] = 50
        filme = cadastrar_filme('King Kong', '10/03/2026', '10/05/2026', 120)
        sala = cadastrar_sala(1, capacidade, '3D')
        sessao = Sessao(1, sala, filme, '15/03/2026', 12, capacidade)
        sessoes.append(sessao)
        return sessao

    def test_comprar_ingresso_inteira_retorna_valor_cheio(self):
        self._criar_sessao_padrao()
        total = comprarIngressos(1, [1], [0])
        self.assertEqual(total, 50)

    def test_comprar_ingresso_meia_retorna_metade_do_valor(self):
        self._criar_sessao_padrao()
        total = comprarIngressos(1, [1], [1])
        self.assertEqual(total, 25)

    def test_comprar_varios_ingressos_tipos_mistos_soma_correta(self):
        self._criar_sessao_padrao()
        total = comprarIngressos(1, [1, 2, 3], [0, 1, 0])
        self.assertEqual(total, 125)

    def test_comprar_ingresso_reserva_assento_escolhido(self):
        sessao = self._criar_sessao_padrao()
        comprarIngressos(1, [1], [0])
        self.assertEqual(sessao.assentos[1], 1)

    def test_comprar_ingresso_nao_reserva_outros_assentos(self):
        sessao = self._criar_sessao_padrao()
        comprarIngressos(1, [1], [0])
        self.assertEqual(sessao.assentos[2], 0)

    def test_comprar_ingresso_sessao_inexistente_retorna_zero(self):
        self._criar_sessao_padrao()
        total = comprarIngressos(999, [1], [0])
        self.assertEqual(total, 0)

    def test_comprar_ingresso_assento_ja_ocupado_retorna_zero(self):
        sessao = self._criar_sessao_padrao()
        sessao.assentos[1] = 1
        total = comprarIngressos(1, [1], [0])
        self.assertEqual(total, 0)

    def test_comprar_ingresso_assento_inexistente_retorna_zero(self):
        self._criar_sessao_padrao(capacidade=3)
        total = comprarIngressos(1, [10], [0])
        self.assertEqual(total, 0)

    def test_comprar_ingresso_tipo_invalido_retorna_zero(self):
        self._criar_sessao_padrao()
        total = comprarIngressos(1, [1], [2])
        self.assertEqual(total, 0)

    def test_comprar_ingresso_listas_tamanhos_diferentes_retorna_zero(self):
        self._criar_sessao_padrao()
        total = comprarIngressos(1, [1, 2], [0])
        self.assertEqual(total, 0)

    def test_comprar_ingresso_lista_vazia_retorna_zero(self):
        self._criar_sessao_padrao()
        total = comprarIngressos(1, [], [])
        self.assertEqual(total, 0)

    def test_comprar_ingresso_parcialmente_invalido_nao_reserva_nenhum_assento(self):
        sessao = self._criar_sessao_padrao()
        sessao.assentos[2] = 1

        total = comprarIngressos(1, [1, 2], [0, 0])

        self.assertEqual(total, 0)
        self.assertEqual(sessao.assentos[1], 0)

    def test_comprar_ingresso_assento_repetido_na_mesma_compra(self):
        sessao = self._criar_sessao_padrao()

        total = comprarIngressos(1, [1, 1], [0, 0])

        self.assertEqual(total, 100)
        self.assertEqual(sessao.assentos[1], 1)


if __name__ == '__main__':
    unittest.main()