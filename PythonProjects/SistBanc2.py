saldoAtual = 0
listaDeposito = []
listaSaque = []
deposito = 0 
saca = 0 
numeroSaques = 0

extrato = ""

def sacar(*,saldo:float, valorSacado:float, extratoSaque:list, qntdeSaque:int, LimiteSaques:int): #argumentos nomeados, keyword only
    #retorna saldo e extrato
    for i in range(qntdeSaque):
        if qntdeSaque > LimiteSaques:
            return saldo, extratoSaque
        else:
            saldo -= valorSacado
            extratoSaque.append(valorSacado)
            return saldo, extratoSaque
    


def depositar(saldo:float,valorDepositado:float,extratoDeposito:list): #argumentos posicionais, positional only
    #retorna saldo e extrato
    saldo += valorDepositado
    extratoDeposito.append(valorDepositado)
    return saldo, extratoDeposito

def visualizarExtrato(saldo:float,*,extratoSaque:list, extratoDeposito:list): #argumentos posicionais e nomeados
    #retorna extrato
    for _ in extratoDeposito:
        if len(extratoDeposito) == 0:
            print("Não há registro de depósitos")
        else:
            print(f"Depósito de R$ {_}")
        
    for _ in extratoSaque:
        if len(listaSaque) == 0:
            print("Não há registro de saques!")
        else:
            print(f"Saque de  R$ {_}")
        print(f"O seu saldo atual é R$ {saldo}")

def criarUsuario(nome:str, dataNascimento:str, cpf:int, endereco:str):
    #retorna lista de dicionarios
    listaUsuario = []
    dicUsuario = {
        "nome":nome,
        "DataDeNascimento":dataNascimento,
        "cpf":cpf,
        "endereço":endereco
    }

    listaUsuario.append(dicUsuario)
    return listaUsuario

def contaCorrente(ag:int, numeroConta:int, cpfUsuario:int):
    #retorna uma lista de tuplas (formada por ag, conta, cpfUsuario)
    return ag, numeroConta, cpfUsuario

while True:
    operacao_escolhida = input(
    """
    Escolha a operação bancária!
    [d] Depósito
    [s] Sacar
    [e] Visualizar Extrato
    [u] Criar Usuário
    [cc] Criar conta 
    [q] Sair
    
    """)
    if operacao_escolhida == 'd':
        deposito = float(input("Quanto você quer depositar ?"))
        listaDeposito.append(deposito)
        saldoAtual += deposito
    elif operacao_escolhida == 's':
        pass
    elif operacao_escolhida == 'e':
        pass
    elif operacao_escolhida == 'u':
        pass
    elif operacao_escolhida == 'cc':
        pass
    elif operacao_escolhida == 'q':
        break
    else:
        continue