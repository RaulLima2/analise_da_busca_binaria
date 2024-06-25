import unittest
from search.busca_sequencial_otimizada import busca_sequencial_otimizada

class TestBuscaSequencialOtimizada(unittest.TestCase):
    
    def test_busca_sequencial_otimizada(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(busca_sequencial_otimizada(lista, 3), 6)

    def test_busca_sequencial_otimizada(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(busca_sequencial_otimizada(lista, 3), 2)
    
    def test_elemento_nao_encontrado(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(busca_sequencial_otimizada(lista, 6), -1)
    
    def test_lista_vazia(self):
        lista = []
        self.assertEqual(busca_sequencial_otimizada(lista, 5), -1)