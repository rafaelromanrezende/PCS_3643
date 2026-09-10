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

    def test_hello(self):
        self.assertEqual('hello','hello')

    def test_goodbye(self):
        self.assertTrue('goodbye'=='hello')

#    def tearDown(self):


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
     
    def test_listar_filme_disponivel(self):
        tipo_sala['3D'] = 50

        filme = cadastrar_filme(
            'King Kong', '10/03/2026', '10/05/2026', 120
        )
        sala = cadastrar_sala(1, 100, '3D')

        sessao = Sessao(sala, filme, '15/03/2026', 12)
        sessao.codigo = 1
        sessao.assentos = [0] * 100
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

        sessao1 = Sessao(sala, filme, '15/03/2026', 12)
        sessao1.codigo = 1
        sessao1.assentos = [0] * 100

        sessao2 = Sessao(sala, filme, '15/03/2026', 18)
        sessao2.codigo = 2
        sessao2.assentos = [0] * 100

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

        sessao = Sessao(sala, filme, '15/03/2026', 12)
        sessao.codigo = 1
        sessao.assentos = [1, 1, 1]
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

if __name__ == '__main__':
    unittest.main()