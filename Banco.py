depositos = []
saques = []
saldo_atual = 0

def deposito(valor):
    global saldo_atual
    depositos.append(valor)
    saldo_atual += valor
    return saldo_atual

def saque(valor):
    global saldo_atual
    if valor > saldo_atual:
        print('Saldo insuficiente')
        return saldo_atual
    else:
        saques.append(valor)
        saldo_atual -= valor
        return saldo_atual

def saldo():
    return saldo_atual

print('Menu:')
print('1 - Deposito')
print('2 - Saque')
print('3 - Extrato')
print('4 - Sair')
menu = input('Escolha a operação:')

while menu != '4':
    match menu:
        case '1':
            count = input('Digite o número de depósitos que deseja fazer: ')
            for i in range(int(count)):
                valor = float(input('Digite o valor do depósito: '))
                deposito(valor)
            print('Depósitos:', depositos)
            print('Saldo atual:', saldo())
        case '2':
            count = input('Digite o número de saques que deseja fazer: ')
            if int(count) > 3:
                print('O número máximo de saques é 3')
            else:
                for i in range(int(count)):
                    valor = float(input('Digite o valor do saque: '))
                    if valor > 500:
                        print('O valor máximo de saque é R$500,00')
                    else:
                        saque(valor)
                print('Saques:', saques)
                print('Saldo atual:', saldo())
        case '3':
            print('Depósitos: R$', depositos)
            print('Saques: R$', saques)
            print('Saldo atual: R$', saldo())
        case '4':
            print('Saindo...')
            break
        case _:
            print('Opção inválida')

    menu = input('Escolha a operação:')
