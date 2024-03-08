print('Sistema de Operações\n----------------------')
print('Calculadora Simples: (1)\nEquação de 2º Grau: (2)\nGeometria Analítica: (3)\n----------------------')
#print('')
code = int(input('Código: '))
print('______________________')

if code == 1:
    print('CALCULADORA SIMPLES - 2 NÚMEROS\n______________________')
    print('Adição: \033[36m(A)\033[m\nSubtração: \033[36m(S)\033[m\nMultiplicação: \033[36m(M)\033[m')
    print('Divisão: \033[36m(D)\033[m\nRaiz Quadrada: \033[36m(R)\033[m\nPotenciaçao: \033[36m(P)\033[m\nLogaritmo: \033[36m(L)\033[m\n----------------------')
    op = str(input('Digite a Inicial da Operação: '))
    opçoes = ['A','S','M','D',]

    if op.upper() == 'R':
        print('______________________')
        from math import sqrt
        num = float(input('Número: '))
        raiz = sqrt(num)
        print(f'-------------------\nRaiz: {raiz}')
    elif op.upper() == 'P':
        print('______________________')
        num = float(input('Número: '))
        exp = float(input('Expoente: '))
        result = num ** exp
        print(f'-------------------\nPotenciação: {num}^{exp} = {result}')
    elif op.upper() == 'L':
        print('______________________')
        from math import log
        num = float(input('Número: '))
        base = float(input('Base: ')) 
        result = log(num,base)
        print(f'-------------------\nLog: {result}')
    elif op.upper() in opçoes:
        print('______________________')
        num1 = float(input('Número 1: '))
        num2 = float(input('Número 2: '))

        if op.upper() == 'A':
            result = num1 + num2
            print(f'-------------------\nAdição: {num1} + {num2} = {result}')
        elif op.upper() == 'S':
            result = num1 - num2
            print(f'-------------------\nSubtração: {num1} - {num2} = {result}')
        elif op.upper() == 'M':
            result = num1 * num2
            print(f'-------------------\nMultiplicação: {num1} x {num2} = {result}')
        elif op.upper() == 'D':
            if num2 == 0:
                print('-------------------\nIndefinido')
            else:
                result = num1 / num2
                print(f'-------------------\nDivisão: {num1} ÷ {num2} = {result}')

elif code == 2:
    print('EQUAÇÃO DE 2º GRAU\n______________________')
    a = int(input('Coeficiente A: '))
    b = int(input('Coeficiente B: '))
    c = int(input('Coeficiente C: '))

    delta = b**2 - (4 * a * c)
    x1 = (-b + (delta**0.5)) / (2 * a)
    x2 = (-b - (delta**0.5)) / (2 * a)

    if delta < 0:
        print('-------------------\nO Resultado NÃO é um Número Real')
    else:
        print(f'-------------------\nX1 = {x1}\nX2 = {x2}')

elif code == 3:
    print('GEOMETRIA ANALITICA\n______________________')
    print('Distância entre 2 Pontos: \033[33m(1)\033[m\nEquação da Reta: \033[33m(2)\033[m')
    choise = int(input('----------------------\nInforme a Operação: '))
    if choise == 1:
        print('______________________\nInforme os Valores de x1 e y1\n------------------------')
        x1 = float(input('x1: '))
        y1 = float(input('y1: '))
        print('______________________\nInforme os Valores de x2 e y2\n------------------------')
        x2 = float(input('x2: '))
        y2 = float(input('y2: '))

        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
        result = dist**0.5
        print(f'-----------------------\nDistância = √{dist} = {result}')
    #elif choise == 2:
