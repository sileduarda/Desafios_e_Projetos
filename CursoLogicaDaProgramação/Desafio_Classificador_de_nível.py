'''# Desafio Classificador de nível de Herói

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões

## Objetivo

Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 5.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nivel}**"'''

heroi = input("Digite o nome do seu herói: ")
xp = int(input("Digite experiência do seu herói: "))

if xp <= 1000:
    print(f'O Herói {heroi} está no nível Ferro')
if xp >= 1001 and xp <= 2000:
    print(f'O Herói {heroi} está no nível Bronze') 
if xp >= 2001 and xp <= 5000:
    print(f'O Herói {heroi} está no nível Prata')
if xp >= 5001 and xp <= 7000:
    print(f'O Herói {heroi} está no nível Ouro')
if xp >= 7001 and xp <= 8000: 
    print(f'O Herói {heroi} está no nível Platina')
if xp >= 8001 and xp <= 9000:
    print(f'O Herói {heroi} está no nível Ascendente')
if xp >= 9001 and xp <= 10000:
    print(f'O Herói {heroi} está no nível Imortal')
if xp >= 10001:
    print (f'O Herói {heroi} está no nível Radiante')