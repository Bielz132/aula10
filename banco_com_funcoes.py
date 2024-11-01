# ATIVIDADE:

# CRIE UM SISTEMA DE UM BANCO.
# OPERAÇÕES DO BANCO:

# SAQUE() 
# DEPOSITO() 
# VISUALIZAR_STATUS() 
# BOCA_DO_CAIXA()
din = 500.00               
extrato = 1
deposito = 2
saque = 3 
sair = 4 

nome = 'gabriel'
senha = 123
gmail = 'gabriel@gmail.com'

print('Ola, seja bem vindo ao banco "Boca Da Fortuna"')

for n in range(1,3):
        nome_user = input('Digite seu nome: ')
        senha_user = int(input('Digite sua senha: '))
        gmail_user = input('Digite seu gmail: ')
        if nome_user == nome and senha_user == senha and gmail_user == gmail:
                print(f'Seja bem vindo {nome}')
                print(f''' Você gostaria de fazer oque?
                Ver extrato = 1
                Fazer deposito = 2
                fazer saque = 3
                sair do sistema = 4''')
                break

                

def banco_extrato():
                escolha = int(input('-> '))

                if escolha == extrato:

                    print('Ok')
                    print("Você tem R$ 500.00")
                    desejo = int(input('Deseja fazer um DEPOSITO = 1 ou SAQUE = 2?: '))
                    if desejo == 1:

                        print('Deseja depositar quanto?')  
                        ale = float(input('-> '))
                        total = din + ale
                        print(total)
                          
                    else:
                        print('Deseja sacar quanto?')
                        ale2 = float(input('-> '))
                        total2 = din - ale2
                        print(total2)
                        
banco_extrato()
def banco_deposito():
    escolha = int(input('-> '))
    if escolha == deposito:
        print('Ok, deseja depositar quanto?')
        ale3 = float(input('-> '))
        otal3 = din + ale3
        print(total3)
banco_deposito()

def banco_saque():
    escolha = int(input('-> '))
    if escolha == saque:
        print('Ok, deseja sacar quanto?')
        ale4 = float(input('-> '))
        total4 = din - ale4
        print(total4)
banco_saque()

def banco_final():
    escolha = int(input('-> '))
    if escolha == sair:
        print('Ok, desligando sistema')
banco_final()        
                  
if nome_user != nome and senha_user != senha and gmail_user != gmail:
    print('Tente novamente')
n = input('clique enter para sair')