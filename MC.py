# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.metrics import ConfusionMatrixDisplay

# # Definir las clases
# clases = [chr(i) for i in range(65, 91)] + ["ESPACIO"]  # A-Z + ESPACIO

# # Inicializar la matriz de confusión (27x27, ya que hay 27 clases)
# matriz_confusion = np.zeros((len(clases), len(clases)), dtype=int)

# # Rellenar la matriz de confusión con los errores proporcionados
# # Filas representan las clases verdaderas, columnas las clases predichas

# # A --> Confusión con la clase "Y"
# matriz_confusion[clases.index('A'), clases.index('A')] = 199  # 200 - 1
# matriz_confusion[clases.index('A'), clases.index('Y')] = 1

# # B --> 1 confusión con la clase "ESPACIO", 1 confusión con la clase "T"
# matriz_confusion[clases.index('B'), clases.index('B')] = 198  # 200 - 2
# matriz_confusion[clases.index('B'), clases.index('ESPACIO')] = 1
# matriz_confusion[clases.index('B'), clases.index('T')] = 1

# # C --> 2 confusiones con la clase "O"
# matriz_confusion[clases.index('C'), clases.index('C')] = 198  # 200 - 2
# matriz_confusion[clases.index('C'), clases.index('O')] = 2

# # D --> 1 confusión con la clase "O", 1 con la clase "Q"
# matriz_confusion[clases.index('D'), clases.index('D')] = 198  # 200 - 2
# matriz_confusion[clases.index('D'), clases.index('O')] = 1
# matriz_confusion[clases.index('D'), clases.index('Q')] = 1

# # E --> No tuvo ninguna confusión
# matriz_confusion[clases.index('E'), clases.index('E')] = 200

# # F --> 1 confusión con la clase "L"
# matriz_confusion[clases.index('F'), clases.index('F')] = 199  # 200 - 1
# matriz_confusion[clases.index('F'), clases.index('L')] = 1

# # G --> 1 confusión con "X"
# matriz_confusion[clases.index('G'), clases.index('G')] = 199  # 200 - 1
# matriz_confusion[clases.index('G'), clases.index('X')] = 1

# # H --> No tuvo confusión
# matriz_confusion[clases.index('H'), clases.index('H')] = 200

# # I --> 3 confusiones con "J"
# matriz_confusion[clases.index('I'), clases.index('I')] = 197  # 200 - 3
# matriz_confusion[clases.index('I'), clases.index('J')] = 3

# # J --> No tuvo confusión
# matriz_confusion[clases.index('J'), clases.index('J')] = 200

# # K --> No tuvo confusión
# matriz_confusion[clases.index('K'), clases.index('K')] = 200

# # L --> 1 con "F"
# matriz_confusion[clases.index('L'), clases.index('L')] = 199  # 200 - 1
# matriz_confusion[clases.index('L'), clases.index('F')] = 1

# # M --> 1 con "N"
# matriz_confusion[clases.index('M'), clases.index('M')] = 199  # 200 - 1
# matriz_confusion[clases.index('M'), clases.index('N')] = 1

# # N --> 1 con "M"
# matriz_confusion[clases.index('N'), clases.index('N')] = 199  # 200 - 1
# matriz_confusion[clases.index('N'), clases.index('M')] = 1

# # O --> 2 con "Q"
# matriz_confusion[clases.index('O'), clases.index('O')] = 198  # 200 - 2
# matriz_confusion[clases.index('O'), clases.index('Q')] = 2

# # P --> No tuvo confusión
# matriz_confusion[clases.index('P'), clases.index('P')] = 200

# # Q --> 1 con "O"
# matriz_confusion[clases.index('Q'), clases.index('Q')] = 199  # 200 - 1
# matriz_confusion[clases.index('Q'), clases.index('O')] = 1

# # R --> 1 con "S"
# matriz_confusion[clases.index('R'), clases.index('R')] = 199  # 200 - 1
# matriz_confusion[clases.index('R'), clases.index('S')] = 1

