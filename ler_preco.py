def ler_preco(mensagem):
    while True:
        try:
            preco = float(input(mensagem).replace(",", "."))
            if preco < 0:
                print("O preço não pode ser negativo.")
                continue
            return preco
        except ValueError:
            print("Digite um preço válido.")
