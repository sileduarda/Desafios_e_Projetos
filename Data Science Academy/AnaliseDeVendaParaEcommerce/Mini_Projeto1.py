# Importando as bibliotecas que serão utilizadas 

# Instala o pacote watermark - gerar marca d'agua com versões de outros pacotes, ! indica que vou executar um comando de sistema operacional, pip é instalador de pacotes na linguagem python, -q é instalação silenciosa e -U é para realizar o update se o pacote já tiver instalado 


# Importação da biblioteca para manipulação de dados em tabelas
import pandas as pd  

# Importação da biblioteca NumPy para operações matemáticas e arrays
import numpy as np  

# Importação da biblioteca Matplotlib para geração de gráficos
import matplotlib.pyplot as plt  

# Importação da biblioteca Seaborn para visualização estatística de dados
import seaborn as sns  

# Importação da biblioteca random para geração de números aleatórios
import random  

# Importação das classes datetime e timedelta para manipulação de datas e intervalos de tempo
from datetime import datetime, timedelta  


import platform

# Criando a marca d'agua
print("Autor: Maria Eduarda | DSA")
print("Python:", platform.python_version())
print("Pandas:", pd.__version__)
print("Numpy:", np.__version__)



# Criando função para geração de dados fictícios 
def dsa_gera_dados(num_registros = 600):
    """" 
    Gera um DataFrame do Pandas com dados de vendas fictícios 
    """

    # Mensagem incial indicando a quantidade de registros a serem gerados 
    print(f'\nIniciando a geração de {num_registros} registros de vendas...')

    # Dic com produtos, categorias e preços:
    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
    }

# Cria uma list apenas com os nomes dos produtos 
    lista_produtos = list(produtos.keys())

# Dicionário com cidade e seus respectivos estados 
    cidades_estados = {
        'São Paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo Horizonte': 'MG', 'Porto Alegre': 'RS', 'Salvador':'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'
    }
    # Cria uma lista apenas com os nomes das cidades 
    lista_cidades = list(cidades_estados.keys())

    # Lista que armazenará os registros de vendas
    dados_vendas = []

    # Define a data inicial dos pedidos
    data_inicial  = datetime(2026, 1, 1)

    # Loop para gerar os registros de vendas 
    for i in range(num_registros):

        # Seleciona aleatoriamente um produto
        produto_nome = random.choice(lista_produtos)

        # Seleciona aleatoriamente uma cidade
        cidade = random.choice(lista_cidades)

        # Gera uma quantidade de produtos vendida entre 1 e 7
        quantidade = np.random.randint(1,8)

        # Calcula a data do pedido a partir da data inicial
        data_pedido = data_inicial + timedelta(days = int(i/5), hours = random.randint(0, 23))

        # Se o produto for Mouse ou Teclado, aplica desconto ateatório de até 10% 
        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome]['preco']

        # Adiciona um registro de venda à lista
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100,150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]

        })

    # Mensagem final indicando que a geração terminou
    print('Geração de dados concluída.\n')

    # Retorna os dados no formato de DataFrame 
    return pd.DataFrame(dados_vendas)
    


# Gerar, Carregar e Explorar os Dados 
# Gera os dados chamando a função criada anteriormente
df_vendas = dsa_gera_dados(1000)

# Exibindo o tipo 
type(df_vendas)

# Shape 
df_vendas.shape

# Exibe as 5 primeiras linhas do DataFrama
df_vendas.head()

#Exibe as 5 ultimas linhas do DataFrame
df_vendas.tail()

# Exibindo informações gerais sobre o DataFrame (tipos de dados, valores não nulos)
df_vendas.info()

# Resumo estatístico
df_vendas.describe()

# Tipos de dados 
df_vendas.dtypes

# Limpeza, Pré Processamento e Engenharia de Atributos 

# A engenharia de atributos torna os dados implícitos, explicitos

## # Se a coluna 'Data_Pedido' não estiver como tipo datetime, precisamos fazer a conversão explícita
# A coluna pode ser usada para análise temporal
df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])

# Engenharia de atributos - porque um dos objetivos do problema de negócio é gerar o faturamento explícito no df.
# Criando a coluna 'Faturamento' (preço x quantidade) para ter a receita de cada pedido
df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']

