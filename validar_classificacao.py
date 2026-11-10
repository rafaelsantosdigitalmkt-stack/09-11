from ler_inteiro import ler_inteiro


def validar_classificacao():
    while True:
        classificacao = ler_inteiro("Classificação indicativa (0 a 18): ")
        if 0 <= classificacao <= 18:
            return classificacao
        print("A classificação deve estar entre 0 e 18.")
