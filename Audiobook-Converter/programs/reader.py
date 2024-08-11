from time import sleep
import pyttsx3
import speech_recognition as sr
from urllib import request
import re

engine = pyttsx3.init('sapi5',True)
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+1)
engine.setProperty('voice',voices[1].id)

def r(text):
    try:
        request.urlopen(f'http://192.168.29.42/{text}')
    except:
        pass

def speak(text):
    #r('/h')
    engine.say(text)
    engine.runAndWait()
    #r('/c')

def takecommand():
    r= sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening...')
            audio = r.listen(source,timeout=3.0)
            print('recognizing.....')
        query = r.recognize_google(audio, language='en')
        print(f'user requested {query}')
    except Exception:
        print('waiting....')
        query='None'
    return query 


def file(joinpath="audio/demo/", headding="", section=""):
    title = re.sub("(\'|:|,|\"|\?)","",headding.text.replace(" ","_"))
    return joinpath+"SECTION_".join(str(section))+"_"+title.replace(' ','_').replace(':',"").replace("?","")+".mp3"

def convert_audio(name,text, sec):
    file_name=file(headding=name, section= sec)
    engine.save_to_file("topic : "+name.text+" . "+text.text, file_name)
    engine.runAndWait()

# convert_audio('test',"Dow ")