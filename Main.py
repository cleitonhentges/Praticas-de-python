import pandas as pd
import seaborn as sms
import matplotlib.pyplot as plt

# Exportando arquivo csv:

file_path = 'C:/Users/cleiton/Downloads/ecommerce_preparados.csv'
df = pd.read_csv(file_path)

#Teste:
print(df.head().to_string())

#Gráfico de Histograma para as Notas:
plt.figure (figsize= (10, 6))
plt.hist(df['Nota'], color='cyan', alpha=0.8, bins=20)
plt.title('Distribuição das Notas de Avaliação de Produtos', fontsize=16, fontweight='bold')
plt.xlabel('Notas', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.tight_layout()
plt.show()

#Gráfico de Dispersão entre Nota e Preço:
plt.figure (figsize= (10, 6))
sms.scatterplot(x=df['Nota'], y=df['Preço'], color='dodgerblue', alpha=0.7, s=100)
plt.title('Relação entre Nota e Preço de Produtos', fontsize=16, fontweight='bold')
plt.xlabel('Nota de Avaliação', fontsize=12)
plt.ylabel('Preço (R$)', fontsize=12)
plt.tight_layout()
plt.show()

plt.hexbin(df['Nota'], df['Preço'], gridsize=40, cmap='Blues')
plt.colorbar(label='Densidade')
plt.xlabel('Nota do Produto')
plt.ylabel('Preço')
plt.title('Distribuição de Preço em Função da Nota do Produto')
plt.show()

#Matriz de Correlação:
plt.figure (figsize= (10, 6))
corr = df[['Nota', 'N_Avaliações']].corr()
sms.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', annot_kws={'size': 14}, linewidths=0.5, cbar=True)
plt.title('Matriz de Correlação: Nota vs N_Avaliações', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

#Convertendo e Calculando a Média da Quantidade Vendida;
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos_Cod'], errors='coerce')

grouped_data = df.groupby('Marca')['Qtd_Vendidos'].mean().sort_values(ascending=False).head(20)

#Gráfico de Barras: Quantidade Vendida por marca
plt.figure(figsize= (10, 6))
sms.barplot(x=grouped_data.values, y=grouped_data.index, hue=grouped_data.index, palette='viridis', legend=False)
plt.title('Correlação entre Quantidade Vendida e Marca (Top 20)', fontsize=16)
plt.xlabel('Quantidade Vendida (Média)', fontsize=12)
plt.ylabel('Marca', fontsize=12)
plt.tight_layout()
plt.show()

#filtro/seleção de categorias--
#Classificação das Categorias de Gênero;

df['Categoria'] = df['Gênero'].replace({
   'Masculino': 'Masculino',
   'Masculino'.lower(): 'Masculino',
   'Meninos': 'Masculino',
   'menino': 'Masculino',
   'Feminino': 'Feminino',
   'Feminino'.lower(): 'Feminino',
   'Meninas': 'Feminino',
   'Mulher': 'Feminino',
   'short menina verao look mulher': 'Feminino',
   'bermuda feminina brilho Blogueira': 'Feminino',
   'Bebês': 'Infantil',
   'Sem gênero': 'Sem gênero',
   'Sem gênero infantil': 'Infantil',
   'Unissex': 'Sem gênero',
   'roupa para gordinha pluss P ao 52': 'Feminino',
})

print(df['Categoria'])

contagem = df['Categoria'].value_counts()

print(contagem)

x = df['Categoria'].value_counts().index
y = df['Categoria'].value_counts().values

## Gráfico de Pizza para a Distribuição das Categorias:
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90, wedgeprops={'edgecolor': 'black'})
plt.title('Categoria de Produtos e Clientela', fontsize=16)
plt.tight_layout()
plt.show()

#Gráfico de Densidade:Praticas-de-python
plt.figure (figsize= (10, 6))
sms.kdeplot (df['Nota'], fill=True)
plt.title ('Densidade de Notas')
plt.xlabel('Notas')
plt.show ()

#Gráfico de Regressão:
plt.figure(figsize=(8, 6))
sms.regplot(
    x='Nota',
    y='N_Avaliações',
    data=df,
    color='#278f65',
    scatter_kws={'alpha': 0.5, 'color': '#34c289'}
)
plt.title('Relação entre Nota do Produto e Número de Avaliações', fontsize=14)
plt.xlabel('Nota do Produto', fontsize=12)
plt.ylabel('Número de Avaliações', fontsize=12)
plt.show()