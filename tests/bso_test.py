import unittest
from src.busca_sequencial_otimizada import busca_sequencial_otimizada

class TestBuscaSequencialOtimizada(unittest.TestCase):
    
    def test_busca_sequencial_otimizada(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(busca_sequencial_otimizada(lista, 3, 0, len(lista)), 6)

    def test_busca_sequencial_otimizada(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(busca_sequencial_otimizada(lista, 3, 0, len(lista)), 2)
    
    def test_elemento_nao_encontrado(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(busca_sequencial_otimizada(lista, 6, 0, len(lista)), -1)
    
    def test_lista_vazia(self):
        lista = []
        self.assertEqual(busca_sequencial_otimizada(lista, 5, 0, len(lista)), -1)

if __name__ == '__main__':
        unittest.main()