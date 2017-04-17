import random

numeros = [1,2,3,4,5]
alunos = {"20151004016":"Luiz","20151004067":"Lucas", "20151006969":"Marcos"}
mensagemProva4 = ""
print(" Seja bem vindo(a) ao programa da prova 4 ")
print(" Lista é um conjunto de itens que podem ser iterados")
print(" Dicionário é um conjunto de chaves e valores que tambem podem ser iterados")
print(" Estou pronto para manipular listas e dicionarios na prova!")

sorteados = []
posição = -1

while len(sorteados) < 20:
    valor = random.randint(1, 100)
    sorteados.append(valor)
    posição = posição + 1
    print("O valor da linha", posição, "é", valor)

mensagemProva4 = "Prova sobre manipulação de listas e dicionários"
print(len(mensagemProva4))
mensagemProva4 = mensagemProva4 + ". Prova de número 4."
print(mensagemProva4)
           
