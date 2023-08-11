'''Funções'''
def gerarExtrato(saldo_conta, / , lista_saques=lista_saques, lista_depositos=lista_depositos):
    saques = ''
    depositos = ''
    
    for valor_saque in lista_saques:
        saques += f'\n        R$ {valor_saque:.2f}'
    for valor_deposito in lista_depositos:
        depositos += f'\n        R$ {valor_deposito:.2f}' 
    
    quantidade_saques = len(lista_saques)
    quantidade_depositos = len(lista_depositos)
       
    extrato = '''
        ========== Extrato ==========
        '''
    extrato += f''' 
        Quantidade de saques realizados {quantidade_saques}
        Valores sacados{saques}
        ''' if quantidade_saques >= 1 else ''
    extrato += f'''
        Quantidade de depositos realizados {quantidade_depositos}
        Valores depositados{depositos}
        ''' if quantidade_depositos >= 1 else ''
    extrato += f'''
        Saldo atual R${saldo_conta:.2f}

        =============================
        '''
    print(extrato)
    return saldo_conta

def saque(*, saldo_conta, valor, lista_saques, lista_depositos):
    global LIMITE_SAQUES
    
    if len(lista_saques) < LIMITE_SAQUES:
        
        if valor_saque > saldo_conta:
            print('Saldo insuficiente!')
        elif valor > 0 and valor <= saldo_conta and valor <= 500:
            print('''
                     Processando saque....
                     Retire o dinheiro no local indicado!
                     ''')
            lista_saques.append(valor)
            saldo_conta -= valor
        elif valor_saque > 500:
            print('Valor exede o valor máximo para saque!')
        else:
            print('Valor inválido! Tente novamente!')
    else:
        print('Quantidade de saques exedidas!')
    return gerarExtrato(saldo_conta, lista_saques=lista_saques, lista_depositos=lista_depositos)

                
def deposito(saldo_conta, valor, lista_depositos, lista_saques):
    if valor_deposito > 0:
        print('''
                Processando deposito....
                Deposito realizado com sucesso!
                ''')
        saldo_conta += valor_deposito
        lista_depositos.append(valor_deposito)
    else:
        print('Valor inválido! Tente novamente!')
    return gerarExtrato(saldo_conta, lista_depositos=lista_depositos, lista_saques=lista_saques)
                
def cadastroUsuario(usuarios):
    cpf = input('Digite seu CPF: ')
                
    if not usuarios.get(cpf):
        nome = input('Digite seu nome: ')
        data_de_nascimento = input('Digite sua data de nascimento: ')
        logradouro = input('Logradouro: ')
        numero = input('Numero: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        estado = input('Estado(sigla): ')
        endereco = f'{logradouro}, {numero} - {bairro} - {cidade}/{estado}'
        
        usuarios[cpf] = {'nome':nome, 'Data de nascimento':data_de_nascimento, 'CPF':cpf, 'Endereço':endereco}
                
        print('''
            Registrando conta...
            Conta Registrada com sucesso!''')
    else:
        print('Este cpf já esta cadastrado em nosso sistema, tente fazer login.')

def cadastroConta(usuario, usuarios):
    global numero_contas
                
    numero_contas += 1
    AGENCIA = '0001'
    conta = str(numero_contas)
    senha = input('Digite uma senha: ')
    usuarios[usuario].update({conta: [AGENCIA, senha]})
    
    print(f'''
        Sua conta foi criada com sucesso!
        Dados da conta
        Agencia: {AGENCIA}
        Numero da conta: {conta}
        ''')
                
def checkLogin(tipo, usuarios):
    global logado_usuario, logado_conta
    
    login = input('Digite seu CPF: ')
    
    if tipo == 'usuario':
        if login in usuarios.keys():
            logado_usuario = True 
            return login
        else:
            return print('Usuário não encontrada, tente novamente!')
    elif tipo == 'conta':
        numero_da_conta = input('Digite o numero da conta: ')
        senha = input('Digite o senha: ')
        
        contas_usuarios = usuarios[login]
        if contas_usuarios.get(numero_da_conta):
            if senha in contas_usuarios[numero_da_conta]:
                logado_conta = True
                return login
            else:
                print('Senha incorreta!')
        else:
            return print('Conta não encontrada, tente novamente!')
          
        
        
'''Constantes'''
LIMITE_SAQUES = 3
                
'''Variáveis'''
saldo_conta = 0
lista_saques, lista_depositos, usuarios= [], [], {}
logado_usuario, logado_conta = False, False
numero_contas = 0

menu_sistema ="""
    ========== Menu ==========

    [l] Fazer login
    [c] Criar usuário
    [q] Sair

    ========================== 
"""                          
                
menu_usuario ="""
    ========== Menu ==========

    [a] Acessar uma conta
    [c] Criar conta
    [u] Trocar de usuário
    [q] Sair

    ========================== 
"""
                
menu_conta = """
    ========== Menu ==========

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Trocar de usuário
    [t] Trocar de conta
    [q] Sair

    ========================== 
"""


while True:
    print(menu_sistema)
    opcao = input('Digite a opção desejada: ')
                
    if opcao == 'l':
        usuario = checkLogin('usuario', usuarios)
                
        while logado_usuario:
            print(f'Bem-vindo Sr. {usuarios[usuario]["nome"]}!')
            print(menu_usuario)
            opcao = input('Digite a opção desejada: ')
                
            if opcao == 'a':
                checkLogin('conta', usuarios)
                
                while logado_conta:
                    print(menu_conta)
                    opcao = input('Digite a opção desejada: ')

                    if opcao == 'd':
                        valor_deposito = float(input("Digite o valor para deposito: "))
                        saldo_conta = deposito(saldo_conta, valor_deposito, lista_depositos, lista_saques)
                    elif opcao == 's':
                        valor_saque = float(input("Digite o valor que deseja sacar: "))
                        saldo_conta = saque(saldo_conta=saldo_conta , valor=valor_saque, lista_saques=lista_saques, lista_depositos=lista_depositos)
                    elif opcao == 'e':
                        gerarExtrato(saldo_conta, lista_saques=lista_saques, lista_depositos=lista_depositos)
                    elif opcao == 'u':
                        logado_usuario = False
                    elif opcao == 't':
                        logado_conta = False
                    elif opcao == 'q':
                        print("Obrigado por usar nosso sistema! Volte sempre!")
                        break
                    else:
                        print("Operação inválisa, por favor selecione novamente a operação desejada.")

            elif opcao == 'c':
                cadastroConta(usuario, usuarios)
            elif opcao == 'u':
                logado_usuario = False
            elif opcao == 'q':
                print("Obrigado por usar nosso sistema! Volte sempre!")
                break
            else:
                print("Operação inválisa, por favor selecione novamente a operação desejada.")
                
    elif opcao == 'c':
        cadastroUsuario(usuarios)
    elif opcao == 'q':
        print("Obrigado por usar nosso sistema! Volte sempre!")
        break
    else:
        print("Operação inválisa, por favor selecione novamente a operação desejada.")