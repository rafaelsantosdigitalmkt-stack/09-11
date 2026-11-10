def busca_binaria(titulos, titulo_procurado):
    procurado = titulo_procurado.casefold()
    inicio = 0
    fim = len(titulos) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        atual = titulos[meio].casefold()
        if atual == procurado:
            return meio
        if atual < procurado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1
