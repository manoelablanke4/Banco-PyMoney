import datetime
import re
import test


menu = """"
Seja bem-vindo ao banco PyMoney!
Qual operação deseja realizar?

[d] - Depositar
[s] - Sacar
[e] - Extrato
[u] - Criar usuário
[c] - Criar conta
[q] - Sair

--------------------------------
"""

conta = test.Conta(0,1,'0001','José',[])
print(conta.saldo)
vezes_saque = 0
saldo = 0
extrato = []
limite_saque = 500
vezes_transaçoes = 0
usuarios = []
contas = []

def saque(*,valor,limite_saque,vezes_saque,saldo,extrato):
    if saldo >= valor and valor <= limite_saque and vezes_saque <= 3:
        saldo -= valor
        date = datetime.datetime.now()
        extrato.append(f'Saque: - R$ {valor} - {date.strftime("%d/%m/%Y %H:%M:%S")}')
        print()
        print('--------------------------------')
        print('==== Sua operação de saque foi realizada com sucesso ====')
        print('--------------------------------')
        print()
        return saldo, extrato
    elif vezes_saque > 3:
        print()
        print('--------------------------------')
        print('==== Limite de saques diários atingido ====')
        print('--------------------------------')
        print()
        return saldo, extrato
    else:
        print()
        print('--------------------------------')
        print('==== Saldo insuficiente =====')
        print('--------------------------------')
        print()
        return saldo, extrato

def deposito(clientes):
    cpf = input('Digite seu CPF: ')
    cliente = filtrar_usuarios(clientes,cpf)

    if not cliente:
        print()
        print('--------------------------------')
        print('CPF não cadastrado. Tente novamente.')
        print('--------------------------------')
        print()
        return
    
    valor = float(input('Qual valor deseja depositar? '))
   

    

def extrato_funcao(saldo,/,*,extrato):
    extrato.append(f'Saldo: R$ {saldo}')
    print('--------------------------------')
    print('Extrato:')
    for item in extrato:
        print(item)
    print('--------------------------------')


def filtrar_usuarios(usuarios,cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True
    return False

def criar_usuario(usuarios):
    nome = input('Digite seu nome: ')
    data_de_nascimento = input('Digite sua data de nascimento: ')
    endereco = input('Digite seu endereço no formato:(logradouro, num - bairro - cidade/sigla do estado) ')
    end_pattern = re.compile(r'^[a-zA-Z\s]+, \d+[a-zA-Z]? - [a-zA-Z\s]+ - [a-zA-Z\s]+/[A-Z]{2}$')
    if re.match(end_pattern, endereco) == None:
        print()
        print('--------------------------------')
        print('Endereço inválido. Tente novamente.')
        print('--------------------------------')
        print()
        return
    cpf = input('Digite seu CPF: ')
    filter = filtrar_usuarios(usuarios,cpf)
    if filter:
        print()
        print('--------------------------------')
        print('CPF já cadastrado. Tente novamente.')
        print('--------------------------------')
        print()
        return
    usuarios.append({'nome':nome,'data_de_nascimento':data_de_nascimento,'endereco':endereco,'cpf':cpf})
    print()
    print('--------------------------------')
    print(f'Usuário {nome} criado com sucesso!')
    print('--------------------------------')
    print()
    return 
def criar_conta(contas,usuarios):
    conferir_cpf = input('Digite seu CPF para criar uma conta: ')
    agencia = '0001'
    numero_conta = len(contas) + 1
    filter = filtrar_usuarios(usuarios,conferir_cpf)
    if not filter:
        print()
        print('--------------------------------')
        print('CPF não cadastrado. Tente novamente.')
        print('--------------------------------')
        print()
    contas.append({'agencia':agencia,'numero_conta':numero_conta,'cpf':conferir_cpf})
    print()
    print('--------------------------------')
    print(f'Conta com número {numero_conta} criado com sucesso!')
    print('--------------------------------')
    print()
def conta_do_cliente(cpf):
    for conta in contas:
        if conta['cpf'] == cpf:
            return conta
    return False
    
while True:
    opcao = menu()

    clientes = []
    contas = []
    if opcao == 'd':
        deposito(clientes,valor)

    elif opcao == 's':
        vezes_saque += 1
        valor = float(input('Qual valor deseja sacar? '))
        saldo, extrato = saque(valor=valor,limite_saque=limite_saque,vezes_saque=vezes_saque,saldo=saldo,extrato=extrato)

    elif opcao == 'e':
        extrato_funcao(saldo,extrato=extrato)
    elif opcao == 'u':
        criar_usuario(usuarios) 
    elif opcao == 'c':
        criar_conta(contas,usuarios)  
    elif opcao == 'q':
        break
    else:
        print('Opção inválida. Tente novamente.')
        print('--------------------------------')