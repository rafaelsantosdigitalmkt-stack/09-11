from configuracao import ANO_ATUAL
from ler_inteiro import ler_inteiro


def validar_ano():
    while True:
        ano = ler_inteiro("Ano de lançamento: ")
        if ano < 1:
            print("O ano deve ser maior que zero.")
        elif ano > ANO_ATUAL:
            print(f"O ano não pode ser futuro (máximo: {ANO_ATUAL}).")
        else:
            return ano
