

import pyttsx3

engine = pyttsx3.init("sapi5")

print("Available voices:")
for voice in engine.getProperty("voices"):
    print(voice.id)

engine.setProperty("volume", 1.0)
engine.setProperty("rate", 150)

print("Starting voice test...")
engine.say("Hello, I am Jarvis. Can you hear me?")
engine.runAndWait()
print("Voice test completed.")
