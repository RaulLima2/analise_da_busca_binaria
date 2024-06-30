import unittest
from src.busca_binaria import busca_binaria

class TestBinarySearch(unittest.TestCase):

    def test_elemento_no_meio(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(busca_binaria(lista, 5, 0, len(lista)), 4)

    def test_elemento_no_inicio(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(busca_binaria(lista, 1, 0, len(lista)), 0)

    def test_elemento_no_fim(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(busca_binaria(lista, 10, 0, len(lista)), 9)

    def test_elemento_nao_encontrado(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(busca_binaria(lista, 11, 0, len(lista)), -1)

    def test_lista_vazia(self):
        lista = []
        self.assertEqual(busca_binaria(lista, 5, 0, len(lista)), -1)

if __name__ == '__main__':
    
    unittest.main()