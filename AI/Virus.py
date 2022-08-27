import pyttsx3
import datetime
import webbrowser as wb

#Dedicate for (Amadeus) Wolfgang Mozart (1980).

#Variable
Introduction = "I'm Amadeus Wolfgang Mozart"

Amadeus = pyttsx3.init()

quote1 = "As a musican and famous composer timeless , Time is very important to me"

voice = Amadeus.getProperty('voices')
Amadeus.setProperty('voice' ,voice[0].id)

def speakAmadeus(audio):
    print("Amadeus: " + audio)
    Amadeus.say(audio)
    Amadeus.runAndWait()

def IntroductionSelf():
    speakAmadeus(Introduction)

def timeAmadeus():
   Time = datetime.datetime.now().strftime("%I:%M %p")
   speakAmadeus(Time)

def Welcome():
    IntroductionSelf()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speakAmadeus("Good Morning! Want some coffe and listen to my music ?")
    elif hour >= 12 and hour < 18:
        speakAmadeus("Good Afternoon! It is sunny outside, I need get some sleep or write some beautiful piece")
    else:
        speakAmadeus("Good Night!")

def Command():
    speakAmadeus("Type your command, please.")
    question = str(input('Your command is: '))
    return question

if __name__ == "__main__":
    Welcome()
    while True:
        question = Command()
        if "google" or "Google" in question:
            speakAmadeus("What is your order?")
            search = Command()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speakAmadeus(f'Here is your order ({search}) on Google.')
            print("\n")
        elif "youtube" or "Youtube" in question:
            speakAmadeus("What is your order?")
            search = Command()
            url = f"https://www.youtube.com/results?search_query={search}"
            wb.get().open(url)
            speakAmadeus(f'Here is your order ({search}) on Youtube.')
        elif "exit" or "Exit" or "quit" or "Quit" or "Leave" or "leave" in question:
            speakAmadeus("Goodbye! See ya.")
            break
        else:
            speakAmadeus("Try Again.")


