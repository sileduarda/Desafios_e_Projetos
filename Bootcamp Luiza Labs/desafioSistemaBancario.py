# Variáveis Globais
limite = 500
saldo = 0
numero_saques = 0
LIMITE_SAQUES = 3


def depositar():
    global saldo
    deposito = float(input('Qual valor deseja depositar? '))
    if deposito > 0:
        saldo += deposito
        print(f'Você depositou R${deposito} reais. Deseja continuar?')
    extrato()


def sacar():
    global LIMITE_SAQUES, numero_saques, saldo, limite
    saque = float(input('Qual valor deseja sacar? '))
# BLOCO 1 - VERIFICANDO LIMITES
    excedeu_limite_total = saque > saldo + limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    if excedeu_limite_total:
        print('Falha na operação, você não possui mais limite especial')
    elif excedeu_saques:
        print('Falha na operação, limite de saques insuficiente')
    # BLOCO 2 - SAQUE DE FATO
    saldo -= saque
    if saldo < 0:
       limite += saldo
       print(f'Você utilizou R${saldo} do seu limite especial')
    else:
        print(f'Você sacou R${saque} reais.')


def extrato():
    global saldo, limite
    print(f'Seu saldo atual é de R${saldo} e seu limite especial é de {limite}')

# ---------------------------
#     PROGRAMA PRINCIPAL
# ---------------------------
def main():
    while True:
        print("\n=== Sistema Bancário ===")
        print("1 - Saque")
        print("2 - Depósito")
        print("3 - Visualizar Extrato")
        print("0 - Sair")
        print("===========================")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            sacar()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            extrato()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

main()


























