import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
import random

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Function to recognize speech and return text
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't request results. Check your internet connection.")
        return ""

# Function to generate a response and speak it using mpg321
def respond(response_text):
    print("Assistant:", response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

# Main loop
while True:
    user_input = recognize_speech().lower()

    if "hello" in user_input:
        respond("Hello! How can I assist you today?")
    elif "open website" in user_input:
        webbrowser.open("https://monkeytype.com/")
    elif "tell a joke" in user_input:
        jokes = ["Why don't scientists trust atoms? Because they make up everything!",
                 "Parallel lines have so much in common. It's a shame they'll never meet.",
                 "Why did the scarecrow win an award? Because he was outstanding in his field!"]
        respond(random.choice(jokes))
    elif "exit" in user_input:
        respond("Goodbye!")
        break
    else:
        respond("I'm not sure how to respond to that. Please ask another question.")
