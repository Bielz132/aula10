#Funcoes

def mostrar_texto_tela():
    print('teste')
mostrar_texto_tela()

def soma():
    n1 = int(input('Digite um Numero: '))
    n2 = int(input('Digite um Numero: '))
    soma = n1 + n2
    print(soma)
soma()
# precisa deixar encostado na borda

def subtracao():
    n1 = int(input('Digite um Numero: '))
    n2 = int(input('Digite um Numero: '))
    subtracao = n1 - n2
    print(subtracao)

subtracao() 
# precisa deixar encostado na borda

def multiplicacao():
    n1 = int(input('Digite um Numero: '))
    n2 = int(input('Digite um Numero: '))
    multi = n1 * n2
    print(multi)

multiplicacao() 
# precisa deixar encostado na borda

def divisao():
    n1 = int(input('Digite um Numero: '))
    n2 = int(input('Digite um Numero: '))
    divi = n1 / n2
    print(divi)

divisao() 
# precisa deixar encostado na borda

def calculadora():
    ope = input(f'''Escolha uma operação: "+ - * /" 
    --> ''')

    if ope == '+':
        soma()

    elif ope == '-':
        subtracao()

    elif ope == '*':
        multiplicacao()

    elif ope == '/':
        divisao()

    else:
        print('Digitação não existe')
calculadora()