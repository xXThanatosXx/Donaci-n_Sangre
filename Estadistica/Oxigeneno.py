import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos de saturación de oxígeno (antes y después) basados en el RIQ proporcionado: 
# Antes (93-95), Después (92.25-95), Mediana Antes: 95, Mediana Después: 93.5, Valor p: 0.125
saturacion_antes = [93, 94, 94, 94, 95, 95, 95, 95]
saturacion_despues = [92.25, 93, 93, 93.5, 94, 94.5, 95, 95]

# Crear el DataFrame
df = pd.DataFrame({
    'Saturación de Oxígeno': saturacion_antes + saturacion_despues,
    'Momento': ['Antes'] * len(saturacion_antes) + ['Después'] * len(saturacion_despues)
})

# Crear el diagrama de cajas y bigotes
plt.figure(figsize=(8, 6))
sns.boxplot(x='Momento',
            y='Saturación de Oxígeno',
            data=df,
            palette="Set3",
            width=0.5,
            fliersize=4,
            linewidth=1.5)

# Dibujar un recuadro similar a una leyenda personalizada
plt.plot([], [], ' ', label='Mediana Antes: 95')
plt.plot([], [], ' ', label='Mediana Después: 93.5')
plt.plot([], [], ' ', label='Valor p = 0,125')
plt.legend(title='Resumen', loc='best', frameon=True)

# Personalización del gráfico
plt.title('Comparación de Saturación de Oxígeno')
plt.ylabel('Saturación de Oxígeno (%)')
plt.xlabel('Momento')
plt.ylim(91.5, 96.5)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
