#create class unitest to test the function busca binaria, busca sequencial and busca sequencial otimizada
import unittest
import numpy as np
from src import busca_binaria, busca_sequencial, busca_sequencial_otimizada

class TestBusca(unittest.TestCase):

    def test_busca_binaria(self):
        tamanho_dos_vetores: list[int]  = [10**7]
        for tamanho in tamanho_dos_vetores:
            vetor:np.ndarray =  np.random.randint(tamanho - np.random.randint(0, tamanho), size=tamanho)
            vetor = sorted(vetor)
            chave:int = vetor[np.random.randint(0, tamanho - 1)]
            self.assertEqual(busca_binaria(chave,vetor, 0,len(vetor)), chave, "Busca binaria falhou")
            self.assertEqual(busca_binaria(chave,vetor), vetor[0])
            self.assertEqual(busca_binaria(chave,vetor), vetor[-1])
            self.assertEqual(busca_binaria(chave,vetor), vetor[len(vetor)//2])
    
    def test_busca_sequencial(self):
        tamanho_dos_vetores: list[int]  = [10**7]
        for tamanho in tamanho_dos_vetores:
            vetor:np.ndarray = np.arange(tamanho)
            chave:int = vetor[np.random.randint(0, tamanho - 1)]
            self.assertEqual(busca_sequencial(chave,vetor), chave, "Busca sequencial falhou")
            self.assertEqual(busca_sequencial(chave,vetor), vetor[len(vetor)//2])

    def test_busca_sequencial_otimizada(self):
        tamanho_dos_vetores: list[int]  = [10**7]
        for tamanho in tamanho_dos_vetores:
            vetor:np.ndarray = np.random.permutation(tamanho)
            vetor = sorted(vetor)
            chave:int = vetor[np.random.randint(0, tamanho - 1)]
            self.assertEqual(busca_sequencial_otimizada(chave,vetor), chave, "Busca sequencial otimizada falhou")
            self.assertEqual(busca_sequencial_otimizada(chave,vetor), vetor[0])
            self.assertEqual(busca_sequencial_otimizada(chave,vetor), vetor[-1])
    
if __name__ == '__main__':
    unittest.main()