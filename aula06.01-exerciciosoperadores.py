## Fazer as operações de comparação usando "IF" e "ELSE";
## da atividade 2 à 6 (que estão no DRIVE da matéria);

## EXERCÍCIO 2 — 

## Um aluno será aprovado se:
## Sua nota for maior ou igual a 6
## E sua frequência for maior ou igual a 75%

## Dados:
## nota = 7
## frequencia = 80

nota = 7
frequencia = 80

if(nota >= 6 and frequencia >= 70):
    print ("Aprovado!")
else:
    print ("Reprovado!")

## EXERCICIO 3

## Desconto

## Um cliente receberá desconto se:

## Possuir cartão da loja
## OU realizar uma compra acima de R$ 500

## Dados:
## tem_cartao = False
## valor_compra = 600

tem_cartao = False
valor_compra = 600

if (tem_cartao == True or valor_compra >= 500): 
    print ("Tem desconto")
else: 
    print ("Não tem desconto")

## EXERCÍCIO 4

## Acesso ao Sistema

## Um usuário poderá acessar o sistema se:
## Estiver ativo
## E tiver informado a senha corretamente

## Dados:

## usuario_ativo = True
## senha_correta = True

usuario_ativo = True
senha_correta = True

if (usuario_ativo == True and senha_correta == True):
    print ("Bem vindo ao sistema!")
else:
    print ("Acesso negado!")


## EXERCÍCIO 5
 
## Compra de Produto

## Uma pessoa poderá comprar um produto se:
## Tiver dinheiro suficiente
## E houver produto no estoque
## Dados:

## dinheiro = 100
## preco = 80
## estoque = 5

dinheiro = 100
preco = 80
estoque = 5

if (dinheiro >= preco and estoque >= 0):
    print ("Agradecemos a sua preferência!")
else:
    print ("Compra negada")


## EXERCÍCIO 6

## Entrada em uma Festa

## Uma pessoa poderá entrar na festa se:
## Tiver 18 anos ou mais
## OU estiver acompanhada de um responsável
## Dados:

## idade = 16
## acompanhado = True

idade = 16
acompanhado = True

if (idade >= 18 or acompanhado == True):
    print ("Entrada autorizada")
else:
    print ("Entrada negada")