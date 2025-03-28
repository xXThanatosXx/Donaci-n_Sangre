import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#Frecuencia respiratoria (lpm)	17 (17 - 18)	17 (16 - 18)	0,138
# Datos de frecuencia respiratoria (antes y después)
frecuencia_antes = [17, 17, 17, 17, 17, 18, 18, 18]
frecuencia_despues = [16, 16, 17, 17, 17, 18, 18, 18]

# Crear el DataFrame
df = pd.DataFrame({
    'Frecuencia respiratoria': frecuencia_antes + frecuencia_despues,
    'Momento': ['Antes'] * len(frecuencia_antes) + ['Después'] * len(frecuencia_despues)
})

# Crear el diagrama de cajas y bigotes
plt.figure(figsize=(8, 6))
sns.boxplot(x='Momento', y='Frecuencia respiratoria', data=df, palette="Set3")

# Dibujar un recuadro similar a una leyenda personalizada
plt.plot([], [], ' ', label='Mediana Antes: 17')
plt.plot([], [], ' ', label='Mediana Después: 17')
plt.plot([], [], ' ', label='Valor p = 0,138')
plt.legend(title='Resumen', loc='best', frameon=True)

# Personalización del gráfico
plt.title('Comparación de Frecuencia respiratoria')
plt.ylabel('Frecuencia respiratoria(rpm)')
plt.xlabel('Momento')
plt.tight_layout()
plt.ylim(14, 20)  # ajustar para resaltar la diferencia
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