# # S --> 2 con "Z"
# matriz_confusion[clases.index('S'), clases.index('S')] = 198  # 200 - 2
# matriz_confusion[clases.index('S'), clases.index('Z')] = 2

# # T --> 1 con "ESPACIO"
# matriz_confusion[clases.index('T'), clases.index('T')] = 199  # 200 - 1
# matriz_confusion[clases.index('T'), clases.index('ESPACIO')] = 1

# # U --> No tuvo confusión
# matriz_confusion[clases.index('U'), clases.index('U')] = 200

# # V --> 2 con "W"
# matriz_confusion[clases.index('V'), clases.index('V')] = 198  # 200 - 2
# matriz_confusion[clases.index('V'), clases.index('W')] = 2

# # W --> 1 con "V"
# matriz_confusion[clases.index('W'), clases.index('W')] = 199  # 200 - 1
# matriz_confusion[clases.index('W'), clases.index('V')] = 1

# # X --> 1 con "G"
# matriz_confusion[clases.index('X'), clases.index('X')] = 199  # 200 - 1
# matriz_confusion[clases.index('X'), clases.index('G')] = 1

# # Y --> No tuvo confusión
# matriz_confusion[clases.index('Y'), clases.index('Y')] = 200

# # Z --> 1 con "S"
# matriz_confusion[clases.index('Z'), clases.index('Z')] = 199  # 200 - 1
# matriz_confusion[clases.index('Z'), clases.index('S')] = 1

# # ESPACIO --> 2 con "T"
# matriz_confusion[clases.index('ESPACIO'), clases.index('ESPACIO')] = 198  # 200 - 2
# matriz_confusion[clases.index('ESPACIO'), clases.index('T')] = 2

# # Visualizar la matriz de confusión
# disp = ConfusionMatrixDisplay(confusion_matrix=matriz_confusion, display_labels=clases)

# plt.figure(figsize=(20, 20))  # Aumenta el tamaño de la figura
# disp.plot(cmap=plt.cm.Blues, values_format='d')  # Usa formato entero
# plt.xticks(rotation=90, ha='right', fontsize=10)  # Ajusta el tamaño de la fuente y rota las etiquetas del eje x
# plt.yticks(rotation=0, fontsize=10)  # Ajusta el tamaño de la fuente de las etiquetas del eje y
# plt.xlabel("Clase Predicha", fontsize=12)
# plt.ylabel("Clase Verdadera", fontsize=12)
# plt.title("Matriz de Confusión", fontsize=14)
# plt.tight_layout()  # Ajusta el espaciado
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.metrics import ConfusionMatrixDisplay

# # Definir las clases
# clases = [chr(i) for i in range(65, 91)] + ["ESPACIO"]  # A-Z + ESPACIO

# # Inicializar la matriz de confusión (27x27, ya que hay 27 clases)
# matriz_confusion = np.zeros((len(clases), len(clases)), dtype=int)

# # Rellenar la matriz de confusión con los errores proporcionados
# # Filas representan las clases verdaderas, columnas las clases predichas

# # A --> Confusión con la clase "Y"
# matriz_confusion[clases.index('A'), clases.index('A')] = 199  # 200 - 1
# matriz_confusion[clases.index('A'), clases.index('Y')] = 1

# # B --> 1 confusión con la clase "ESPACIO", 1 confusión con la clase "T"
# matriz_confusion[clases.index('B'), clases.index('B')] = 198  # 200 - 2
# matriz_confusion[clases.index('B'), clases.index('ESPACIO')] = 1
# matriz_confusion[clases.index('B'), clases.index('T')] = 1

# # C --> 2 confusiones con la clase "O"
# matriz_confusion[clases.index('C'), clases.index('C')] = 198  # 200 - 2
# matriz_confusion[clases.index('C'), clases.index('O')] = 2

# # D --> 1 confusión con la clase "O", 1 con la clase "Q"
# matriz_confusion[clases.index('D'), clases.index('D')] = 198  # 200 - 2
# matriz_confusion[clases.index('D'), clases.index('O')] = 1
# matriz_confusion[clases.index('D'), clases.index('Q')] = 1

