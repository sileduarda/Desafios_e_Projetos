#main -- Funçao Geral -- 
from operacoes.banco import Banco

from utilitarios.exception import SaldoInsuficienteError, ContaInexistenteError

# Função que exibe o menu principal 
def menuPrincipal():
    largura = 30  # largura total do menu
    print('=' * largura)
    print("--- Banco BB Cash ---".center(largura))
    print("Bem-vindo ao Banco BB Cash!".center(largura))
    print('=' * largura)
    print("Menu Principal".center(largura))
    print('=' * largura)
    print('1. Adicionar Cliente')
    print('2. Criar Conta')
    print('3. Acessar Conta')
    print('4. Sair')
    print('=' * largura) 

    return input('Escolha uma opção: ') 



def menuConta(banco):

    try:
        # Solicitanto ao usuário o número da conta
        num_conta = int(input("Digite o número da conta: "))

        # Busca a conta no banco
        conta = banco.buscar_conta(num_conta)

        while True:
            print(f"\n--- Operações para Conta Nº {conta._numero} ---")
            print(f"Cliente: {conta._cliente.nome} | Saldo: R${conta.saldo:.2f}")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver Extrato")
            print("4. Voltar ao Menu Principal")

            # Lê a opção do usuário
            opcao = input("Escolha uma opção: ")
            if opcao == '1':

                # Deposita valor na conta
                valor = float(input("Digite o valor para depósito: "))
                conta.depositar(valor)
            
            elif opcao == '2':
                
                # Tenta realizar um saque
                try:
                    
                    valor = float(input("Digite o valor para saque: "))
                    conta.sacar(valor) 
                
                except SaldoInsuficienteError as e:
                    print(f"Erro na operação: {e}")
            
            elif opcao == '3':
                
                # Exibe o extrato da conta
                conta.extrato()
            
            elif opcao == '4':
                
                # Sai do menu da conta e retorna ao menu principal
                break
            
            else:
                print("Opção inválida. Tente novamente.")

     # Exceção caso a conta não exista
    except ContaInexistenteError as e:
        print(f"Erro: {e}")
    
    # Exceção para entradas inválidas (não numéricas)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número.")


# Função principal
def main():

    # Cria o objeto banco
    banco = Banco("Banco BB Cash")
    while True:
        opcao = menuPrincipal()

        if opcao == 4:
            print('Obrigada por utilizar o nosso banco! Até logo!')  
            break
        elif opcao == 1:
            nome = input('Digite o nome do cliete: ')
            cpf = input("Digite o CPF do cliente: ")
            banco.adicionar_cliente(nome,cpf)

        elif opcao == 2:
            # Cria uma nova conta
            cpf = input('Digite o CPF do cliente para vincular a conta: ')
            cliente = banco._clientes.get(cpf)

            if cliente:
                tipo = input("Digite o tipo da conta (corrente/poupanca): ")
                banco.criar_conta(cliente, tipo)
            else: 
                print('Cliente não encontrado. Cadastre o cliente primeiro.')

        elif opcao == 3:

            # Abre o menu de operações de uma conta 
            menuConta(banco)

        else:
             print("Opção inválida, digite novamente!")

# Ponto de entrada da aplicação
if __name__ == "__main__":
    main()



