import numpy as np

def busca_binaria(chave:int, vetor:np.ndarray, esquerda:int, direita:int) -> int:
  esquerda:int = 0
  direita:int = len(vetor) - 1
  while direita >= esquerda:
    meio:int = int((esquerda + direita)//2)
    if vetor[meio] == chave:
      return meio
    elif vetor[meio] > chave:
      direita:int = meio - 1
    elif vetor[meio] < chave:
      esquerda:int = meio + 1
  return -1
