import pandas as pd

# Especificar el delimitador y la codificación al leer el archivo CSV
data = pd.read_csv('results.csv', delimiter=',', encoding='utf-8')

# Verificar si 'epoch' está en las columnas
if 'epoch' in data.columns:
    print("La columna 'epoch' se encuentra en el DataFrame.")
else:
    print("La columna 'epoch' no se encontró en el DataFrame.")
