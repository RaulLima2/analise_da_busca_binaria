import numpy as np

def busca_sequencial_otimizada(chave:int, vetor:np.ndarray)->int:
    for index, item in enumerate(vetor):
        if item < chave:
            return -1
        elif item == chave:
            return index