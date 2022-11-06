import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    # elif 'open google' in command:
    #         webbrowser.open("google.com")
    #
    #
    # elif 'open facebook' in command:
    #         webbrowser.open("facebook.com")
    #
    #
    # elif 'open instagram' in command:
    #         webbrowser.open("instagram.com")
    #
    # elif 'open gmail' in command:
    #         webbrowser.open("gmail.com")
    #
    # elif 'open stack overflow' in command:
    #         webbrowser.open("stackoverflow.com")
    elif 'exit' in command or 'stop' in command:
        return False
    else:
        talk('Please say the command again.')



while True:
    a=run_alexa()
    print(a)
    if a==False:
        break
