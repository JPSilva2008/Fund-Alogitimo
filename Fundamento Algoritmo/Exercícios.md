# Lista de Exercícios: Programação em Python

---

### Questão 1: Módulo `math` e Condicionais (`if`, `elif`, `else`)
Escreva um programa em Python que realize cálculos geométricos com base no raio de um círculo:
* **a)** Importe o módulo `math`.
* **b)** Solicite ao usuário o raio $r$ e um número de opção ($1$ para calcular a área, $2$ para o perímetro e $3$ para calcular a raiz quadrada do raio usando `math.sqrt`).
* **c)** Utilizando a estrutura `if`, `elif` e `else`, exiba o resultado correspondente utilizando `math.pi`. Trate opções inválidas com uma mensagem de alerta.

---

### Questão 2: Repetição com `for` e `range()`
A função `range()` é utilizada para gerar sequências numéricas em laços de repetição.
* **a)** Escreva um código utilizando `for i in range(...)` que imprima todos os números pares de $10$ até $50$ (inclusive).
* **b)** Escreva um código que calcule e exiba a soma de todos os números ímpares no intervalo de $1$ a $100$.

---

### Questão 3: Manipulação de Listas
Dada a lista inicial `numeros = [12, 45, 7, 23, 89, 34, 56, 3]`:
* **a)** Adicione o número $99$ ao final da lista com `.append()` e o número $1$ na primeira posição (índice $0$) com `.insert()`.
* **b)** Remova o menor elemento da lista utilizando a função `min()` e o método `.remove()`.
* **c)** Escreva um laço `for` que percorra a lista atualizada e crie uma nova lista contendo apenas os valores maiores que $30$.

---

### Questão 4: Tuplas e Imutabilidade
Diferente das listas, as tuplas são estruturas de dados imutáveis.
* **a)** Dada a tupla `ponto_3d = (10, 20, 30)`, tente alterar o valor do primeiro elemento para $15$ e explique o erro gerado pelo Python.
* **b)** Realize o **desempacotamento** da tupla `aluno = ("Maria", 8.5, "Aprovado")` em três variáveis separadas (`nome`, `nota`, `status`) e exiba seus valores na tela.

---

### Questão 5: Dicionários (Chaves e Valores)
Dicionários armazenam dados no formato chave-valor.
* **a)** Crie um dicionário chamado `produto` contendo as chaves `"nome"`, `"preco"` e `"estoque"`.
* **b)** Atualize o preço do produto aplicando $10\%$ de desconto e adicione uma nova chave chamada `"categoria"`.
* **c)** Utilize um laço `for` junto ao método `.items()` para iterar sobre o dicionário e imprimir cada chave acompanhada de seu respectivo valor.

---

### Questão 6: Estrutura de Repetição `while`
Escreva um programa em Python utilizando a estrutura `while`:
* Solicite que o usuário digite uma senha. O programa deve continuar pedindo a senha enquanto o valor digitado for diferente da senha correta `"python123"`.
* Exiba uma mensagem de acesso liberado assim que o usuário acertar a senha, mostrando também a quantidade de tentativas incorretas realizadas.

---

### Questão 7: Loop Infinito com `while True` e `break`
O laço `while True` permite criar repetições indeterminadas que são interrompidas por condições específicas.
* Escreva um programa que leia sucessivos números inteiros digitados pelo usuário.
* Utilize a instrução `break` para encerrar o loop quando o usuário digitar o número $0$.
* Ao final do programa, exiba a quantidade de números digitados (desconsiderando o zero) e a soma total deles.

---

### Questão 8: Iterando sobre Estruturas Compostas (Lista de Dicionários)
Considere a seguinte lista de dicionários representando uma turma de alunos:

```python
turma = [
    {"nome": "Ana", "nota": 9.0},
    {"nome": "Bruno", "nota": 5.5},
    {"nome": "Carla", "nota": 7.5},
    {"nome": "Diego", "nota": 4.0}
]
```

* **a)** Escreva um laço `for` que percorra a lista `turma` e imprima o nome de cada aluno acompanhado da situação: `"Aprovado"` (nota $\ge 7.0$) ou `"Reprovado"` (nota $< 7.0$) usando `if`/`else`.
* **b)** Calcule e exiba a média geral das notas da turma.

---

### Questão 9: Comparação entre Lista, Tupla e Dicionário
Responda de forma direta sobre o uso das estruturas de dados em Python:
* **a)** Em qual situação prática é preferível utilizar uma **Tupla** em vez de uma **Lista**?
* **b)** Qual é a principal vantagem de buscar um valor em um **Dicionário** através de uma chave em comparação com procurar um elemento em uma **Lista**?

---

### Questão 10: Desafio Integrado (Menu Interativo)
Crie um programa completo em Python que combine os conceitos estudados:
* Implemente um loop `while True` que exiba um menu com as seguintes opções:
  1. **Calcular Fatorial** (utilize a função `math.factorial`).
  2. **Cadastrar Pessoa** (solicite nome e idade e armazene como dicionário em uma lista global).
  3. **Listar Pessoas Cadastradas** (percorra a lista com `for` exibindo nome e idade).
  4. **Sair**.
* Use `if`, `elif` e `else` para tratar a opção escolhida e `break` para encerrar a execução na opção 4.