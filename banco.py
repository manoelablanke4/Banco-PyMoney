menu = """"
Seja bem-vindo ao banco PyMoney!
Qual operação deseja realizar?

[d] - Depositar
[s] - Sacar
[e] - Extrato
[s] - Sair

--------------------------------
"""

vezes_saque = 0
saldo = 0
extrato = []
limite_saque = 500

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input('Qual valor deseja depositar? '))
        saldo += valor
        extrato.append(f'Depósito: + R$ {valor}')
    elif opcao == 's':
        valor = float(input('Qual valor deseja sacar? '))
        if saldo >= valor and valor <= limite_saque and vezes_saque <= 3:
            saldo -= valor
            vezes_saque += 1
            extrato.append(f'Saque: - R$ {valor}')
        else:
            print('Saldo insuficiente ou limite de saque ultrapassado.')
            print('--------------------------------')
            vezes_saque += 1
    elif opcao == 'e':
        extrato.append(f'Saldo: R$ {saldo}')
        print('--------------------------------')
        print('Extrato:')
        for item in extrato:
            print(item)
        print('--------------------------------')    
    elif opcao == 's':
        break
    else:
        print('Opção inválida. Tente novamente.')
        print('--------------------------------')