# # E --> No tuvo ninguna confusión
# matriz_confusion[clases.index('E'), clases.index('E')] = 200

# # F --> 1 confusión con la clase "L"
# matriz_confusion[clases.index('F'), clases.index('F')] = 199  # 200 - 1
# matriz_confusion[clases.index('F'), clases.index('L')] = 1

# # G --> 1 confusión con "X"
# matriz_confusion[clases.index('G'), clases.index('G')] = 199  # 200 - 1
# matriz_confusion[clases.index('G'), clases.index('X')] = 1

# # H --> No tuvo confusión
# matriz_confusion[clases.index('H'), clases.index('H')] = 200

# # I --> 3 confusiones con "J"
# matriz_confusion[clases.index('I'), clases.index('I')] = 197  # 200 - 3
# matriz_confusion[clases.index('I'), clases.index('J')] = 3

# # J --> No tuvo confusión
# matriz_confusion[clases.index('J'), clases.index('J')] = 200

# # K --> No tuvo confusión
# matriz_confusion[clases.index('K'), clases.index('K')] = 200

# # L --> 1 con "F"
# matriz_confusion[clases.index('L'), clases.index('L')] = 199  # 200 - 1
# matriz_confusion[clases.index('L'), clases.index('F')] = 1

# # M --> 1 con "N"
# matriz_confusion[clases.index('M'), clases.index('M')] = 199  # 200 - 1
# matriz_confusion[clases.index('M'), clases.index('N')] = 1

# # N --> 1 con "M"
# matriz_confusion[clases.index('N'), clases.index('N')] = 199  # 200 - 1
# matriz_confusion[clases.index('N'), clases.index('M')] = 1

# # O --> 2 con "Q"
# matriz_confusion[clases.index('O'), clases.index('O')] = 198  # 200 - 2
# matriz_confusion[clases.index('O'), clases.index('Q')] = 2

# # P --> No tuvo confusión
# matriz_confusion[clases.index('P'), clases.index('P')] = 200

# # Q --> 1 con "O"
# matriz_confusion[clases.index('Q'), clases.index('Q')] = 199  # 200 - 1
# matriz_confusion[clases.index('Q'), clases.index('O')] = 1

# # R --> 1 con "S"
# matriz_confusion[clases.index('R'), clases.index('R')] = 199  # 200 - 1
# matriz_confusion[clases.index('R'), clases.index('S')] = 1

# # S --> 2 con "Z"
# matriz_confusion[clases.index('S'), clases.index('S')] = 198  # 200 - 2
# matriz_confusion[clases.index('S'), clases.index('Z')] = 2

# # T --> 1 con "ESPACIO"
# matriz_confusion[clases.index('T'), clases.index('T')] = 199  # 200 - 1
# matriz_confusion[clases.index('T'), clases.index('ESPACIO')] = 1

# # U --> No tuvo confusión
# matriz_confusion[clases.index('U'), clases.index('U')] = 200

# # V --> 2 con "W"
# matriz_confusion[clases.index('V'), clases.index('V')] = 198  # 200 - 2
# matriz_confusion[clases.index('V'), clases.index('W')] = 2

# # W --> 1 con "V"
# matriz_confusion[clases.index('W'), clases.index('W')] = 199  # 200 - 1
# matriz_confusion[clases.index('W'), clases.index('V')] = 1

# # X --> 1 con "G"
# matriz_confusion[clases.index('X'), clases.index('X')] = 199  # 200 - 1
# matriz_confusion[clases.index('X'), clases.index('G')] = 1

# # Y --> No tuvo confusión
# matriz_confusion[clases.index('Y'), clases.index('Y')] = 200

# # Z --> 1 con "S"
# matriz_confusion[clases.index('Z'), clases.index('Z')] = 199  # 200 - 1
# matriz_confusion[clases.index('Z'), clases.index('S')] = 1

