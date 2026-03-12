x = int(input("Digite um numero: "))
Primo = True
for i in range(2,x):
    if x %i ==0:
        Primo=False
if Primo:
    print("É primo")
else:
    print("Não é primo")

