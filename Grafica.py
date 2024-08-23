import pandas as pd
import matplotlib.pyplot as plt

# Leer datos del archivo CSV
data = pd.read_csv('results.csv', skipinitialspace=True)

# Obtener datos de precisión para todas las épocas
epochs = data['epoch']
precision_B = data['metrics/precision(B)']
precision_M = data['metrics/precision(M)']
recall_M = data['metrics/recall(M)']



# Crear gráfico de precisión en función de las épocas
plt.figure(figsize=(10, 6))
#plt.plot(epochs, precision_B, label='Precision (B)', marker='o')
#plt.plot(epochs, precision_M, label='Precision (M)', marker='o')
plt.plot(epochs, recall_M, label = 'Recall (M)', marker = 'H')
plt.xlabel('Época')
plt.ylabel('Error de Precisión')
plt.title('Precisión en función de las épocas')
# Configurar el eje y para que vaya de 0 a 1
#plt.ylim(0, 1)
plt.legend()
plt.grid(True)
plt.show()
