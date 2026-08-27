## O que são Estruturas de Dados?

## Estruturas de dados são usadas para armazenar vários valores em uma única variável.
## Elas ajudam a organizar informações dentro do programa.

## Principais estruturas no Python:
## Listas
## Tuplas
## Dicionários
## Conjuntos (Sets)

## 1. Listas (List)

## Listas armazenam vários valores em uma única variável.

## Elas são definidas usando colchetes [ ] ou usando o comando "list".

## numeros = [10, 20, 30, 40]
## print(numeros)

## 1.1 - Características das Listas

## Permitem modificar valores
## Permitem valores repetidos
## Podem armazenar diferentes tipos de dados

## dados = ["Ana", 20, 1.65, True]
## print(dados)

## 1.2 - Acessando Elementos da Lista

## O índice sempre começa em 0.

## frutas = ["maçã", "banana", "laranja"]
## print(frutas[0])
## print(frutas[1])
## print(frutas[2])

## 1.3 - Funções e Métodos das Listas

## Principais métodos usados em listas

## Método                           Descrição                             Exemplo
## append()                         adiciona elemento no final             lista.append(5)
## insert()                         adiciona em posição específica         lista.insert(1, 10)
## remove()                         remove valor/nome específico                lista.remove(3)
## pop()                            remove elemento por índice             lista.pop(0)
## clear()                          remove todos elementos                 lista.clear()
## index()                          retorna índice do valor                lista.index(20)
## count()                          conta ocorrências                      lista.count(5)
## sort()                           ordena lista                           lista.sort()
## reverse()                        inverte lista                          lista.reverse()
## copy()                           copia lista                            nova_lista =lista.copy()

## exemplos LISTA

nome = ["André"]

nome.insert (1, "João")

print (nome)

## 2. Tuplas (Tuple)

## Tuplas são semelhantes às listas, mas não podem ser modificadas.
## Usam parênteses ( ) .

## cores = ("vermelho", "azul", "verde")
## print(cores)

## 2.1 Características das Tuplas

## Não podem ser alteradas
## São mais seguras para dados fixos
## Permitem repetição de valores

## 2.2 - Métodos das Tuplas

## Tuplas possuem poucos métodos.

## Método Descrição Exemplo
## count() conta quantas vezes um valor aparece tupla.count(2)
## index() retorna posição do valor tupla.index(5)


## 3. Dicionários (Dictionary)

## Dicionários armazenam dados em pares de chave e valor.
## Usam chaves { } .

## pessoa = {
## "nome": "Ana",
## "idade": 20,
## "cidade": "Goiânia"
## }
## print(pessoa)

## Funções e Métodos dos Dicionários

## Método                           Descrição                           Exemplo
## keys()                           retorna todas as chaves             d.keys()
## values()                         etorna todos valores                d.values()
## items()                          retorna chave e valor               d.items()
## get()                            acessa valor com segurança          d.get("nome")
## update()                         atualiza dicionário                 d.update({"idade":21})
## pop()                            remove chave                        d.pop("idade")
## popitem()                        remove último item                  d.popitem()
## clear()                          limpa dicionário                    d.clear()
## copy()                           copia dicionário novo =             d.copy()

## Exemplo com Dicionário

pessoa = {"nome":"Ana",
          "idade":20}

pessoa["cidade"] = "Goiânia"

print(pessoa.keys())
print(pessoa.values())