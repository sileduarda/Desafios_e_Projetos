# Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador, depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitorias - derrotas)
# Se vitorias for menor do que 10 = Ferro
# Se vitorias for entre 11 e 20 = Bronze
# Se vitorias for entre 21 e 50 = Prata
# Se vitorias for entre 51 e 80 = Ouro
# Se vitorias for entre 81 e 90 = Diamante
# Se vitorias for entre 91 e 100 = Lendário
# Se vitorias for maior ou igual a 101 = Imortal
# Ao final deve se exibir uma mensagem: 
# O Herói tem o saldo de {saldoVitorias} e está no nível {nível}

def calculadoraDePartidasRankeadas(vitorias, derrotas):
    saldoVitorias = vitorias - derrotas
    if saldoVitorias < 10:
        nível = 'Ferro'
    elif 11 <= saldoVitorias <= 20:  
        nível = 'Bronze'
    elif 21 <= saldoVitorias <= 50:
        nível = 'Prata'
    elif 51 <= saldoVitorias <= 80:
        nível = 'Ouro'
    elif 81 <= saldoVitorias <= 90:
        nível = 'Diamante'
    elif 91 <= saldoVitorias <= 100:
        nível = 'Lendário'
    elif saldoVitorias >= 101:
        nível = 'Imortal' 
    print(f'O héroi tem saldo de {saldoVitorias} e está no nível {nível}')
    
    
calculadoraDePartidasRankeadas(150, 2)