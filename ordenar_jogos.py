def ordenar_jogos(titulos, dados):
    quantidade = len(titulos)
    for limite in range(quantidade - 1, 0, -1):
        houve_troca = False
        for indice in range(limite):
            if titulos[indice].casefold() > titulos[indice + 1].casefold():
                titulos[indice], titulos[indice + 1] = (
                    titulos[indice + 1],
                    titulos[indice],
                )
                dados[indice], dados[indice + 1] = dados[indice + 1], dados[indice]
                houve_troca = True
        if not houve_troca:
            break
    print("\nJogos ordenados em ordem alfabética.")
