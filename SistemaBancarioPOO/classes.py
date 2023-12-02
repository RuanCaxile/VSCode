from datetime import date
from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty

class Cliente:
   def __init__(self, endereco:str) -> None:
      self.endereco = endereco
      self.contas = []
   
   def realizar_transacao(self,conta, transacao):
       pass
   
   def adicionar_conta(self,conta):
       pass



class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome:str, data_nascimento:date) -> None:
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
        self.cliente = cliente
    
    @property
    def saldo(self) -> float:
        pass

    @classmethod
    def nova_conta(self,cliente:Cliente, numero:int):
        pass

    @property    
    def sacar(self, valor:float) -> bool:
        pass
    
    @property
    def depositar(self, valor:float) -> bool:
        pass

    @property
    def agencia(self):
        pass

    @property
    def cliente(self):
        pass

    @property
    def historico(self):
        pass

class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite= 500, limite_saques=3) -> None:
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

class Historico:
    def __init__(self) -> None:
        self._transacao = []

    def transacoes(self):
        pass


    def adicionar_transacao(self, transacao):
        pass


class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self):
        pass

class Deposito(Transacao):
    def __init__(self, valor:float) -> None:
        super().__init__()
        self._valor = valor

    @property
    def valor(self):
        pass

    def registrar(self):
        pass

class Saque(Transacao):
    def __init__(self, valor:float) -> None:
        super().__init__()
        self._valor = valor

    @property
    def valor(self):
        pass

    def registrar(self):
        pass

