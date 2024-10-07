import pyttsx3

def reproducir_audio(palabra):
    engine = pyttsx3.init()
    
    # Configurar la velocidad (la velocidad predeterminada es alrededor de 200 WPM)
    rate = engine.getProperty('rate')  # Obtener la velocidad actual
    engine.setProperty('rate', rate - 40)  # Reducir la velocidad en 50 WPM (ajusta según prefieras)
    
    
    engine.say(palabra)
    engine.runAndWait()




#detector = "HOLA"
#reproducir_audio("La palabra deletreada fue: ", palabra)
