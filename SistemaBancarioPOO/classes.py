class Cliente:
   def __init__(self, endereco:str, contas:list) -> None:
      pass  




class Conta:
    def __init__(self, saldo:float, numero:int, agencia:str, cliente:Cliente, historico:Historico) -> None:
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.historico = historico
    

    def saldo(self) -> float:
        pass

    def nova_conta(self,cliente:Cliente, numero:int, ):
        pass
        
    def sacar(self, valor:float) -> bool:
        pass

    def depositar(self, valor:float) -> bool:
        pass


