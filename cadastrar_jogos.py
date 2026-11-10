from configuracao import QUANTIDADE_JOGOS
from ler_preco import ler_preco
from ler_titulo import ler_titulo
from validar_ano import validar_ano
from validar_classificacao import validar_classificacao


def cadastrar_jogos(titulos, dados):
    print(f"Cadastro de {QUANTIDADE_JOGOS} jogos")
    for indice in range(QUANTIDADE_JOGOS):
        print(f"\nJogo {indice + 1}")
        titulos[indice] = ler_titulo()
        ano = validar_ano()
        classificacao = validar_classificacao()
        preco = ler_preco("Preço base da diária (R$): ")
        dados[indice] = [ano, classificacao, preco]
