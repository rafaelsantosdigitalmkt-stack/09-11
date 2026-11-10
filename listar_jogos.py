from exibir_jogo import exibir_jogo


def listar_jogos(titulos, dados):
    print("\n=== Catálogo de jogos ===")
    for indice in range(len(titulos)):
        exibir_jogo(titulos[indice], dados[indice])
