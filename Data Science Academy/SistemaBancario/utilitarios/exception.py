## Define a exceção para saldo insuficiente em operações de saque 

class SaldoInsuficienteError(Exception):
    """Exceção levantada quando uam operação de saque excede o saldo disponível."""

    # Contruindo excessão
    def __init__(self, saldo_atual, valor_saque, mensagem = "Saldo insuficiente para realizar o saque."):

        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque

         # Mensagem detalhada de erro com saldo atual e valor do saque
        self.mensagem = f"{mensagem} Saldo atual: R${saldo_atual:.2f}, Tentativa de saque: R${valor_saque:.2f}"

        # Chama o construtor da classe Exception com a mensagem
        super().__init__(self.mensagem)

# Define a exceção para operações em contas inexistentes
class ContaInexistenteError(Exception):
    
    # Construtor da exceção
    def __init__(self, numero_conta, mensagem="A conta especificada não foi encontrada."):
        
        # Número da conta que não foi encontrada
        self.numero_conta = numero_conta
        
        # Mensagem detalhada de erro com o número da conta
        self.mensagem = f"{mensagem} Número da conta: {numero_conta}"
        
        # Chama o construtor da classe Exception com a mensagem
        super().__init__(self.mensagem)
