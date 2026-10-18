import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import time
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "YOUR_NEW_NEWSDATA_API_KEY"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    # Fixed: passed the variable 'text' instead of string literal 'text'
    tts = gTTS(text=text, lang="en")
    tts.save("temp.mp3")

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the correct temporary MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the music
    pygame.mixer.music.play()

    print("Playing MP3...")

    # Keep playing until the music finishes
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    # Clean up pygame and remove temp file safely
    pygame.mixer.music.unload()
    pygame.mixer.quit()
    print("Music finished!")

    if os.path.exists("temp.mp3"):
        os.remove("temp.mp3")


def aiProcess(command):
    # Best practice: client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    client = client = OpenAI(api_key=["OPENAI_API_KEY"])
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a poetic assistant, skilled in explaining complex"
                    " topics. Give short responses please."
                ),
            },
            {"role": "user", "content": command},
        ],
    )
    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(
            f"https://newsdata.io/api/1/latest?apikey={newsapi}&language=en"
        )
        if r.status_code == 200:
            data = r.json()
            articles = data.get("results", [])  # newsdata.io typically uses 'results'
            for article in articles[:3]:  # Limit to top 3 articles
                speak(article["title"])
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=2)

            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Ya")
                # Listen for Command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))



























            

# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# if __name__ == "__main__":
#     speak("Initializing Jarvis....")
    
#     while True:
#         r = sr.Recognizer()
        
#         # Obtain audio from the microphone
#         with sr.Microphone() as source:
#             print("Listening...")
#             # Optional: Adjust for background noise if necessary
#             # r.adjust_for_ambient_noise(source)
#             audio = r.listen(source)

#         # Recognize speech using Google Speech Recognition
#         try:
#             print("Recognizing...")
#             command = r.recognize_google(audio)
#             print(f"User said: {command}")
            
#             # Example command check
#             if "open google" in command.lower():
#                 speak("Opening Google")
#                 webbrowser.open("https://google.com")
                
#         except sr.UnknownValueError:
#             print("Google Speech Recognition could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")