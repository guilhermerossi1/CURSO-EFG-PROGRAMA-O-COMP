## BLOCO DE CÓDIGOS E ESTRUTURAS CONDICIONAIS

# EXEMPLO DA AULA:

idade = int(input ("Informe sua idade"))

if idade >= 18 and idade <= 59:
    print ("é um adulto")
elif idade >= 12 and idade <= 17:
    print ("é um adolescente")
elif idade >= 60 and idade <= 120:
    print ("é um idoso")
elif idade >= 1 and idade <= 11:
    print ("é uma criança")
else:
    print ("idade inválida")


## ele vai executar o bloco de códigos, pq os "ifs" e "elifs" estão na mesma sequencia de linha
## ex:  if......                        ----------------- assim ta certo
##      elif..... 

##          if....                      --------------- assim ta errado
##             elif....