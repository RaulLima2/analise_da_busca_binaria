"""
This module contains a binary search algorithm implementation.

The binary search algorithm performs a search on a sorted array to find the index of a given key.

Example usage:

  vetor = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  chave = 5
  resultado = busca_binaria(vetor, chave, 0, len(vetor) - 1)
  print(f"The index of {chave} is {resultado}")
"""

import numpy as np

def busca_binaria(vetor:np.ndarray, chave:int, esquerda:int, direita:int) -> int:
    """
    Perform binary search on a sorted array to find the index of a given key.

    Args:
      vetor (np.ndarray): The sorted array to be searched.
      chave (int): The key to be searched for.
      esquerda (int): The leftmost index of the search range.
      direita (int): The rightmost index of the search range.

    Returns:
      int: The index of the key in the array, or 0 if the key is not found.
    """
    inicio:int = esquerda
    fim:int = direita
    while inicio <= fim:
        meio:int = (inicio + fim) // 2
        if vetor[meio] == chave:
            return meio
        if vetor[meio] < chave:
            inicio:int = meio + 1
        if vetor[meio] > chave:
            fim:int = meio - 1
    return 0
