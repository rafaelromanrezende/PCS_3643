#Eduardo Gobbi Jorge | NUSP: 5980278
#Marcelo Olivetti França Neri de Almeida | NUSP: 15474654
#Rafael Romanello Rezende | NUSP: 15485490
#Vinícius Akira Durante Tahara | NUSP: 12547002


import unittest

class TestModelo(unittest.TestCase):

#    def setUp(self):

    def test_hello(self):
        self.assertEqual('hello','hello')

    def test_goodbye(self):
        self.assertTrue('goodbye'=='hello')

#    def tearDown(self):


if __name__ == '__main__':
    unittest.main()