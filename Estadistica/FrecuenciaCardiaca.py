import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos de frecuencia cardiaca (antes y después)
frecuencia_antes = [75, 76, 77, 78, 79, 80, 81, 82]  # valores dentro del rango del RIQ
frecuencia_despues = [74, 75, 76, 77, 80, 83, 85, 87]  # valores dentro del rango del RIQ

# Crear el DataFrame
df = pd.DataFrame({
    'Frecuencia Cardíaca': frecuencia_antes + frecuencia_despues,
    'Momento': ['Antes'] * len(frecuencia_antes) + ['Después'] * len(frecuencia_despues)
})

# Crear el diagrama de cajas y bigotes
plt.figure(figsize=(8, 6))
sns.boxplot(x='Momento', y='Frecuencia Cardíaca', data=df, palette="Set3")

# Dibujar un recuadro similar a una leyenda personalizada
plt.plot([], [], ' ', label='Mediana Antes: 79')
plt.plot([], [], ' ', label='Mediana Después: 80')
plt.plot([], [], ' ', label='Valor p = 0,048')
plt.legend(title='Resumen', loc='best', frameon=True)

# Personalización del gráfico
plt.title('Comparación de Frecuencia Cardíaca')
plt.ylabel('Frecuencia Cardíaca (lpm)')
plt.xlabel('Momento')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
