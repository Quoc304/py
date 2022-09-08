from gtts import gTTS
import os
import wikipedia
if __name__ == '__main__':
    cin = input("Nhập wiki cần tìm: ")
    wikipedia.set_lang("vi")
    m = wikipedia.summary(cin)
    print(m)
    tts = gTTS(m, lang = 'vi')
    tts.save("{cin}.mp3")
