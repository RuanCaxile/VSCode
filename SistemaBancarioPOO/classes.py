from datetime import date
from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty

class Cliente:
   def __init__(self, endereco:str) -> None:
      self.endereco = endereco
      self.contas = []
   
   def realizar_transacao(self,conta, transacao):
       if isinstance(transacao,Transacao):
        transacao.registrar(conta)
   
   def adicionar_conta(self,conta):
       self.contas.append(conta)



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
        return self._saldo

    @classmethod
    def nova_conta(cls, numero, cliente):
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
    def depositar(self, valor:float) -> bool:
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
        self._transacao.append(transacao)


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
        return self._valor

    def registrar(self, conta):
        pass 

class Saque(Transacao):
    def __init__(self, valor:float) -> None:
        super().__init__()
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        pass

