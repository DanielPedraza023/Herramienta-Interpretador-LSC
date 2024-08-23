import matplotlib.pyplot as plt

# Datos simulados
señales = ['A', 'B', 'E', 'K', 'M', 'N', 'O', 'Q', 'S', 'U', 'X', 'Z', 'ESPACIO']
precisiones = [0.95, 0.90, 0.92, 0.85, 0.88, 0.87, 0.94, 0.80, 0.89, 0.93, 0.75, 0.78, 0.98]
tiempos_respuesta = [0.1, 0.12, 0.09, 0.15, 0.11, 0.14, 0.08, 0.18, 0.13, 0.07, 0.20, 0.17, 0.05]  # en segundos

# Crear el diagrama de dispersión
plt.figure(figsize=(12, 6))
plt.scatter(tiempos_respuesta, precisiones, color='blue')

# Etiquetas y título
for i, señal in enumerate(señales):
    plt.annotate(señal, (tiempos_respuesta[i], precisiones[i]))

plt.xlabel('Tiempo de Respuesta (s)')
plt.ylabel('Precisión')
plt.title('Diagrama de Dispersión de Precisión vs. Tiempo de Respuesta')
plt.xlim(0, max(tiempos_respuesta) + 0.05)
plt.ylim(0, 1)
plt.grid(True)
plt.show()
