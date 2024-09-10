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

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente os números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: 
        print('\n@@@ Já existe usuário com esse CPF! @@@')
        return 
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço: ')
    usuarios.append({'nome':nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuário criado')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: 
        print('\n ====== Conta criada com sucesso! ======')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('\n @@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@')

def listar_contas(contas):
    for conta in contas:
        print(conta)

def main():
    AGENCIA = '0001'
    usuarios = []
    contas = []

    while True:
        print('\nMenu:')
        print('1 - Depósito')
        print('2 - Saque')
        print('3 - Extrato')
        print('4 - Criar usuário')
        print('5 - Criar conta corrente')
        print('6 - Listar contas')
        print('7 - Sair')
        menu = input('Escolha a operação: ')

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
                criar_usuario(usuarios)

            case '5':
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)

            case '6':
                listar_contas(contas)

            case '7':
                print('Saindo...')
                break

            case _:
                print('Opção inválida')


main()
