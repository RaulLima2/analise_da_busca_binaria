"""
This module contains a function for performing a sequential search in an array.
"""
import numpy as np

def busca_sequencial(vetor:np.ndarray, chave:int, inicio:int, final:int)->int:
    """
    This function performs a sequential search in an array.
    Parameters:
    vetor:np.ndarray -> The array to be searched.
    chave:int -> The value to be searched.
    inicio:int -> The initial index of the search.
    final:int -> The final index of the search.
    Returns:
    int -> The index of the key in the array.
    """
    for index in range(inicio, final):
        if vetor[index] == chave:
            return index
    return -1
