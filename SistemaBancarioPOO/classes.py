from datetime import date


class Cliente:
   def __init__(self, endereco:str, contas:list) -> None:
      self.endereco = endereco
      self.contas = contas
   
   def realizar_transacao(conta: Conta, transacao: Transacao):
       pass
   
   def adicionar_conta(conta:Conta):
       pass



class PessoaFisica(Cliente):
    def __init__(self, endereco: str, contas: list, cpf: str, nome:str, data_nascimento:date) -> None:
        super().__init__(endereco, contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    


class Conta:
    def __init__(self, saldo:float, numero:int, agencia:str, cliente:Cliente, historico:Historico) -> None:
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.historico = historico
    

    def saldo(self) -> float:
        pass

    def nova_conta(self,cliente:Cliente, numero:int):
        pass
        
    def sacar(self, valor:float) -> bool:
        pass

    def depositar(self, valor:float) -> bool:
        pass

class ContaCorrente(Conta):
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico: Historico, limite:float, limite_saques:int) -> None:
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques

