import speech_recognition as sr
import pyttsx3

# Inicializar o reconhecedor
recognizer = sr.Recognizer()

# Inicializar o sintetizador de voz
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    global engine
    engine.say(text)
    engine.runAndWait()


# Capturar áudio do microfone
def listen():
    with sr.Microphone(device_index=2) as source:
        print("Diga alguma coisa...")
        speak("Diga alguma coisa...")
        try:
            audio = recognizer.listen(source)
            # Reconhecer usando o Google Speech Recognition
            text = recognizer.recognize_google(audio, language="pt-PT")
            print("Você disse:", text)
            speak(text)
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            speak("Não entendi o que vocé disse.")
            listen()
        except sr.RequestError as e:
            print("Erro ao conectar ao serviço de reconhecimento:", e)

listen()
