def classificar_jogo(classificacao):
    if classificacao == 0:
        return "Livre"
    if classificacao < 16:
        return "Recomendado para Adolescentes"
    if classificacao == 18:
        return "Exclusivo para Adultos"
    return f"Classificação indicativa: {classificacao} anos"
