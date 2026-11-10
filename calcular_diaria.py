from configuracao import ANO_ATUAL


def calcular_diaria(ano, preco_base):
    taxa_lancamento = 5.0 if ano == ANO_ATUAL else 0.0
    return preco_base + taxa_lancamento, taxa_lancamento
