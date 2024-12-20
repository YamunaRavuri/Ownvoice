import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Function to set voice
def set_voice(voice_preference="female"):
    voices = engine.getProperty('voices')
    if voice_preference.lower() == "female":
        for voice in voices:
            if "female" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
    elif voice_preference.lower() == "male":
        for voice in voices:
            if "male" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
    else:
        # Default to first voice if no preference matches
        engine.setProperty('voice', voices[0].id)

# Set voice preference
set_voice("female")  # Change to "female" if preferred

# Function for the engine to speak
def engine_talk(text):
    print(f"Virat is saying: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to listen to user commands
def user_commands():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'virat' in command:
                command = command.replace('virat', '')
                print(f"User said: {command}")
                return command
    except Exception as e:
        print(f"Error: {e}")
        return ""

# Function to process commands
def run_virat():
    command = user_commands()
    if command:
        if 'play' in command:
            song = command.replace('play', '')
            engine_talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            engine_talk('The current time is ' + time)
        elif 'who is' in command:
            name = command.replace('who is', '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)
        elif 'joke' in command:
            engine_talk(pyjokes.get_joke())
        elif 'stop' in command:
            sys.exit()
        else:
            engine_talk('I could not hear you properly')
    else:
        engine_talk('I did not catch that. Please speak again.')

# Main loop
while True:
    run_virat()
