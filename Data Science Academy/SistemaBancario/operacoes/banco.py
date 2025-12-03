from entidades.cliente import Cliente

from entidades.conta import Conta, ContaCorrente, ContaPopupanca

from utilitarios.exception import ContaInexistenteError

# definindo a classe banco
class Banco:
    """Classe que gerencia as operações do banco. Demonstra Composição, pois "tem clientes e contas"""

    # Construtor da classe
    def __init__(self, nome: str):
        self.nome = nome
        self._clientes = {}
        self._contas = {}

    # Metodo para adicionar um novo cliente ao banco 

    def adicionar_cliente(self, nome: str, cpf: str) -> Cliente: 

        """Cria e adiciona um novo cliente ao banco"""
    # Verifica se o cliente já existe
        if cpf in self._clientes:
            print("Erro: CPF já cadastrado.")
            return self._clientes[cpf]
    
        # Criando objeto cliente e adicionando ao dic
        novo_cliente = Cliente(nome, cpf)
        self._clientes[cpf] = novo_cliente
        print(f'Cliente {nome} adicionando com sucesso!')
        return novo_cliente
    
    def criar_conta(self, cliente: Cliente, tipo: str) -> Conta: 

        """Cria uma nova conta para um cliente existente."""

        numero_conta = Conta.get_total_contas() + 1
        # Cria corrente
        if tipo.lower() == 'corrente':
            nova_conta = ContaCorrente(numero_conta, cliente)

        # Cria poupança
        elif tipo.lower() =='poupanca':
            nova_conta = ContaPopupanca(numero_conta, cliente)
        
        else:
            print('Tipo de cona inválido.')

        # adiciona a conta ao dic de contas
        self._contas[numero_conta] = nova_conta

        # Associa a conta ao cliente 
        cliente.adicionar_conta(nova_conta)
        print(f'Conta {tipo} nº {numero_conta} criada para o cliente {cliente.nome}.')

        return nova_conta
    
    # Buscando conta pelo numero
    def buscar_conta(self, numero_conta:int) -> Conta:
        
        conta = self._contas.get(numero_conta)

        if not conta:
            raise ContaInexistenteError(numero_conta)
        return conta