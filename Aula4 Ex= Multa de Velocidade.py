limite = float(input("Digite a velocidade da via: "))
velocidade = float(input("Digite a velocidade do carro: "))
if velocidade <= limite:
    print("velocidade do carro esta dentro da velocidade da via")
else:
    porcentagem = ((velocidade - limite)/limite) * 100
    print(f"velocidade{porcentagem:.0f}% acima do limite")
    if porcentagem <= 20:
        print("Penalidade: Multa de R$130,16.")
        print("Pontuação: 4 pontos na CNH.")
    elif porcentagem <= 50:
        print("Penalidade: Multa de R$195,23.")
        print("Pontuação: 5 pontos na CNH.")
    else:
        print("Penalidade:Multa de R$880,41.")
        print("Pontuação:7 pontos na CNH.")

    