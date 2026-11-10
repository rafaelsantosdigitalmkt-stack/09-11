def ler_titulo():
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("O título não pode ficar vazio.")