# # ESPACIO --> 2 con "T"
# matriz_confusion[clases.index('ESPACIO'), clases.index('ESPACIO')] = 198  # 200 - 2
# matriz_confusion[clases.index('ESPACIO'), clases.index('T')] = 2

# # Visualizar la matriz de confusión
# fig, ax = plt.subplots(figsize=(20, 20))  # Aumenta el tamaño de la figura

# disp = ConfusionMatrixDisplay(confusion_matrix=matriz_confusion, display_labels=clases)
# disp.plot(ax=ax, cmap=plt.cm.Blues, values_format='d')  # Usa formato entero

# # Ajustar el tamaño de la fuente dentro de las celdas
# for text in ax.texts:
#     text.set_size(8)  # Disminuir el tamaño de la fuente dentro de las celdas

# # Ajustar el tamaño de las etiquetas de los ejes y el título
# plt.xticks(rotation=90, ha='right', fontsize=10)  # Ajusta el tamaño de la fuente y rota las etiquetas del eje x
# plt.yticks(rotation=0, fontsize=10)  # Ajusta el tamaño de la fuente de las etiquetas del eje y
# plt.xlabel("Clase Predicha", fontsize=12)
# plt.ylabel("Clase Verdadera", fontsize=12)
# plt.title("Matriz de Confusión", fontsize=14)
# plt.tight_layout()  # Ajusta el espaciado
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# Definir las clases
clases = [chr(i) for i in range(65, 91)] + ["ESPACIO"]  # A-Z + ESPACIO

# Inicializar la matriz de confusión (27x27, ya que hay 27 clases)
matriz_confusion = np.zeros((len(clases), len(clases)), dtype=int)

# Rellenar la matriz de confusión con los errores proporcionados
# Filas representan las clases verdaderas, columnas las clases predichas

# A --> Confusión con la clase "Y"
matriz_confusion[clases.index('A'), clases.index('A')] = 199  # 200 - 1
matriz_confusion[clases.index('A'), clases.index('Y')] = 1

# B --> 1 confusión con la clase "ESPACIO", 1 confusión con la clase "T"
matriz_confusion[clases.index('B'), clases.index('B')] = 198  # 200 - 2
matriz_confusion[clases.index('B'), clases.index('ESPACIO')] = 1
matriz_confusion[clases.index('B'), clases.index('T')] = 1

# C --> 2 confusiones con la clase "O"
matriz_confusion[clases.index('C'), clases.index('C')] = 198  # 200 - 2
matriz_confusion[clases.index('C'), clases.index('O')] = 2

# D --> 1 confusión con la clase "O", 1 con la clase "Q"
matriz_confusion[clases.index('D'), clases.index('D')] = 198  # 200 - 2
matriz_confusion[clases.index('D'), clases.index('O')] = 1
matriz_confusion[clases.index('D'), clases.index('Q')] = 1

# E --> No tuvo ninguna confusión
matriz_confusion[clases.index('E'), clases.index('E')] = 200

# F --> 1 confusión con la clase "L"
matriz_confusion[clases.index('F'), clases.index('F')] = 195  # 200 - 5
matriz_confusion[clases.index('F'), clases.index('L')] = 5

# G --> 1 confusión con "X"
matriz_confusion[clases.index('G'), clases.index('G')] = 190  # 200 - 10
matriz_confusion[clases.index('G'), clases.index('X')] = 10

# H --> No tuvo confusión
matriz_confusion[clases.index('H'), clases.index('H')] = 200

# I --> 3 confusiones con "J"
matriz_confusion[clases.index('I'), clases.index('I')] = 98  # 200 - 102
matriz_confusion[clases.index('I'), clases.index('J')] = 102

# J --> No tuvo confusión
matriz_confusion[clases.index('J'), clases.index('J')] = 200

# K --> No tuvo confusión
matriz_confusion[clases.index('K'), clases.index('K')] = 200

