# Volver a importar las librerías después del reinicio del kernel
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos de la escala Likert
categorias = ['Totalmente satisfecho', 'Muy satisfecho', 'Ni satisfecho ni insatisfecho']
porcentajes = [42, 48, 10]
colores = ['#66c2a5', '#fc8d62', '#8da0cb']

# Crear gráfico de barras horizontales
plt.figure(figsize=(10, 5))
bars = plt.barh(categorias, porcentajes, color=colores)

# Añadir etiquetas de porcentaje al final de cada barra
for bar in bars:
    plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
             f'{bar.get_width()}%', va='center', fontsize=10)

# Personalización del gráfico
plt.title('Resultados de Satisfacción según Escala Likert')
plt.xlabel('Porcentaje (%)')
plt.xlim(0, 100)
plt.gca().invert_yaxis()  # Para que la categoría más alta aparezca arriba
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
