import pyttsx3
import speech_recognition
import requests
import datetime
from bs4 import BeautifulSoup

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("understanding.......")
        query = r.recognize_google(audio,language= 'en-in')
        print(f"you said : {query}\n")
    except Exception as e:
        print(f"say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if "listen" in query:
            from Greetme import greetme
            greetme()

            while True:
                query = takecommand().lower()
                if "go to sleep" in query:
                    speak("ok sir, you can call me any time")
                    break
                elif "hello" in query:
                    speak("hello Sir, How are you ?")
                elif "i am fine" in query:
                    speak("that's great Sir")
                elif "how are you" in query:
                    speak("Perfect Sir")
                elif "thank you" in query:
                    speak("you are welcome Sir") 
                
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                
                # elif "temperature" in query:
                #     search = "temperature in gujrat"
                #     url = f"https://www.google.com/search?q={search}"
                #     r = requests.get(url)

                elif "the time" in query:
                    time = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir,the time is {time}")
                
                elif "finally sleep" in query:
                    speak("Ok Sir, Going to sleep")
                    exit()

                