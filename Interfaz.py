import cv2
import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk
from ultralytics import YOLO
from TextToAudio import reproducir_audio
import main
import time

# Lectura de la camara
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Lectura de nuestro modelo entrenado
model = YOLO("lsc.pt")

# Llamar funcion de detección de manos
detector = main.detectorManos(Confdeteccion=0.9)

# Lista que guarda las señales reconocidas
señales_reconocidas = []
ultima_señal = None
ultima_deteteccion_tiempo = 0
tiempo_espera = 1.0

# Variable para mostrar la palabra en construcción
palabra_actual = ''

# Configuración de la fuente y el color del texto
fuente = cv2.FONT_HERSHEY_COMPLEX
color_texto = (0, 0, 255)
tamaño_fuente = 2
grosor_texto = 3

# Configuración de Tkinter
root = tk.Tk()
root.title("Reconocedor de Señas")
root.geometry("1600x800")

# Crear marco para mostrar la imagen completa
frame_completo = Frame(root)
frame_completo.pack(side="left", padx=10, pady=10)

# Crear marco para mostrar la imagen recortada
frame_recortado = Frame(root)
frame_recortado.pack(side="right", padx=10, pady=10)

# Etiqueta para mostrar la palabra en construcción
label_palabra = Label(frame_completo, text="", font=("Helvetica", 24), fg="red")
label_palabra.pack()

# Etiqueta para mostrar el video completo
label_video_completo = Label(frame_completo)
label_video_completo.pack()

# Etiqueta para mostrar el video recortado
label_video_recortado = Label(frame_recortado)
label_video_recortado.pack()

def mostrar_video():
    global ultima_señal, ultima_deteteccion_tiempo, palabra_actual

    ret, frame = cap.read()
    if not ret:
        return

    frame = detector.encontrarManos(frame, dibujar=False)
    lista1, bbox, mano = detector.encontrarPosicion(frame, ManoNum=0, dibujarPuntos=False, dibujarBox=False, color=[255, 0, 0])
    
    recorte = None
    if mano == 1:
        xmin, ymin, xmax, ymax = bbox
        xmin = max(0, xmin - 60)
        ymin = max(0, ymin - 50)
        xmax += 55
        ymax += 70

        recorte = frame[ymin:ymax, xmin:xmax]
        recorte = cv2.resize(recorte, (640, 640), interpolation=cv2.INTER_CUBIC)
        resultados = model.predict(recorte, conf=0.65)

        if len(resultados) > 0 and len(resultados[0].boxes) > 0:
            señal_en_imagen = None

            for result in resultados:
                for box in result.boxes:
                    clase_id = int(box.cls)
                    clase = result.names[clase_id]
                    señal_en_imagen = clase

            if señal_en_imagen and (señal_en_imagen != ultima_señal or (time.time() - ultima_deteteccion_tiempo) > tiempo_espera):
                señales_reconocidas.append(señal_en_imagen)
                palabra_actual += señal_en_imagen
                ultima_señal = señal_en_imagen
                ultima_deteteccion_tiempo = time.time()
                print(señales_reconocidas)

        anotaciones = resultados[0].plot() if len(resultados) > 0 else frame
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), [0, 255, 0], 2)

    if mano > 1:
        cv2.putText(frame, "Se detecta mas de una mano", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.putText(frame, "Palabra: " + palabra_actual, (50, 100), fuente, tamaño_fuente, color_texto, grosor_texto, cv2.LINE_AA)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_completo = Image.fromarray(frame_rgb)
    imgtk_completo = ImageTk.PhotoImage(image=img_completo)
    label_video_completo.imgtk = imgtk_completo
    label_video_completo.configure(image=imgtk_completo)
    label_palabra.config(text="Palabra: " + palabra_actual)
    
    if recorte is not None:
        recorte_rgb = cv2.cvtColor(recorte, cv2.COLOR_BGR2RGB)
        img_recortado = Image.fromarray(recorte_rgb)
        imgtk_recortado = ImageTk.PhotoImage(image=img_recortado)
        label_video_recortado.imgtk = imgtk_recortado
        label_video_recortado.configure(image=imgtk_recortado)

    label_video_completo.after(10, mostrar_video)

def procesar_enter(event):
    global palabra_actual, señales_reconocidas, ultima_señal, ultima_deteteccion_tiempo

    if not señales_reconocidas:
        print("No se ha detectado ninguna señal")
        reproducir_audio("No se ha detectado ninguna señal")
    else:
        palabras = []
        palabra_actual = ''
        for señal in señales_reconocidas:
            if señal == 'ESPACIO':
                palabras.append(palabra_actual)
                palabra_actual = ''
            else:
                palabra_actual += señal
        palabras.append(palabra_actual)
        palabra_completa = ' '.join(palabras)

        print("Palabra completa formada por las señales reconocidas:", palabra_completa)
        reproducir_audio(palabra_completa)

    señales_reconocidas = []
    palabra_actual = ''
    ultima_señal = None
    ultima_deteteccion_tiempo = 0

root.bind('<Return>', procesar_enter)
mostrar_video()
root.mainloop()

cap.release()
cv2.destroyAllWindows()
