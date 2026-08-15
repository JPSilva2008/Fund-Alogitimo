# Guia de Estudos: Conceitos Fundamentais de Python

---

## 1. Módulo `math` (`import math`)
O módulo nativo **`math`** fornece funções matemáticas avançadas, como cálculo de raízes, potências, arredondamentos e constantes como o $\pi$.

```python
import math

# Principais funções e constantes:
raiz = math.sqrt(16)          # Raiz quadrada -> 4.0
potencia = math.pow(2, 3)      # Potência (2³) -> 8.0
piso = math.floor(3.9)        # Arredonda para baixo -> 3
teto = math.ceil(3.1)         # Arredonda para cima -> 4
fatorial = math.factorial(5)  # Fatorial (5!) -> 120

print(math.pi)  # Constante Pi -> 3.141592653589793
```

---

## 2. Estruturas Condicionais (`if`, `elif`, `else`)
Servem para controlar o fluxo do programa com base em condições lógicas que retornam `True` (Verdadeiro) ou `False` (Falso).

```python
nota = 8.5

if nota >= 9.0:
    print("Aprovado com distinção!")
elif nota >= 7.0:
    print("Aprovado!")
elif nota >= 5.0:
    print("Recuperação.")
else:
    print("Reprovado.")
```

---

## 3. Laço `for` e `for in range()`
Utilizado para iterar sobre sequências ou quando o número de repetições é conhecido previamente.

```python
# Sintaxe range(início, fim_exclusivo, passo)
for i in range(5):
    print(f"Contagem: {i}")  # Imprime de 0 a 4

for numero in range(1, 10, 2):
    print(numero)  # Imprime: 1, 3, 5, 7, 9

# Iterando diretamente sobre uma coleção:
frutas = ["Maçã", "Banana", "Uva"]
for fruta in frutas:
    print(f"Fruta: {fruta}")
```

---

## 4. Laço `while` e `while True` com `break`
O laço `while` repete um bloco enquanto a condição for verdadeira. A instrução `while True` cria um loop contínuo que deve ser interrompido com `break`.

```python
# Estrutura enquanto simples
contador = 1
while contador <= 3:
    print(f"Tentativa {contador}")
    contador += 1

# Loop infinito controlado por interrupção
while True:
    comando = input("Digite 'sair' para encerrar: ")
    if comando.lower() == "sair":
        print("Saindo do programa...")
        break  # Encerra o laço
```

---

## 5. Listas (`[]`)
Coleções **ordenadas** e **mutáveis** que permitem modificar, adicionar e remover elementos.

```python
frutas = ["Maçã", "Banana", "Laranja"]

# Principais métodos e operações:
frutas.append("Uva")         # Adiciona elemento ao final
frutas.insert(1, "Manga")    # Insere elemento na posição 1
frutas.remove("Banana")      # Remove elemento por valor
item = frutas.pop()          # Remove e retorna o último elemento
frutas[0] = "Morango"        # Altera elemento do índice 0
```

---

## 6. Tuplas (`()`)
Coleções **ordenadas** e **imutáveis**. Não é possível alterar, incluir ou excluir itens após sua criação.

```python
coordenadas = (10.5, -23.8)

# Acesso por índice
print(coordenadas[0])  # 10.5

# Desempacotamento
latitude, longitude = coordenadas

# Tentar alterar gera TypeError:
# coordenadas[0] = 15.0
```

---

## 7. Dicionários (`{}`)
Coleções **mutáveis** que armazenam dados no formato de pares **Chave: Valor**.

```python
aluno = {
    "nome": "Lucas",
    "idade": 20,
    "curso": "Engenharia"
}

# Acesso e Atualização
print(aluno["nome"])     # "Lucas"
aluno["nota"] = 9.5       # Adiciona nova chave
aluno["idade"] = 21       # Atualiza chave existente

# Iteração sobre chaves e valores
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
```

---

## 8. Resumo das Estruturas de Dados

| Estrutura | Sintaxe | Mutável? | Ordenada? | Acesso aos Dados |
| :--- | :--- | :--- | :--- | :--- |
| **Lista** | `[1, 2, 3]` | Sim | Sim | Pelo índice (`lista[0]`) |
| **Tupla** | `(1, 2, 3)` | Não | Sim | Pelo índice (`tupla[0]`) |
| **Dicionário** | `{"chave": "valor"}` | Sim | Sim | Pela chave (`dic["chave"]`) |