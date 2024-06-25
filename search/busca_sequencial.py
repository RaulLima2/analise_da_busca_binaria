"""
This module contains a function for performing a sequential search in an array.
"""
import numpy as np

def busca_sequencial(chave:int, vetor:np.ndarray)->int:
    """
    Performs a sequential search for a given key in an array.

    Parameters:
    chave (int): The key to search for.
    vetor (np.ndarray): The array to search in.

    Returns:
    int: The index of the key in the array if found, otherwise -1.
    """
    for index, item in enumerate(vetor):
        if item == chave:
            return index
    return -1
