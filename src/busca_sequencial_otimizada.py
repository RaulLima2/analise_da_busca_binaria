import numpy as np

def busca_sequencial_otimizada(chave:int, vetor:np.ndarray)->int:
    for index, item in enumerate(vetor):
        if item > chave:
            break
        if item == chave:
            return index
    return -1