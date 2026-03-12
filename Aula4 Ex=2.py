x1 = int(input("Digite o primiero numero: "))
x2 = int(input("Digite o segundo numero: "))
x3 = int(input("Digite o terceiro numero: "))

if x1 >= x2 and x1>= x3:
    maior = x1
    if x2 >= x3:
        meio = x2
        menor = x3
    else:
        meio = x3
        menor = x2

elif x2 >= x1 and x2>= x3:
    maior = x2
    if x1 >= x3:
        meio = x1
        menor = x3
    else:
        meio = x3
        menor = x1
else:
    maior = x3
    if x1 >= x2:
        meio = x1
        menor = x2
    else:
        meio = x2
        menor = x1
print("nOrdem decrescente")
print(maior , meio , menor)

