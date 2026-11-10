from calcular_diaria import calcular_diaria
from classificar_jogo import classificar_jogo
from obter_categoria import obter_categoria


def exibir_jogo(titulo, dados_jogo):
    ano, classificacao, preco_base = dados_jogo
    preco_final, taxa = calcular_diaria(ano, preco_base)

    print(f"\nTítulo: {titulo}")
    print(f"Ano de lançamento: {ano}")
    print(f"Classificação: {classificar_jogo(classificacao)}")
    print(f"Preço base da diária: R$ {preco_base:.2f}")
    if taxa:
        print(f"Taxa de Lançamento Aplicada: R$ {taxa:.2f}")
    print(f"Preço final da diária: R$ {preco_final:.2f}")
    print(obter_categoria(preco_final))
