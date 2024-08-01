import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando o estilo do seaborn
sns.set(style="whitegrid")

# Dados das entregas para o mês de Julho
dados_entregas = {
    'Dentro do Prazo': 882,
    'Fora do Prazo': 17,
    'Não Realizadas': 6
}

# Categorias e valores
categorias = list(dados_entregas.keys())
valores = list(dados_entregas.values())

# Cores personalizadas para cada categoria
cores = ['#4CAF50', '#FF9800', '#F44336']  # Verde, Laranja, Vermelho

# Criando o gráfico de barras
plt.figure(figsize=(10, 6))
barra = sns.barplot(x=categorias, y=valores, palette=cores)

# Adicionando rótulos de valores no topo de cada barra
for p in barra.patches:
    barra.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha='center', va='center',
                   xytext=(0, 9),
                   textcoords='offset points')

# Adicionando título e rótulos
plt.title('Status das Entregas no Mês de Julho', fontsize=16)
plt.xlabel('Status das Entregas', fontsize=14)
plt.ylabel('Quantidade', fontsize=14)

# Melhorando o layout
plt.tight_layout()

# Exibindo o gráfico
plt.show()
