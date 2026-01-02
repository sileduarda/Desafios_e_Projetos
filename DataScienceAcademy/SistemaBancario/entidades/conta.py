# Módulo que define as classes de Conta (Abstrata, Corrente e Poupança).

from abc import ABC, abstractmethod
from datetime import datetime
from utilitarios.exception import SaldoInsuficienteError

class Conta(ABC):
    _total_contas = 0
    def __init__(self, numero: int, cliente):
        self.numero = numero
        self._cliente =  cliente
        self._saldo = 0.0
        self._historico = []
        Conta._total_contas +=1 

    @property
    def saldo(self): 
        return self._saldo
    
    @classmethod
    def get_total_contas(cls):
        return cls._total_contas
    
    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            self._historico.append((datetime.now(), f"Depósito de R${valor:.2f}"))
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido')


    @abstractmethod
    def sacar (self, valor: float):

        """Método abstrato para sacar um valor. Deve ser implementado pelas subclasses."""

        pass

    def extrato(self):
        """Exibe o extrato da conta."""
        print(f'\n--- Extrado da Conta Nº {self._numero} ---')
        print(f'Cliente: {self._cliente.nome}')
        print(f'Saldo atual: R${self.saldo:.2f}')
        print('Histórico de transações:')

        # caso não haja transações registradas
        if not self._historico:
            print("Nenhuma transação registrada.")
        
        for data, transacao in self._historico:
            print(f'- {data.strftime('%d%m%Y %H:%M:%S')}: {transacao}')
        print("--------------------------------------\n")

class ContaCorrente(Conta):
    """Subclasse que representa uma conta corrente"""

    def __init__(self, numero: int, cliente, limite: float = 500.0):
        # chamando o construtor da classe pai
        super().__init__(numero,cliente)

        self.limite = limite
    
    # implementando o método sacar 
    def sacar(self, valor: float):

        """Permite saque utilizando o saldo da conta mais o limite (cheque especial)."""
        if valor <= 0:
            print('Valor de saque inválido.')
            return
        
        # calcula o saldo disponível (saldo + limite)
        saldo_disponivel = self._saldo + self.limite

        # Caso o valor do saque ultrapasse o saldo disponível
        if valor > saldo_disponivel:
            raise SaldoInsuficienteError(saldo_disponivel, valor, "Saldo e limite insuficientes")
        
        self._saldo -= valor

        self._historico.append((datetime.now(), f"Saque de R${valor:/2f}"))
        print (f'Saque de R${valor:.2f} realizado com sucesso.')

class ContaPopupanca(Conta):

    def __init__(self, numero: int, cliente):
        super().__init__(numero, cliente)

    def sacar(self, valor: float):
        if valor <= 0:
            print('Valor de saque inválido')
            return

        if valor > self._saldo:
            raise SaldoInsuficienteError(self._saldo, valor)
        
        self._saldo -= valor
        self._historico.append((datetime(),f'Saque de R${valor:.2f}'))
        print(f'Saque de R4{valor:.2f} realizado com sucesso.')