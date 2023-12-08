from datetime import datetime
from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty
import textwrap
class Cliente:
   def __init__(self, endereco:str) -> None:
      self.endereco = endereco
      self.contas = []
   
   def realizar_transacao(self,conta, transacao):
        transacao.registrar(conta)
   
   def adicionar_conta(self,conta):
       self.contas.append(conta)



class PessoaFisica(Cliente):
    def __init__(self, nome:str, data_nascimento, cpf:str, endereco:str) -> None:
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    


class Conta:
    def __init__(self,numero:int, cliente:Cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._historico = Historico()
        self._cliente = cliente
    
    @property
    def saldo(self) -> float:
        return self._saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property    
    def sacar(self, valor:float) -> bool:
        pode_sacar = self._saldo >= self.cliente.limite and valor > 0

        if pode_sacar:
            self._saldo -= valor
            print("Operação realizada com sucesso!!!")
            return True
        else:
            print("Operação não realizada! Por gentileza, verifique seu limite e o valor informado.")
        return False
  
    @property
    def depositar(self, valor) -> bool:
        pode_depositar = valor > 0
        if pode_depositar:
            self._saldo += valor
            print("Operação realizada com sucesso!!!")
            return True
        else:
            print("Operação não realizada! O valor informado é inválido.")
        
        return False
    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self.cliente

    @property
    def historico(self):
        return self._historico.transacoes()        

class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite= 500, limite_saques=3) -> None:
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

class Historico:
    def __init__(self) -> None:
        self._transacao = []

    def transacoes(self):
        return self._transacao


    def adicionar_transacao(self, transacao):
        self._transacao.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self):
        pass

class Deposito(Transacao):
    def __init__(self, valor) -> None:
        super().__init__()
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_deposito = conta.depositar(self.valor)

        if sucesso_deposito:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor:float) -> None:
        super().__init__()
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_saque = conta.sacar(self._valor)

        if sucesso_saque:
            conta.historico.adicionar_transacao(self)

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta!")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Já existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("Cliente criado com sucesso!")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado, fluxo de criação de conta encerrado!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("Conta criada com sucesso!")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()