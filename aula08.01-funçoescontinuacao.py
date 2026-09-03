## Estruturas de Repetição

## for, while, break e continue

## O que são Estruturas de Repetição

## Estruturas de repetição permitem executar um bloco de código várias vezes.
## Elas são usadas quando queremos repetir uma ação sem precisar escrever o mesmo
## código várias vezes.
## Exemplos do dia a dia:
## Contar de 1 até 10
## Mostrar uma lista de nomes
## Repetir uma pergunta até o usuário digitar algo válido

## Principais Estruturas de Repetição

## Em Python usamos principalmente:
## for
## while

## Também podemos controlar o comportamento do loop com:
## break
## continue

## Estrutura FOR

## O for é usado quando sabemos quantas vezes queremos repetir algo.
## Estrutura:

## for variável in sequência:
## código

## Exemplo com FOR

## for i in range(5):
## print(i)

## Saída:

## 0
## 1
## 2
## 3
## 4

## Usando Range

## A função range() cria uma sequência de números.
## Exemplo:

## for i in range(1, 6):
## print(i)

## Saída:

## 1
## 2
## 3
## 4
## 5

## Exemplo com Lista

## O for também pode percorrer listas.

## nomes = ["Ana", "Carlos", "João"]
## for nome in nomes:
## print(nome)

## Estrutura WHILE

## O while executa um bloco de código enquanto uma condição for verdadeira.
## Estrutura:

## while condição:
## código

## Exemplo com WHILE

## contador = 1

## while contador <= 5:
## print(contador)
## contador += 1

## Esse código conta de 1 até 5.

## Exemplo com Input

## senha = ""

## while senha != "python":
## senha = input("Digite a senha: ")

## O programa continua pedindo a senha até o usuário acertar.

## Usando BREAK

## O break serve para interromper o loop imediatamente.
## Exemplo:

## while True:
## numero = int(input("Digite um número (0 para sair): "))
## if numero == 0:
## break

## print("Número digitado:", numero)

## Quando o usuário digita 0, o loop é encerrado.

## Usando CONTINUE

## O continue pula para a próxima repetição do loop.
## Exemplo:

## for i in range(1, 6):
## if i == 3:
## continue

## print(i)

## Saída:
## 1
## 2
## 4
## 5

## Comparação FOR vs WHILE

## FOR:

## Usado quando sabemos quantas repetições queremos
## Muito usado com listas e sequências
## WHILE:

## Usado quando não sabemos quantas vezes será necessário repetir
## Depende de uma condição