preco=float(input("digite o preco do produto: "))
codigo=float(input("digite o codigo de origem: "))
if codigo == 1:
    procedencia = "Sul"
elif codigo == 2:
    procedencia = "Norte"
elif codigo == 3:
    procedencia = "Leste"
elif codigo == 4:
    procedencia = "Oeste"
elif codigo == 5 or codigo == 6:
    procedencia = "Nordeste"
elif codigo == 7 or codigo == 8 or codigo == 9:
    procedencia = "Sudeste"
elif 10 <= codigo <= 20:
    procedencia = "Centro-Oeste"
elif 25 <= codigo <= 30:
    procedencia = "Nordeste"
else:
    procedencia = "Importado"
print(f"\npreco: R$ {preco:.2f}")
print(f"procedencia: {procedencia}")