# Importações 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Criando o conjunto de dados fictício

# Definindo o número de usuarios 
num_usuarios = 10000

# 1. Gerar o número de visitas ao site entre 1 e 50
visitas = np.random.randint(1,101, size = num_usuarios)

# 2. Gerar o tempo no site (distribuição normal, correlacionado com as visitas)
tempo_no_site = np.random.normal(loc = 20, scale = 5, size = num_usuarios) + (visitas * 0.5)

tempo_no_site = np.round(tempo_no_site, 2) # arredondar para 2 casas decimais

# 3. Gerar o número de itens no carrinho (dependente das visitas e do tempo)
# Usuários que visitam mais e passam mais tempo, tendem a adicionar mais itens ao carrinho 

itens_no_carrinho = np.random.randint(0,8, size = num_usuarios) + (visitas // 10) 

# Garante que o tempo no site tmabém influencia positivamente 

itens_no_carrinho += (itens_no_carrinho + (tempo_no_site // 15)).astype(int)

# 4. Gerar o valor da compra (correlacionado com os itens no carrinho) 
# Preço médio por item de R$ 35, com alguma variação aleatória 
valor_compra = (itens_no_carrinho * 35) + np.random.normal(loc = 0, scale = 10, size = num_usuarios)

type(valor_compra)
type(itens_no_carrinho)

# Se não houver itens no carrinho, o valor da compra deve ser 0
valor_compra[itens_no_carrinho == 0] = 0
valor_compra[valor_compra < 0] = 0 # Corrigir valores negativos que possam surgir
valor_compra = np.round(valor_compra, 2)

# Unindo tudo em uma única matriz (ndarray)
# Cada linha representa um usuário, cada coluna uma métrica
dados_ecommerce = np.column_stack((visitas, tempo_no_site, itens_no_carrinho, valor_compra))

print("\nShape da nossa massa de dados:", dados_ecommerce.shape)
print("\nExemplo dos 5 primeiros usuários (linhas):")
print("\nColunas: [Visitas, Tempo no Site (min), Itens no Carrinho, Valor da Compra (R$)]\n")
print(dados_ecommerce[:5])

"""
Perguntas-Chave a Serem Respondidas

A análise de dados deve responder às seguintes perguntas críticas de negócio:

- 1- Qual é o perfil médio do nosso usuário em termos de visitas, tempo de navegação e valor de compra (ticket médio)?

- 2- Quais são as características e comportamentos distintos dos nossos clientes de "Alto Valor"? Eles visitam mais o site? Passam mais tempo navegando?

- 3- Qual é o comportamento dos usuários que visitam o site, mas não realizam nenhuma compra? Onde está a oportunidade de conversão com este grupo?

- 4- Existe uma correlação estatisticamente relevante entre o tempo gasto no site, o número de itens no carrinho e o valor final da compra?

"""

# Importando a massa de dados para um DataFrame do Pandas

dados = pd.DataFrame(dados_ecommerce, columns = ['Visitas', 'TemponoSite(min)', 'ItensnoCarrinho', 'ValordaCompra(R$)']) 

# Vendo o DataFrame
print("\nVisualizando as 5 primeiras linhas do DataFrame:\n")
print(dados.head())
print(dados.tail())

# Respondendo a primeira pergunta: 
# 
# Perfil médio do usuário
perfil_medio = dados.mean()
print("\nPerfil Médio do Usuário:\n")
print(perfil_medio)

# Perfil mediano do usuário
perfil_meadiano = dados.median()
print("\nPerfil Mediano do Usuário:\n")
print(perfil_meadiano)

# Desvio padrão
dados.std()
print("\nDesvio Padrão dos Dados:\n")
print(dados.std())

# Maior e menor valor de compra 
dados.max()
print("\nMaior Valor de Compra:\n")
print(dados.max())

dados.min()
print("\nMenor Valor de Compra:\n")
print(dados.min())

# Separado a coluna 'ValordaCompra(R$)' para análise
valor_coluna = dados['ValordaCompra(R$)']
media_valor = valor_coluna.mean()
mediana_valor = valor_coluna.median()
std_valor = valor_coluna.std()

# Criando o histograma
plt.figure(figsize = (12,5))
plt.hist(valor_coluna, bins = 30, color = 'grey', edgecolor = 'black', alpha = 0.7)
plt.axvline(media_valor, color = 'red', linestyle = 'dashed', linewidth = 2, label = f'Média: R$ {media_valor:.2f}')
plt.axvline(mediana_valor, color = 'orange', linestyle = '--', linewidth = 2, label = f'Mediana: R$ {mediana_valor:.2f}')
plt.axvline(media_valor + std_valor, color = 'blue', linestyle = ':', linewidth = 2, label = f'+1 Desvio Padrão: R$ {media_valor + std_valor:.2f}')
plt.axvline(media_valor - std_valor, color = 'green', linestyle = ':', linewidth = 2, label = f'-1 Desvio Padrão: R$ {media_valor - std_valor:.2f}')
plt.title('Distribuição do Valor das Compras dos Usuários')
plt.xlabel('Valor da Compra (R$)')  
plt.ylabel('Número de Usuários')
plt.legend()
plt.grid(axis = 'y', alpha = 0.75)
plt.show()

# Respondendo a segunda pergunta: 

# Definindo um cliente de "Alto Valor" para a empresa

limite_alto_valor = dados['ValordaCompra(R$)'].quantile(0.90)  # Top 10% dos compradores

clientes_alto_valor = dados[dados['ValordaCompra(R$)'] >= limite_alto_valor]

# Estatisticas desse segmento 

media_alto_valor = clientes_alto_valor.mean()
print("\nMédia dos Clientes de Alto Valor:\n")      
print(media_alto_valor)

# Os clientes de alto valor (aqueles que estão no top 10% do valor de compra) tendem a visitar o site com maior frequência em média 41 vezes, passam mais tempo navegando (cerca de 40 minutos) e adicionam mais itens ao carrinho (em média 6 itens) em comparação com o usuário médio.
# 
# 
#
# Respondendo a terceira pergunta:
# Analisando os usuários que não realizaram compras

usuarios_sem_compra = dados[dados['ValordaCompra(R$)'] == 0] 
num_usuarios_sem_compra = usuarios_sem_compra.shape[0]
print(f"\nNúmero de Usuários que Não Realizaram Compras: {num_usuarios_sem_compra}\n")  

# Estatísticas desses usuários
media_usuarios_sem_compra = usuarios_sem_compra.mean()
print("\nMédia dos Usuários sem Compra:\n")
print(media_usuarios_sem_compra)

""" Os usuários que não realizaram compras visitaram o site em média 15 vezes e passaram cerca de 12 minutos navegando. Eles não adicionaram itens ao carrinho, indicando um desinteresse inicial. Isso sugere que talvez não haja uma oportunidade significativa para melhorar a conversão desses usuários, mas podemos tentar utilizar estratégias de remarketing, ofertas especiais ou melhorias na experiência do usuário no site."""

# Respondendo a quarta pergunta:
# Analisando correlações entre as variáveis
# A função np.corrcoef calcula a matriz de correlacao rowvar = False indica que as colunas representam variáveis diferentes

matriz_correlacao = np.corrcoef(dados.values, rowvar = False)
print("\nMatriz de Correlação entre as Variáveis:\n")   
print(matriz_correlacao)

# Colocando a matriz de correlação em forma gráfica usando seaborn
plt.figure(figsize = (8,6))
sns.heatmap(matriz_correlacao, annot = True, fmt = '.2f', cmap = 'coolwarm', xticklabels = dados.columns, yticklabels = dados.columns)
plt.title('Matriz de Correlação entre as Variáveis do E-commerce')  
plt.show()

""" Segundo a matriz de correlacao e o heatmap, podemos observar que há uma correlação positiva significativa entre o número de itens no carrinho e o valor da compra (correlação de aproximadamente 0.85). Isso indica que, à medida que os usuários adicionam mais itens ao carrinho, o valor total da compra tende a aumentar substancialmente.
Além disso, há uma correlação moderada entre o tempo no site e o valor da compra (cerca de 0.6), sugerindo que usuários que passam mais tempo navegando também tendem a gastar mais. No entanto, a correlação entre o número de visitas e o valor da compra é relativamente baixa (aproximadamente 0.3), indicando que apenas visitar o site com frequência não necessariamente leva a um aumento significativo no valor gasto. """
