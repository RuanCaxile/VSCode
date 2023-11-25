listaContas = []
listaUsuarios = []
def sacar(*,saldo:float, valorSacado:float, extratoSaque:list, qntdeSaque:int, LimiteSaques:int): #argumentos nomeados, keyword only
    #retorna saldo e extrato
    for i in range(qntdeSaque):
        if qntdeSaque > LimiteSaques:
            print("Quantidade de Saques pedidos excedida!")
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
        if len(extratoSaque) == 0:
            print("Não há registro de saques!")
        else:
            print(f"Saque de  R$ {_}")
        print(f"O seu saldo atual é R$ {saldo}")

def criarUsuario(nome:str, dataNascimento:str, endereco:str, cpf:int):
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
    listaDepositoConta = []
    listaSacaConta = []
    saldoConta = 0
    listaConta =[]
    tuplaConta = ag, numeroConta, cpfUsuario, saldoConta, listaDepositoConta, listaSacaConta
    listaConta.append(tuplaConta)
    return listaConta
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

    print(f'As Agências e Contas disponíveis a serem visualizadas são: {listaContas}')
    if operacao_escolhida == 'd':
        contaEscolhida = int(input(f"(Escolha um número entre 1 e {len(listaContas)} Essa operação será realizada para a conta: "))
        deposita = float(input("Quanto você quer depositar ? "))
        saldoDaConta, listaDepositoConta= listaContas[contaEscolhida][3], listaContas[contaEscolhida][4]
        depositar(saldoDaConta,deposita,listaDepositoConta)
    elif operacao_escolhida == 's':
        contaEscolhida = int(input(f"(Escolha um número entre 1 e {len(listaContas)} Essa operação será realizada para a conta: "))
        saca = float(input("Quanto você quer sacar ? "))
        saldoDaConta, listaSacaConta= listaContas[contaEscolhida][3], listaContas[contaEscolhida][5]
        sacar(saldo=saldoDaConta, valorSacado=saca, extratoSaque=listaSacaConta,qntdeSaque=1, LimiteSaques=3)
    elif operacao_escolhida == 'e':
        contaEscolhida = int(input(f"(Escolha um número entre 1 e {len(listaContas)} Essa operação será realizada para a conta: "))
        saldoDaConta, listaDepositoConta, listaSacaConta= listaContas[contaEscolhida][3],listaContas[contaEscolhida][4], listaContas[contaEscolhida][5]
        visualizarExtrato(saldoDaConta, extratoDeposito=listaDepositoConta, extratoSaque=listaSacaConta)
    elif operacao_escolhida == 'u':
        nome = input("Qual o seu nome ? ")
        dataNasc = input("Qual a sua data de nascimento ? ")
        end = input("Qual o seu endereço ? ")
        cpf = int(input("Qual o seu CPF ? "))
        if len(listaUsuarios) == 0:
            listaUsuarios = listaUsuarios + criarUsuario(nome, dataNasc, end, cpf)
        else:
            for j in listaUsuarios:
                if j['cpf'] != cpf:
                    listaUsuarios = listaUsuarios + criarUsuario(nome, dataNasc, end, cpf)
                else:
                    print('CPF já cadastrado!')
                    continue
    elif operacao_escolhida == 'cc':
        if len(listaUsuarios) != 0:
            cpfUsuario = int(input("Escolha um CPF válido para criar sua conta: "))
            for _ in listaUsuarios:
                if _['cpf'] == cpfUsuario:
                    agencia = int(input("Escolha a agência: "))
                    contaDoBanco = int(input("Escolha a conta:"))
                    if len(listaContas) !=0:
                        for k in listaContas:
                            if k[1] != contaDoBanco:
                                listaContas = listaContas + contaCorrente(agencia, contaDoBanco, cpfUsuario)
                            else:
                                continue
                    else:
                        listaContas = listaContas + contaCorrente(agencia, contaDoBanco, cpfUsuario)
                else:
                    continue
        else:
           print("Não há usuários cadastrados!")
           continue 
    elif operacao_escolhida == 'q':
        break
    else:
        continue
