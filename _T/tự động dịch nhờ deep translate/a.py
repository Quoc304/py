from deep_translator import GoogleTranslator
import pyttsx3

engine = pyttsx3.init()
print("====WANT TO EXIT====")
print("==Type Text Exit()==")

while True:
    msg = input("*TRANSLATE BOX: ")
    if msg == 'Exit()':
        break
    else:
        translated = GoogleTranslator(source='auto', target='en').translate(msg)
        print("TRANS: ",translated)
        engine.say(translated)
        engine.runAndWait()
       

