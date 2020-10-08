import speech_recognition as sr
import os
import gtts
from playsound import playsound
import pywhatkit
import sys
from time import strftime

def audioResponse(audio):
    print(audio)
    output=gtts.gTTS(audio)
    output.save("out.mp3")
    playsound("out.mp3")
    os.remove("out.mp3")
def myCommand():
    "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    except sr.UnknownValueError:
        print('....')
        command = myCommand();
    return command
def assistant(command):
    if 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            audioResponse('Hello chief. Good morning')
        elif 12 <= day_time < 18:
            audioResponse('Hello chief. Good afternoon')
        else:
            audioResponse('Hello chif. Good evening')
    elif 'stop' in command:
        audioResponse('Bye bye chief. Have a nice day')
        sys.exit()
    else:
        audioResponse("sorry there is no other functionality currently added to me")
audioResponse('Hey chief, I am your personal voice assistant, Please give a command ')
while True:
    assistant(myCommand())
