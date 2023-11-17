saldoAtual = 0
listaDeposito = []
listaSaque = []
deposito = 0 
saca = 0 
LimiteSaques = 0
extrato = ""

while True:
    operacao_escolhida = input(
    """
    Escolha a operação bancária!
    [d] Depósito
    [s] Sacar
    [e] Extrato
    [q] Sair
    \n
    """)
    if operacao_escolhida == 'd':
        deposito = float(input("Quanto você quer depositar ?"))
        listaDeposito.append(deposito)
        saldoAtual += deposito
    elif operacao_escolhida == 's':
        saca = float(input("Quanto você quer sacar ?"))
        if saldoAtual < saca:
            print("Saldo Insuficiente! Por favor, deposite dinheiro.")
        elif LimiteSaques == 3:
            print("Limite de saque atingido.")
        else:
            saldoAtual -= saca
            listaSaque.append(saca)
            LimiteSaques += 1
    elif operacao_escolhida == 'e':
        for _ in listaDeposito:
            if len(listaDeposito) == 0:
                print("Não há registro de depósitos")
            else:
                print(f"Depósito de R$ {_}")
        
        for _ in listaSaque:
            if len(listaSaque) == 0:
                print("Não há registro de saques!")
            else:
                print(f"Saque de  R$ {_}")
        print(f"O seu saldo atual é R$ {saldoAtual}")
        
    elif operacao_escolhida == 'q':
        break
    else:
        continue