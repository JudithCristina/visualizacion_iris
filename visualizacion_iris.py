import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset Iris desde seaborn
df = sns.load_dataset('iris')

# Mostrar las primeras filas
print(df.head())

# Gráfico 1: Cantidad de flores por especie
df['species'].value_counts().plot(kind='bar')
plt.title('Cantidad de flores por especie')
plt.xlabel('Especie')
plt.ylabel('Cantidad')
plt.tight_layout()
plt.savefig('grafico_flores_por_especie.png')
plt.show()

# Gráfico 2: Boxplot del largo de pétalo por especie
sns.boxplot(data=df, x='species', y='petal_length')
plt.title('Largo de pétalo por especie')
plt.tight_layout()
plt.savefig('boxplot_petal_length.png')
plt.show()
