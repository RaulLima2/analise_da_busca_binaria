
import unittest
from ..src import busca_binaria

class TestBinarySearch(unittest.TestCase):

    def test_elemento_no_meio(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(busca_binaria(arr, 5), 4)

    def test_elemento_no_inicio(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(busca_binaria(arr, 1), 0)

    def test_elemento_no_fim(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(busca_binaria(arr, 10), 9)

    def test_elemento_nao_encontrado(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(busca_binaria(arr, 11), -1)

    def test_lista_vazia(self):
        arr = []
        self.assertEqual(busca_binaria(arr, 5), -1)