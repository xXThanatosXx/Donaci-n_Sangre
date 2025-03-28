import matplotlib.pyplot as plt

# Datos de edad desde la tabla
categorias_edad = ['18-26 años', '27-35 años', '36-44 años', '45-53 años', '54-65 años']
frecuencias = [13, 17, 8, 10, 2]
# color = (0.2, # redness
#          0.3, # greenness
#          0.1, # blueness
#          0.6 # transparency
#          ) 
# Crear gráfico de barras
plt.figure(figsize=(8, 6))
bars = plt.bar(categorias_edad, frecuencias, color='#97CAC4')

# Añadir etiquetas de valor encima de las barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f'{yval}', ha='center', va='bottom')

# Personalización del gráfico
plt.title('Distribución por Edad')
plt.xlabel('Rango de Edad')
plt.ylabel('Número de Participantes')
plt.ylim(0, max(frecuencias) + 5)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
