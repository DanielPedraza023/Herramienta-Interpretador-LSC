import matplotlib.pyplot as plt

# Datos simulados de precisión por señal
señales = ['A', 'B', 'D', 'E', 'F', 'J', 'K', 'L', 'M', 'O', 'R', 'U', 'V','Y','Z','ESPACIO']
precisiones = [0.92, 0.80, 0.95, 0.90, 0.92, 0.87, 0.94, 0.93, 0.91, 0.85, 0.75, 0.78, 0.90, 0.95, 0.85, 0.88 ]
colors = [
    "#FFB3BA",  # Rosa claro
    "#FFDFBA",  # Naranja claro
    "#FFFFBA",  # Amarillo claro
    "#BAFFB3",  # Verde claro
    "#BAE1FF",  # Azul claro
    "#FFBAF0",  # Rosa pastel
    "#FFABAB",  # Rojo claro
    "#FFC3A0",  # Melocotón
    "#D5AAFF",  # Lavanda
    "#A0E7E5",  # Verde agua
    "#FF677D",  # Coral
    "#D4A5A5",  # Marrón claro
    "#392F5A",  # Morado suave
    "#FFB74D",  # Amarillo pastel (nuevo)
    "#81D4FA",  # Azul celeste pastel (nuevo)
    "#B39DDB"   # Lavanda pastel (nuevo)
]

# Gráfico de barras de precisión
plt.figure(figsize=(12, 6))
plt.bar(señales, precisiones, color= colors)
plt.xlabel('Señal')
plt.ylabel('Precisión')
plt.title('Precisión de Detección por Señal')
plt.ylim([0, 1])
#plt.grid()
plt.show()
