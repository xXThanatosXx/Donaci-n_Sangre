import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Ajustar los datos para mejorar la visibilidad del límite superior de la caja para "Después"
tension_antes = [70, 72, 75, 77.5, 78, 79, 80, 80]
tension_despues = [70, 72, 75, 78, 79, 79.5, 80, 80]  # se añadió dispersión en la parte superior

# Crear el DataFrame
df = pd.DataFrame({
    'Tensión Arterial Diastólica': tension_antes + tension_despues,
    'Momento': ['Antes'] * len(tension_antes) + ['Después'] * len(tension_despues)
})

# Crear el diagrama de cajas y bigotes
plt.figure(figsize=(8, 6))
sns.boxplot(x='Momento',
            y='Tensión Arterial Diastólica',
            data=df,
            palette="Set3",
            width=0.5,
            fliersize=4,
            linewidth=1.5)

# Dibujar un recuadro similar a una leyenda personalizada
plt.plot([], [], ' ', label='Mediana Antes: 77.5')
plt.plot([], [], ' ', label='Mediana Después: 80')
plt.plot([], [], ' ', label='Valor p = 0,809')
plt.legend(title='Resumen', loc=1, frameon=True)

# Personalización del gráfico
plt.title('Comparación de Tensión Arterial Diastólica')
plt.ylabel('Tensión Arterial Diastólica (mmHg)')
plt.xlabel('Momento')
plt.ylim(65, 85)
plt.xlim(-0.5, 2)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
