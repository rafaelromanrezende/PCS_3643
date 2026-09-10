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



if __name__ == '__main__':
    unittest.main()