# Engenharia de atributos
# Usando a função lambda para criar uma coluna de status de entrega
df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(lambda estado: ' Rápida' if estado in ['SP', 'RJ', 'MG'] else 'Normal')

# Exibe informações gerais sobre o DataFrame (tipo de dados, valores não nulos)
df_vendas.info()

#Exibe as 5 primeiras linhas novamente para ver as novas colunas 
df_vendas.head()



# Analises 

## Analise 1 
# Quais os top 10 produtos mais vendidos? 

# Agrupa por nome do produto, soma a quantidade e ordena para encontrar os mais vendidos 
top_10_produtos = df_vendas.groupby('Nome_Produto')['Quantidade'].sum().sort_values(ascending = False).head(10)

# Exibindo
top_10_produtos

df_vendas['Quantidade'].dtype
df_vendas['Quantidade'].describe()



# Pegando a media
group_mean = top_10_produtos.mean()


# Define um estilo para os gráficos 
sns.set_style('whitegrid')
# Cria a figura e os eixos
plt.figure(figsize = (12,7))
#Cria o grafico de barras horizontais
top_10_produtos.sort_values(ascending = True).plot(kind='barh', color = 'purple')




# Melhorando o gráfico
plt.title('Top 10 Produtos Mais Vendidos', fontsize = 16)
plt.xlabel('Quantidade Vendida', fontsize = 12)
plt.ylabel('Produto', fontsize = 12)

# Adc linha vertical
plt.axvline(group_mean, ls='--', color='r', label = f'Média: {group_mean:.2f}')

# Exibe o grafico
plt.legend()
plt.tight_layout()
plt.show()


## Analise 2
# Qual foi o faturamento mensal? 

df_vendas.head()

# Criando uma coluna mes para cilitar o agrupamento mensal 

df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')

df_vendas.head()
df_vendas.tail()

# Agrupando por mês e somando o faturamento
faturamento_mensal = df_vendas.groupby('Mes')['Faturamento'].sum()

# Convetendo o índice de volta para datetime para facilitar a plotagem
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')

# Formata para duas casas decimais
faturamento_mensal.map('R${:,.2f}'.format)

# Cria uma nova figura com tamanho de 12 por 6 polegadas
plt.figure(figsize=(12,6))

#Plota os dados de faturamento mensal em formato de linha 
faturamento_mensal.plot(kind = 'line', marker = 'o', linestyle = '-' , color = 'green')

# Definindo o título e os rótulos dos eixos
plt.title('Evolução do Faturamento Mensal', fontsize = 16)
plt.xlabel('Mês', fontsize = 12)
plt.ylabel('Faturamento (R$)', fontsize = 12)

# Rotacionando os rótulos do eixo x para melhor visualização
plt.xticks(rotation = 45)

# Adiciona uma grade com estilo tracejado e linhas finas 
plt.grid(True, which = 'both', linestyle = '--', linewidth = 0.5)   

# Ajusta automaticamente os elementos para evitar sobreposição
plt.tight_layout()

# Exibe o gráfico
plt.show()  

## Analise 3
# Qual o total de vendas pro estado? 
# Agrupando por estado e somando o faturamento
vendas_estado = df_vendas.groupby('Estado')['Faturamento'].sum().sort_values(ascending = False)

vendas_estado.map('R${:,.2f}'.format)

# Criando a figura 
plt.figure(figsize = (12,7))
# Plotando o gráfico de barras horizontais
vendas_estado.plot(kind = 'barh', color = sns.color_palette())

plt.title('Faturamento por Estado', fontsize = 16)
plt.xlabel('Faturamento (R$)', fontsize = 12)
plt.ylabel('Estado', fontsize = 12)

plt.xticks(rotation = 0)

plt.tight_layout() # ajusta os elementos para evitar sobreposição
plt.show() #exibe o gráfico

# Analise 4
#Qual o faturamento total por categoria de produto? 

# Agrupando por categoria e somando o faturamento
faturamento_categoria = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending=False)

faturamento_categoria.map('R${:,.2f}'.format)

