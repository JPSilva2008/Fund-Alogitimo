## 2.3 Gabarito de Python

```python
# Questão 1
import math
raio = float(input("Raio: "))
op = int(input("1-Área, 2-Perímetro, 3-Raiz: "))
if op == 1:
    print(f"Área: {math.pi * raio**2:.2f}")
elif op == 2:
    print(f"Perímetro: {2 * math.pi * raio:.2f}")
elif op == 3:
    print(f"Raiz: {math.sqrt(raio):.2f}")
else:
    print("Opção inválida!")

# Questão 2
for i in range(10, 51, 2):
    print(i, end=" ")
soma_imp = sum(range(1, 101, 2))
print(f"\nSoma ímpares: {soma_imp}")

# Questão 3
numeros = [12, 45, 7, 23, 89, 34, 56, 3]
numeros.append(99)
numeros.insert(0, 1)
numeros.remove(min(numeros))
maiores_30 = [x for x in numeros if x > 30]
print(f"Lista tratada: {numeros}")
print(f"Maiores que 30: {maiores_30}")

# Questão 4
aluno = ("Maria", 8.5, "Aprovado")
nome, nota, status = aluno
print(f"{nome} - {nota} - {status}")

# Questão 5
produto = {"nome": "Notebook", "preco": 3000.0, "estoque": 15}
produto["preco"] *= 0.90
produto["categoria"] = "Eletrônicos"
for k, v in produto.items():
    print(f"{k}: {v}")

# Questão 6
tentativas = 0
while input("Senha: ") != "python123":
    tentativas += 1
    print("Incorreta!")
print(f"Acesso liberado! Erros: {tentativas}")

# Questão 7
qtd, soma = 0, 0
while True:
    n = int(input("Número (0 para sair): "))
    if n == 0:
        break
    soma += n
    qtd += 1
print(f"Qtd: {qtd}, Soma: {soma}")

# Questão 8
turma = [
    {"nome": "Ana", "nota": 9.0},
    {"nome": "Bruno", "nota": 5.5},
    {"nome": "Carla", "nota": 7.5},
    {"nome": "Diego", "nota": 4.0}
]
soma_notas = 0
for a in turma:
    soma_notas += a["nota"]
    sit = "Aprovado" if a["nota"] >= 7.0 else "Reprovado"
    print(f"{a['nome']}: {sit}")
print(f"Média: {soma_notas / len(turma):.2f}")

# Questão 10
import math
pessoas = []
while True:
    print("\n1.Fatorial | 2.Cadastrar | 3.Listar | 4.Sair")
    op = input("Opção: ")
    if op == "1":
        n = int(input("Número: "))
        print(f"Fatorial: {math.factorial(n)}")
    elif op == "2":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        pessoas.append({"nome": nome, "idade": idade})
    elif op == "3":
        for p in pessoas:
            print(f"Nome: {p['nome']} | Idade: {p['idade']}")
    elif op == "4":
        break
```