import numpy as np

def busca_binaria(chave:int, esquerda:int, direita:int, vetor:np.ndarray)->int:
    meio:int = int((esquerda + direita)//2)

    if direita >= esquerda:
        if vetor[meio] > chave:
            return busca_binaria(chave, vetor, 0, meio - 1)
        elif vetor[meio] < chave:
            return busca_binaria(chave, vetor, meio + 1, len(vetor))
        elif vetor[meio] == chave:
            return meio
    else:
        return 0