# L --> 1 con "F"
matriz_confusion[clases.index('L'), clases.index('L')] = 199  # 200 - 1
matriz_confusion[clases.index('L'), clases.index('F')] = 1

# M --> 1 con "N"
matriz_confusion[clases.index('M'), clases.index('M')] = 199  # 200 - 1
matriz_confusion[clases.index('M'), clases.index('N')] = 1

# N --> 1 con "M"
matriz_confusion[clases.index('N'), clases.index('N')] = 199  # 200 - 1
matriz_confusion[clases.index('N'), clases.index('M')] = 1

# O --> 2 con "Q"
matriz_confusion[clases.index('O'), clases.index('O')] = 198  # 200 - 2
matriz_confusion[clases.index('O'), clases.index('Q')] = 2

# P --> No tuvo confusión
matriz_confusion[clases.index('P'), clases.index('P')] = 200

# Q --> 1 con "O"
matriz_confusion[clases.index('Q'), clases.index('Q')] = 199  # 200 - 1
matriz_confusion[clases.index('Q'), clases.index('O')] = 1

# R --> 1 con "S"
matriz_confusion[clases.index('R'), clases.index('R')] = 199  # 200 - 1
matriz_confusion[clases.index('R'), clases.index('S')] = 1

# S --> 2 con "Z"
matriz_confusion[clases.index('S'), clases.index('S')] = 198  # 200 - 2
matriz_confusion[clases.index('S'), clases.index('Z')] = 2

# T --> 1 con "ESPACIO"
matriz_confusion[clases.index('T'), clases.index('T')] = 199  # 200 - 1
matriz_confusion[clases.index('T'), clases.index('ESPACIO')] = 1

# U --> No tuvo confusión
matriz_confusion[clases.index('U'), clases.index('U')] = 200

# V --> 2 con "W"
matriz_confusion[clases.index('V'), clases.index('V')] = 198  # 200 - 2
matriz_confusion[clases.index('V'), clases.index('W')] = 2

# W --> 1 con "V"
matriz_confusion[clases.index('W'), clases.index('W')] = 199  # 200 - 1
matriz_confusion[clases.index('W'), clases.index('V')] = 1

# X --> 1 con "G"
matriz_confusion[clases.index('X'), clases.index('X')] = 199  # 200 - 1
matriz_confusion[clases.index('X'), clases.index('G')] = 1

# Y --> No tuvo confusión
matriz_confusion[clases.index('Y'), clases.index('Y')] = 200

# Z --> 1 con "S"
matriz_confusion[clases.index('Z'), clases.index('Z')] = 199  # 200 - 1
matriz_confusion[clases.index('Z'), clases.index('S')] = 1

# ESPACIO --> 2 con "T"
matriz_confusion[clases.index('ESPACIO'), clases.index('ESPACIO')] = 198  # 200 - 2
matriz_confusion[clases.index('ESPACIO'), clases.index('T')] = 2

# Visualizar la matriz de confusión
fig, ax = plt.subplots(figsize=(10, 8))  # Reducir aún más el tamaño de la figura

disp = ConfusionMatrixDisplay(confusion_matrix=matriz_confusion, display_labels=clases)
disp.plot(ax=ax, cmap=plt.cm.Blues, values_format='d')  # Usa formato entero

# Ajustar el tamaño de la fuente dentro de las celdas
for text in ax.texts:
    text.set_size(8)  # Disminuir el tamaño de la fuente dentro de las celdas

# Ajustar el tamaño de las etiquetas de los ejes y el título
plt.xticks(rotation=90, ha='right', fontsize=8)  # Ajusta el tamaño de la fuente y rota las etiquetas del eje x
plt.yticks(rotation=0, fontsize=8)  # Ajusta el tamaño de la fuente de las etiquetas del eje y
plt.xlabel("Clase Predicha", fontsize=10)
plt.ylabel("Clase Verdadera", fontsize=10)
plt.title("Matriz de Confusión", fontsize=12)
plt.tight_layout(pad=3.0)  # Ajustar el espaciado para evitar recortes
plt.show()
