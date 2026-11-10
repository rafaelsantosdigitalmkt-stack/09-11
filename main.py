from cadastrar_jogos import cadastrar_jogos
from buscar_jogo import buscar_jogo
from configuracao import QUANTIDADE_JOGOS
from exibir_menu import exibir_menu
from listar_jogos import listar_jogos
from ordenar_jogos import ordenar_jogos


titulos = [""] * QUANTIDADE_JOGOS
dados = [[0, 0, 0.0] for _ in range(QUANTIDADE_JOGOS)]
cadastrar_jogos(titulos, dados)

opcao = ""
while opcao != "0":
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case "1":
            listar_jogos(titulos, dados)
        case "2":
            ordenar_jogos(titulos, dados)
            listar_jogos(titulos, dados)
        case "3":
            buscar_jogo(titulos, dados)
        case "0":
            print("Programa encerrado.")
        case _:
            print("Opção inválida. Escolha 0, 1, 2 ou 3.")
