## AULA 07 - NO CASO É A 08 - "FUNÇÕES" ------ TA NO DRIVE

## O que são Funções

## Funções são blocos de código reutilizáveis.
## Elas permitem organizar melhor o programa e evitar repetição de código.
## Uma função executa uma tarefa específica e pode ser usada várias vezes no programa.

## Por que usar Funções

## Usar funções ajuda a:
## Organizar melhor o código
## Reutilizar lógica
## Facilitar manutenção
## Tornar o código mais legível

## Estrutura de uma Função

## Em Python usamos a palavra def para criar uma função.
## Estrutura:

## def nome_da_funcao():
## código

## EXISTEM FUNÇÕES INUMERAS SÓ QUE INTERNAS DO PYTHON, NO CASO DESSA FUNÇÃO(def), ELA SERVE PARA CRIARMOS AS NOSSAS PROPRIAS FUNÇÕES 

## Função com Parâmetros

## Parâmetros são valores que a função recebe para trabalhar.
## Estrutura:

## def nome_funcao(parametro):
## código

## Exemplo com Parâmetro

## def saudacao(nome):
## print("Olá", nome)

## Chamando a função:

## saudacao("Maria")
## saudacao("Carlos")

## Função com Dois Parâmetros

## Uma função pode receber vários parâmetros.

## def soma(a, b):
## resultado = a + b
## print(resultado)

## Chamando a função:

## soma(5, 3)

## O que é Retorno

## O retorno permite que a função envie um valor de volta para o programa.
## Para isso usamos a palavra return .

## Exemplo com Retorno

## def soma(a, b):
## return a + b

## Usando o retorno:

## resultado = soma(4, 6)
## print(resultado)

## Diferença entre Print e Return

## print()
## Mostra o resultado na tela.

## return
## Devolve o valor para ser usado em outra parte do programa.
## Exemplo:

## def soma(a, b):
## return a + b

## resultado = soma(2, 3)
## print(resultado)

## Função com Condição

## Funções também podem usar estruturas de decisão.

## def verificar_idade(idade):
## if idade >= 18:
## return "Maior de idade"
## else:
## return "Menor de idade"

## Uso:

## print(verificar_idade(20))

## O que é Escopo

## Escopo define onde uma variável pode ser usada.
## Existem dois tipos principais:
## escopo local
## escopo global

## Escopo Local

## Uma variável criada dentro de uma função só existe dentro dela.

## def exemplo():
## x = 10
## print(x)

## A variável x

## não pode ser usada fora da função.

## Escopo Global

## Variáveis criadas fora das funções podem ser usadas no programa inteiro.

## x = 10

## def mostrar():
## print(x)
## mostrar()

## Exemplo Misturando Escopos

## x = 5

## def exemplo():
## x = 10
## print("Dentro da função:", x)
## exemplo()
## print("Fora da função:", x)

## Resultado:

## Dentro da função → 10
## Fora da função → 5