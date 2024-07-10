
def classificacaoDoHeroi():
    nome = input("Por favor, insira o nome do herói: ")
    xp = int(input("Por favor, insira a quantidade de XP: "))

    if xp <=1000:
        print("O Herói de nome",nome,"está no nível de Ferro")
    elif xp >= 1001 and xp <= 2000:
            print("O Herói de nome",nome,"está no nível de Bronze")
    elif xp >= 2001 and xp <= 5000:
        print("O Herói de nome",nome,"está no nível de Prata")
    elif xp >= 5001 and xp <= 7000:
        print("O Herói de nome",nome,"está no nível de Ouro")
    elif xp >= 7001 and xp <= 8000:
        print("O Herói de nome",nome,"está no nível de Platina")
    elif xp >= 8001 and xp <= 9000:
        print("O Herói de nome",nome,"está no nível de Ascendente")
    elif xp >= 9001 and xp <= 10000:
        print("O Herói de nome",nome,"está no nível de Imortal")
    elif xp >= 10001:
        print("O Herói de nome",nome,"está no nível de Radiante")

classificacaoDoHeroi()
