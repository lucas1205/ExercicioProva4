#A recusividade é você chama a função dentro dela mesmo, criando um loop.

def recAte5(n):
    print(n)
    if n == 5:
        return n
    else:
        return recAte5(n+1)

recAte5(0)
