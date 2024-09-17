def reversedOrder():
    lista = [float(num.strip()) for num in input('(Separados por virgula)\nInsira os valores que deseja: ').split(',')]
    return list(lista[::-1])


def sumNumbers():
    while True:
        try:
            lista_num = [float(num) for num in input('Insira os numeros que deseja somar ').split(',')]
            return sum(lista_num)
        except ValueError:
            print('Por favor somente insira numeros.')


def firstTwoSum():
    while True:
        try:
            print('Insira duas listas (separadas por virgula) e obtenha a soma entre as duas')
            lista1 = [float(num.strip()) for num in input('A primeira: ').split(',')]
            lista2 = [float(num.strip()) for num in input('A segunda lista: ').split(',')]
            return sum(lista1[:2] + lista2[:2])
        except ValueError:
            print('Apenas números...')


def MaxMinNum() -> float:
    while True:
        try:
            lista_num = [float(num.strip()) for num in input('Insira os numeros que quer o valor maximo e o minimo: ').split(',')]
            return max(lista_num), min(lista_num)
        except ValueError:
            print('Por favor somente insira numeros.')


def AmountoffEvenOdd() -> float:
    while True:
        try:
            numeros = [float(num.strip()) for num in input('Insira os números separados por virgula: ').split(',')]
            counterEven = 0
            counterOdd = 0
            for num in numeros:
                if num % 2 == 0:
                    counterEven += 1 
                else:
                    counterOdd += 1
            return f'Even amount: {counterEven}, Odd amount: {counterOdd}'
        except ValueError:
            print('Insira um valor válido.')


def negativeToZero() -> float:
    while True:
        try:
            numeros = [float(num.strip()) for num in input('Insira os números separados por virgula: ').split(',')]
            for num in numeros:
                if num < 0:
                    num = 0
                print(num)
            break
        except ValueError:
            print('naum pode')


def commonElements( ):
    itens1 = [str(valor.strip()) for valor in input('Insira primeira lista separado por virgula: ').split(',')]
    itens2 = [str(valor.strip()) for valor in input('Insira segunda lista separado por virgula: ').split(',')]
    itens_repetidos = []
    for item1 in itens1:
        itens_repetidos.append(item1) if item1 in itens2 and item1 not in itens_repetidos else ''
    return itens_repetidos


def removeRepeatedElements():
    while True:
        lista = [str(item.strip()) for item in input('Insira a lista separado por virgula: ').split(',')]
        if len(lista) <= 10:
            break
        print('Aceitamos apenas listas com até 10 elementos.')
    
    lista_unica = list(set(lista))
    return lista_unica


def crescentOrder():
    while True:
        try:
            elementos = [int(valor.strip()) for valor in input('Insira a lista separado por virgula: ').split(',')]
            elementos.sort()
            return elementos
        except ValueError:
            print('insira um valor correto numeral.')

def averageElement():
    notas = []
    for index in range(10):
        while True:
            try:
                numeros = int(input(f'Insira o valor da posição {index + 1}: '))
                notas.append(numeros)
                break
            except ValueError:
                print('Valor inválido. Por favor, insira um número.')
    media = sum(notas) / len(notas)
    print(f'Média: {media:.2f}')
    print('Elementos acima da média:')
    for valor in notas:
        if valor > media:
            print(valor)
        
