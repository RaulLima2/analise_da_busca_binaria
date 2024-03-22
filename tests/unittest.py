import unittest
from ..src import busca_binaria, busca_sequencial, busca_sequencial_otimizada
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

class TestBuscaSequencial(unittest.TestCase):

    def test_busca_sequencial(self):
        # Caso de teste simples
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(busca_sequencial(lista, 3), 2)

    def test_elemento_nao_encontrado(self):
        # Testa quando o elemento não está na lista
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(busca_sequencial(lista, 6), -1)

    def test_lista_vazia(self):
        # Testa quando a lista está vazia
        lista = []
        self.assertEqual(busca_sequencial(lista, 5), -1)

class TestBuscaSequencialOtimizada(unittest.TestCase):

    def test_elemento_existente(self):
        lista = [1, 3, 5, 7, 9, 11]
        elemento = 7
        self.assertEqual(busca_sequencial_otimizada(lista, elemento), 3)

    def test_elemento_inexistente(self):
        lista = [1, 3, 5, 7, 9, 11]
        elemento = 8
        self.assertEqual(busca_sequencial_otimizada(lista, elemento), -1)

    def test_elemento_no_inicio(self):
        lista = [1, 3, 5, 7, 9, 11]
        elemento = 1
        self.assertEqual(busca_sequencial_otimizada(lista, elemento), 0)

    def test_elemento_no_fim(self):
        lista = [1, 3, 5, 7, 9, 11]
        elemento = 11
        self.assertEqual(busca_sequencial_otimizada(lista, elemento), 5)

    def test_lista_vazia(self):
        lista = []
        elemento = 5
        self.assertEqual(busca_sequencial_otimizada(lista, elemento), -1)

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
