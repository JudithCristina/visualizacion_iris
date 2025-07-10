import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Cargar el dataset Iris desde seaborn
df = sns.load_dataset('iris')


# Mostrar las primeras filas
print(df.head())


# Gráfico 1: Cantidad de flores por especie
df['species'].value_counts().plot(kind='bar')
plt.title('Cantidad de flores por especie xxxxxxyyy')
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

# Gráfico 3: Dispersión largo vs. ancho de pétalo, coloreado por especie
sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species')
plt.title('Dispersión: largo vs. ancho de pétalo por especie')
plt.xlabel('Largo de pétalo')
plt.ylabel('Ancho de pétalo')
plt.tight_layout()
plt.savefig('scatter_petal_length_vs_width.png')
plt.show()

# Gráfico 4: Dispersión largo vs. ancho de pétalo, coloreado por especie
sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species')
plt.title('Dispersión: largo vs. ancho de pétalo por especie')
plt.xlabel('Largo de pétalo')
plt.ylabel('Ancho de pétalo')
plt.tight_layout()
plt.savefig('scatter_petal_length_vs_width.png')
plt.show()

# --- Nueva dispersion de largo de sépalo ---
plt.figure(figsize=(6,4))
sns.histplot(iris['sepal_length'], bins=10, kde=True)
plt.title('Distribución del largo de sépalo')
plt.xlabel('Largo de sépalo (cm)')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.savefig('histograma_sepal_length_Nuevo.png')
plt.show()