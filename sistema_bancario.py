saldo_conta = 0
quantidade_saques = 0
quantidade_depositos = 0
saques = ''
depositos = ''

menu = """
    ========== Menu ==========

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    ========================== 
"""


while True:
    
    extrato = f'''
    ========== Extrato ==========

    Quantidade de saques realizados {quantidade_saques}
    Valores sacados{saques}

    Quantidade de depositos realizados {quantidade_depositos}
    Valores depositados{depositos}

    Saldo atual R${saldo_conta:.2f}

    =============================
        
        '''

    print(menu)
    opcao = input('Digite a opção desejada: ')

    if opcao == 'd':
        valor_deposito = float(input("Digite o valor para deposito: "))
        if valor_deposito > 0:
            print('''
                     Processando deposito....
                     Deposito realizado com sucesso!
                     ''')
            saldo_conta += valor_deposito
            depositos += f'\n        R$ {valor_deposito:.2f}'
            quantidade_depositos += 1
        else:
            print('Valor inválido! Tente novamente!')
    elif opcao == 's':
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        if valor_saque > 0 and valor_saque <= saldo_conta and valor_saque <= 500 and quantidade_saques < 3:
            print('''
                     Processando saque....
                     Retire o dinheiro no local indicado!
                     ''')
            quantidade_saques += 1
            saldo_conta -= valor_saque
            saques += f'\n        R$ {valor_saque:.2f}'
        elif quantidade_saques > 3:
            print('Quantidade de saques exedidas!')
        elif valor_saque > 500:
            print('Valor exede o valor máximo para saque!')
        elif valor_saque > saldo_conta:
            print('Saldo insuficiente!')
        else:
            print('Valor inválido! Tente novamente!')
    elif opcao == 'e':
        print(extrato)
    elif opcao == 'q':
        print("Obrigado por usar nosso sistema! Volte sempre!")
        break
    else:
        print("Operação inválisa, por favor selecione novamente a operação desejada.")