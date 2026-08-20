## Parte 1.1 — True ou False

## Analise cada expressão e indique se o resultado será True ou False :

## No Expressão Resultado
## 1 10 > 5 ______
## 2 8 < 3 ______
## 3 10 == 10 ______
## 4 7 != 7 ______
## 5 15 >= 15 ______

## 1
numero = 10
numero2 = 5
print (numero > numero2) ## True

## 2
numero = 8
numero2 = 3
print (numero < numero2) ## False

## 3
numero = 10
numero2 = 10
print (numero == numero2) ## True

## 4
numero = 7
numero2 = 7
print (numero != numero2) ## False

## 5
numero = 15
numero2 = 15
print (numero >= numero2) ## True

## Parte 1.2 — True ou False

## Analise cada expressão e indique se o resultado será True ou False :

## No Expressão Resultado
## 6 20 <= 10 ______
## 7 5 != 8 ______
## 8 12 < 12 ______
## 9 18 >= 10 ______
## 10 25 == 30 ______

## 6
numero = 20
numero2 = 10
print (numero <= numero2) ## False

## 7
numero = 5
numero2 = 8
print (numero != numero2) ## True

## 8
numero = 12
numero2 = 12
print (numero < numero2) ## False

## 9
numero = 18
numero2 = 10
print (numero >= numero2) ## True

## 10
numero = 25
numero2 = 30
print (numero == numero2) ## False

## Parte 2.1 - "Permissão para Dirigir"

## Uma pessoa pode dirigir se:
## Tiver 18 anos ou mais
## E possuir carteira de motorista

idademotorista = 16
temcarteira = True
print (idademotorista >= 18 and temcarteira) 

## Parte 2.2 - "Aprovação do Aluno"

## Um aluno será aprovado se:
## Sua nota for maior ou igual a 6
## E sua frequência for maior ou igual a 75%

notaaluno = 10
frequencia = 80
aprovacao = notaaluno >= 6 and frequencia >= 75
print (aprovacao)

## Parte 2.3 - "Desconto"

## Um cliente terá direito a desconto se:
## Possuir cartao da loja
## OU realizar uma compra acima de R$ 500,00

temcartao = False
valorcompra = 600
desconto = temcartao or valorcompra > 500
print (desconto) 

## Parte 2.4 - "Acesso ao Sistema"

## Um usuário poderá acessar o sistema se:
## Estiver ativo
## E tiver informado a senha corretamente

usuarioativo = True
senhacorreta = True
acesso = usuarioativo and senhacorreta
print (acesso)

## Parte 2.5 - "Compra de Produto"

## Um cliente poderá comprar um produto se:
## Tiver dinheiro suficiente
## E o produto estiver em estoque

dinheiro = 100
preco = 80
estoque = 5
compraproduto = dinheiro >=80 and estoque >= 0
print (compraproduto)

## Parte 2.6 - "Entrada em uma Festa"
## Uma pessoa poderá entrar em uma festa se:
## Tiver idade maior ou igual a 18
## OU estiver acompanhada de um responsável 

idade = 16
acompanhado = True
entrada = idade >=18 or acompanhado
print (entrada)

## Parte 2.7 - "Conta Bloqueada"

## Um usuário poderá acessar sua conta somente se não estiver bloqueado.
## Dados:
## bloqueado = False
## Tarefa: Utilize o operador not 

bloqueado = False
acesso = not bloqueado
print (acesso) 

## Parte 2.8 - "Contratação"

## Uma empresa poderá contratar uma pessoa se:
## Tiver 18 anos ou mais
## E tiver experiência OU possuir um curso na área

idade = 20
experiencia = False
curso = True
contratacao = idade >= 18 and experiencia or curso
print (contratacao)

## Parte 2.9 - "Empréstimo"
## Um banco permitirá que uma pessoa faça um empréstimo se:
## Tiver salário maaior ou igual a R$ 2000,00
## E não estiver negativada

salario = 2500
negativado = False
emprestimo = salario >= 2000 and not negativado
print (emprestimo)

## Parte 2.10 - "Desafio Final"

## Uma empresa possui as seguintes regras para contratação:
##Idade deve ser maior ou igual a 18
##A pessoa deve ter experiência OU formação
## E NÃO pode estar com o cadastro bloqueado

idade = 22
experiencia = False
formaçao = True
bloqueado = False
contratacao = idade >= 18 and (experiencia or formaçao) and not bloqueado
print (contratacao)

