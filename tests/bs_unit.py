import unittest
from ..src import busca_sequencial

class TestBuscaSequencial(unittest.TestCase):

    def test_busca_sequencial(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(busca_sequencial(lista, 3), 2)

    def test_elemento_nao_encontrado(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(busca_sequencial(lista, 6), -1)

    def test_lista_vazia(self):
        lista = []
        self.assertEqual(busca_sequencial(lista, 5), -1)

if __name__ == '__main__':
    unittest.main()