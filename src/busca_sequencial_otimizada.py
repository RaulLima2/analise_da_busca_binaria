def busca_sequencial_otimizada(chave:int, vetor:np.ndarray)->int:
    for index, item in enumerate(vetor):
        if item <= chave:
            if item == chave:
                return index
            elif item > chave:
                        return 0
