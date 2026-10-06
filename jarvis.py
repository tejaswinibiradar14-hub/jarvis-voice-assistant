import datetime
import os
import subprocess
import sys
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()


def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("There was a problem with the speech recognition service.")
        return ""


def open_application(app_name):
    if os.name == 'nt':
        try:
            os.startfile(app_name)
        except OSError:
            print(f"Could not open: {app_name}")
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', app_name])
    else:
        subprocess.Popen(['xdg-open', app_name])


def handle_command(command):
    if not command:
        return True

    if "hello" in command or "hi" in command:
        speak("Hello sir. I am Jarvis. How can I help you?")
        return True

    if "time" in command:
        current_time = datetime.datetime.now().strftime('%H:%M %p')
        speak(f"The current time is {current_time}")
        return True

    if "date" in command:
        current_date = datetime.datetime.now().strftime('%A, %d %B %Y')
        speak(f"Today is {current_date}")
        return True

    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
        return True

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
        return True

    if "open notepad" in command:
        if os.name == 'nt':
            os.startfile('notepad')
        elif sys.platform == 'darwin':
            subprocess.Popen(['open', '-a', 'TextEdit'])
        else:
            subprocess.Popen(['gedit'])
        speak("Opening Notepad")
        return True

    if "search for" in command:
        query = command.replace("search for", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")
        else:
            speak("What would you like me to search for?")
        return True

    if "who is" in command:
        person = command.replace("who is", "").strip()
        if person:
            try:
                summary = wikipedia.summary(person, sentences=2)
                speak(summary)
            except Exception:
                speak(f"I could not find information about {person}")
        return True

    if "bye" in command or "goodbye" in command or "exit" in command:
        speak("Goodbye sir. Have a nice day.")
        return False

    if "jarvis" in command:
        speak("Yes sir, how can I help you?")
        return True

    speak("I heard you, but I do not have a command for that yet.")
    return True


def main():
    speak("Initializing Jarvis. I am ready.")

    while True:
        command = listen_for_command()

        if not command:
            continue

        if "jarvis" in command:
            speak("Yes sir?")
            command = listen_for_command()
            if not command:
                continue
            if not handle_command(command):
                break
        else:
            if not handle_command(command):
                break


if __name__ == "__main__":
    main()
