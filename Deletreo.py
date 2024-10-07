import cv2
from ultralytics import YOLO
from TextToAudio import reproducir_audio
import main
import time

# Lectura de la camara
cap = cv2.VideoCapture(1)
# Cambiar la resolucion de la captura
cap.set(3, 1280)
cap.set(4, 720)

# Lectura de nuestro modelo entrenado
model = YOLO("lsc.pt")  # Colocar nombre del modelo resultante

# Llamar funcion de detección de manos
detector = main.detectorManos(Confdeteccion=0.9)

# Lista que guarda las señales reconocidas
señales_reconocidas = []
ultima_señal = None
ultima_deteteccion_tiempo = 0
tiempo_espera = 3.0  # Tiempo en segundos para permitir la misma señal nuevamente

# Variable para mostrar la palabra en construcción
palabra_actual = ''

# Configuración de la fuente y el color del texto
fuente = cv2.FONT_HERSHEY_COMPLEX
color_texto = (0, 0, 0)  # Negro en formato BGR
tamaño_fuente = 2
grosor_texto = 3

while True:
    # Realizar lectura de Video
    ret, frame = cap.read()

    # Extraer informacion de la mano
    frame = detector.encontrarManos(frame, dibujar=False)

    # Posicion de una sola mano
    lista1, bbox, mano = detector.encontrarPosicion(frame, ManoNum=0, dibujarPuntos=False, dibujarBox=False, color=[255, 0, 0])
    
    # Si detecta una mano
    if mano == 1:
        # Extraer informacion del cuadro que encierra la mano
        xmin, ymin, xmax, ymax = bbox

        # Modificamos las dimensiones del cuadro
        xmin = xmin - 60
        ymin = ymin - 50
        xmax = xmax + 55
        ymax = ymax + 70

        if xmin < 0 or ymin < 0:
            xmin = 0
            ymin = 0

        # Recorte del recuadro solo con la mano
        recorte = frame[ymin:ymax, xmin:xmax]

        # Redimensionar
        recorte = cv2.resize(recorte, (640, 640), interpolation=cv2.INTER_CUBIC)

        # Extraer resultados del modelo
        resultados = model.predict(recorte, conf=0.65)  # Se crea una variable la cual almacena los resultados de las predicciones del modelo

        # Comprobar si existen resultados
        if len(resultados) > 0 and len(resultados[0].boxes) > 0:
            # Señales en la imagen
            señal_en_imagen = None

            # Iteramos en cada resultado
            for result in resultados:
                for box in result.boxes:
                    clase_id = int(box.cls)
                    clase = result.names[clase_id]

                    # Asignar la clase de la señal a la variable señal_en_imagen
                    señal_en_imagen = clase

            # Solo agregar la señal si ha pasado suficiente tiempo desde la última detección o si es diferente
            if señal_en_imagen and (señal_en_imagen != ultima_señal or (time.time() - ultima_deteteccion_tiempo) > tiempo_espera):
                if señal_en_imagen == "ESPACIO":
                    señales_reconocidas.append(" ")
                    palabra_actual += " "
                else:
                    señales_reconocidas.append(señal_en_imagen)
                    palabra_actual += señal_en_imagen

                ultima_señal = señal_en_imagen
                ultima_deteteccion_tiempo = time.time()
                print(señales_reconocidas)

        # Mostrar las anotaciones en la imagen
        anotaciones = resultados[0].plot() if len(resultados) > 0 else frame
        cv2.imshow("INTERPRETADOR", anotaciones)
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), [0, 255, 0], 2)  # Recuadro Verde

    if mano > 1:
        cv2.putText(frame, "Se detecta mas de una mano", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Mostrar la palabra en construcción en la ventana
    cv2.putText(frame, "Palabra: " + palabra_actual, (50, 100), fuente, tamaño_fuente, color_texto, grosor_texto, cv2.LINE_AA)

    # Mostrar FPS
    cv2.imshow("LSC", frame)

    # Leer el teclado
    t = cv2.waitKey(1)

    if t == 27: #Tecla escape
        break
    
    elif t == 13: #Tecla enter
        if not señales_reconocidas:
            print("No se ha detectado ninguna señal")
            reproducir_audio("No se ha detectado ninguna señal")
        
        else:
            # Convertir cada lista de señales en una cadena
            palabras = []
            
            palabra_actual = ''
            for señal in señales_reconocidas:
                if señal == " ":
                    palabras.append(palabra_actual)
                    palabra_actual = ''  # Reiniciar palabra actual después de un espacio
                else:
                    palabra_actual += señal
            palabras.append(palabra_actual)  # Agregar la última palabra

            # Unir todas las palabras en una sola cadena
            palabra_completa = ' '.join(palabras)

            print("Palabra completa formada por las señales reconocidas:", palabra_completa)
            reproducir_audio(palabra_completa)

        señales_reconocidas = []
        palabra_actual = ''
        ultima_señal = None
        ultima_deteteccion_tiempo = 0
    
    elif t == 8:  # Tecla de borrar (retroceso)
        if señales_reconocidas:
            señales_reconocidas.pop()  # Eliminar la última señal
            palabra_actual = palabra_actual[:-1]  # Eliminar la última letra de la palabra en construcción
            print("Última letra eliminada. Palabra actual:", palabra_actual)
    
    elif t== 32: #Tecla espacio
        señales_reconocidas = []
        palabra_actual = ''
        ultima_señal = None
        ultima_deteteccion_tiempo = 0

cap.release()
cv2.destroyAllWindows()
#A B D E F J K L M O R U V Y Z ESPACIO	