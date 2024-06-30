"""
This module contains a function for performing an optimized sequential search on a given array.
"""
import numpy as np


def busca_sequencial_otimizada(vetor: np.ndarray, chave: int, inicio: int, final: int) -> int:
    """
    Perform an optimized sequential search on a given array.

    Args:
        vetor (np.ndarray): The array to be searched.
        chave (int): The value to be searched for.
        inicio (int): The starting index of the search range.
        final (int): The ending index of the search range.

    Returns:
        int: The index of the first occurrence of the value in the array, or -1 if not found.
    """
    for index in range(inicio, final):
        if vetor[index] > chave:
            break
        if vetor[index] == chave:
            return index
    return -1
