from busca_binaria import busca_binaria
from exibir_jogo import exibir_jogo
from ordenar_jogos import ordenar_jogos


def buscar_jogo(titulos, dados):
    ordenar_jogos(titulos, dados)
    titulo_procurado = input("Digite o título do jogo que deseja buscar: ").strip()
    indice = busca_binaria(titulos, titulo_procurado)

    if indice != -1:
        print("\nJogo encontrado:")
        exibir_jogo(titulos[indice], dados[indice])
    else:
        print("Jogo não encontrado no catálogo.")
