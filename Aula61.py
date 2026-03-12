n = int(input("Dgite um numero: "))
acumulador = 0
qtd_numeros = 0
while(n!=0):
    acumulador += n
    qtd_numeros +=1
    n = int(input("Dgite um numero: "))
print(acumulador/qtd_numeros)
