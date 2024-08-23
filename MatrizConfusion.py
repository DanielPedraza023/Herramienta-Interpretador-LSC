# import cv2
# from ultralytics import YOLO
# from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# import matplotlib.pyplot as plt
# import main 

# # Inicializar listas para almacenar las etiquetas verdaderas y predichas
# y_true = []
# y_pred = []

# # Crear el mapeo de las 27 clases
# clases = [chr(i) for i in range(65, 91)] + ["ESPACIO"]  # A-Z + ESPACIO
# index_clase = 0  # Iniciar con la primera clase

# # Etiqueta verdadera inicial
# etiqueta_verdadera = clases[index_clase]

# # Configuración de la captura de video
# cap = cv2.VideoCapture(1)
# cap.set(3, 1280)
# cap.set(4, 720)

# # Cargar el modelo entrenado
# model = YOLO("lsc.pt")

# while True:
#     ret, frame = cap.read()
#     # Aquí asumimos que tienes la función 'detectorManos' y otros componentes definidos
#     # Si no, deberás adaptar este fragmento según tu código de detección de manos
#     detector = main.detectorManos(Confdeteccion=0.9)
#     frame = detector.encontrarManos(frame, dibujar=False)
#     lista1, bbox, mano = detector.encontrarPosicion(frame, ManoNum=0, dibujarPuntos=False, dibujarBox=False)

#     if mano == 1:
#         xmin, ymin, xmax, ymax = bbox
#         recorte = frame[ymin:ymax, xmin:xmax]
#         recorte = cv2.resize(recorte, (640, 640), interpolation=cv2.INTER_CUBIC)

#         resultados = model.predict(recorte, conf=0.65)
        
#         if len(resultados) > 0 and len(resultados[0].boxes) > 0:
#             for result in resultados:
#                 for box in result.boxes:
#                     clase_id = int(box.cls)
#                     etiqueta_predicha = result.names[clase_id]

#                     # Almacenar las etiquetas
#                     y_true.append(etiqueta_verdadera)
#                     y_pred.append(etiqueta_predicha)
#                     print(f"Etiqueta Verdadera: {etiqueta_verdadera}, Etiqueta Predicha: {etiqueta_predicha}")

#     # Mostrar la imagen
#     cv2.imshow("LSC", frame)

#     # Leer el teclado
#     t = cv2.waitKey(1)

#     if t == 27:  # Salir con 'ESC'
#         break
#     elif t == ord('n'):  # Cambiar a la siguiente clase con la tecla 'n'
#         index_clase = (index_clase + 1) % len(clases)
#         etiqueta_verdadera = clases[index_clase]
#         print(f"Cambiando a la siguiente clase: {etiqueta_verdadera}")

# # Liberar los recursos
# cap.release()
# cv2.destroyAllWindows()

# # Crear y mostrar la matriz de confusión
# matriz_confusion = confusion_matrix(y_true, y_pred, labels=clases)
# disp = ConfusionMatrixDisplay(confusion_matrix=matriz_confusion, display_labels=clases)
# disp.plot(cmap=plt.cm.Blues, values_format='.2f')
# plt.xlabel("Clase Predicha")
# plt.ylabel("Clase Verdadera")
# plt.title("Matriz de Confusión")
# plt.show()

import cv2
from ultralytics import YOLO
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import main

# Inicializar listas para almacenar las etiquetas verdaderas y predichas
y_true = []
y_pred = []

# Crear el mapeo de las 27 clases
clases = [chr(i) for i in range(65, 91)] + ["ESPACIO"]  # A-Z + ESPACIO
index_clase = 0  # Iniciar con la primera clase

# Etiqueta verdadera inicial
etiqueta_verdadera = clases[index_clase]

# Configuración de la captura de video
cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

# Cargar el modelo entrenado
model = YOLO("lsc.pt")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: No se pudo capturar el frame. Verifica la cámara.")
        break

    if frame is None or frame.size == 0:
        print("Error: El frame está vacío.")
        continue
    
    # Aquí asumimos que tienes la función 'detectorManos' y otros componentes definidos
    # Si no, deberás adaptar este fragmento según tu código de detección de manos
    detector = main.detectorManos(Confdeteccion=0.9)
    
    try:
        frame = detector.encontrarManos(frame, dibujar=False)
        lista1, bbox, mano = detector.encontrarPosicion(frame, ManoNum=0, dibujarPuntos=False, dibujarBox=False)

        if mano == 1:
            xmin, ymin, xmax, ymax = bbox
            recorte = frame[ymin:ymax, xmin:xmax]
            if recorte.size == 0:
                print("Error: El recorte está vacío.")
                continue
            recorte = cv2.resize(recorte, (640, 640), interpolation=cv2.INTER_CUBIC)

            resultados = model.predict(recorte, conf=0.65)
            
            if len(resultados) > 0 and len(resultados[0].boxes) > 0:
                for result in resultados:
                    for box in result.boxes:
                        clase_id = int(box.cls)
                        etiqueta_predicha = result.names[clase_id]

                        # Almacenar las etiquetas
                        y_true.append(etiqueta_verdadera)
                        y_pred.append(etiqueta_predicha)
                        print(f"Etiqueta Verdadera: {etiqueta_verdadera}, Etiqueta Predicha: {etiqueta_predicha}")

    except Exception as e:
        print(f"Error en el procesamiento del frame: {e}")

    # Mostrar la imagen
    cv2.imshow("LSC", frame)

    # Leer el teclado
    t = cv2.waitKey(1)

    if t == 27:  # Salir con 'ESC'
        break
    elif t == ord('n'):  # Cambiar a la siguiente clase con la tecla 'n'
        index_clase = (index_clase + 1) % len(clases)
        etiqueta_verdadera = clases[index_clase]
        print(f"Cambiando a la siguiente clase: {etiqueta_verdadera}")

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()

# Crear y mostrar la matriz de confusión
matriz_confusion = confusion_matrix(y_true, y_pred, labels=clases)
disp = ConfusionMatrixDisplay(confusion_matrix=matriz_confusion, display_labels=clases)

# Ajustes para mejorar la visualización
plt.figure(figsize=(14, 14))  # Aumenta el tamaño de la figura
disp.plot(cmap=plt.cm.Blues, values_format='d')  # 'd' para enteros

# Ajusta las etiquetas y el espaciado
plt.xticks(rotation=90, ha='right', fontsize=10)  # Ajusta el tamaño de la fuente y rota las etiquetas del eje x
plt.yticks(rotation=0, fontsize=10)  # Ajusta el tamaño de la fuente de las etiquetas del eje y
plt.xlabel("Clase Predicha", fontsize=12)
plt.ylabel("Clase Verdadera", fontsize=12)
plt.title("Matriz de Confusión", fontsize=14)
plt.tight_layout()  # Ajusta el espaciado
plt.show()
