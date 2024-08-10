# Angle One Site Reader 🌟

## What is Angle One? 📈

Angel One is a leading Indian brokerage platform that provides a wide array of services for retail investors and traders. Trusted by over 20 million clients, it offers a user-friendly interface for trading stocks, mutual funds, and other financial instruments. The platform is designed to cater to both novice and experienced traders, featuring advanced tools, real-time data, and educational resources to empower users in their investment journey.

As I am a lousy reader, I created this bot to convert long, exhausting paragraphs from the Angle One site into audiobooks. This way, I never miss out on learning my trading concepts and can enjoy listening to them with a cup of tea ☕️.

## Steps Involved in the Code Workflow 🛠️

### Step 1: Importing Libraries 📚

The first step involves importing all the necessary libraries and the rendering function that I created.

```python
from time import sleep
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from reader import convert_audio
```

### Step 2: Setting Up Chrome Driver 🚀

Next, we prepare the Chrome driver to load and process the page using Selenium.

```python
url = "https://www.angelone.in/smart-money/trading-courses/technical-trading-indicators"
path = r"C:\Users\ayush\Desktop\chromedriver.exe"
sev = webdriver.ChromeService(executable_path=path)
b = webdriver.Chrome(service=sev, options=webdriver.ChromeOptions())
sections_len = 0
lesson_len = 0
sections = [1, 2, 3]
lessons = [1, 2, 3]
b.get(url)
```

### Step 3: Automating Site Rendering 🤖

This step automates the site rendering by using the XPath of the lessons' start button and reloading the web page to gather data.

```python
j = 2
itr = 0
while(j - 1 > itr):
    itr += 1
    b.get(url)
    sleep(5)
    x = b.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/section/div/div/div/div[1]/section/div/ol/li/p/a')
    try:
        m = b.find_elements(By.XPATH, "//*[@id='wzrk-cancel']")
        m[-1].click()
    except:
        print("already clicked")
    sections = b.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[2]/div/section/div/div/div/div/h2/button/div[1]/p[1]/a')
    sections_len = len(sections)
    sleep(3)
    sections[i].click()
    
    lessons = b.find_elements(By.PARTIAL_LINK_TEXT, "Start")
    j = max(len(lessons), j)
    lessons[itr].click()
    sleep(5)
    x1 = b.find_element(By.XPATH, '//html/body/div[1]/main/div/div/main/section/div[2]/div[2]/div[1]/div[1]/h1')
    x2 = b.find_element(By.XPATH, '//html/body/div[1]/main/div/div/main/section/div[2]/div[2]/div[3]/div[2]/div')
    convert_audio(x1, x2, 4)
```

### Step 4: Converting Text to Audio 🎧

In this step, after obtaining the data in the `convert_audio` function, we pass the heading element, the text to be read, and the index of the chosen lesson. The function handles proper reading of the text, eliminates unnecessary symbols, and generates a unique audio file name to avoid overwriting old files.

```python
# Code saved in reader.py file
from time import sleep
import pyttsx3
import speech_recognition as sr
from urllib import request
import re

engine = pyttsx3.init('sapi5', True)
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
engine.setProperty('volume', volume - 0.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 1)
engine.setProperty('voice', voices[1].id)

def r(text):
    try:
        request.urlopen(f'http://192.168.29.42/{text}')
    except:
        pass

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening...')
            audio = r.listen(source, timeout=3.0)
            print('recognizing.....')
        query = r.recognize_google(audio, language='en')
        print(f'user requested {query}')
    except Exception:
        print('waiting....')
        query = 'None'
    return query 

def file(joinpath="audio/trading/", heading="", section=""):
    title = re.sub("(\'|:|,|\"|\?)", "", heading.text.replace(" ", "_"))
    return joinpath + "SECTION_".join(str(section)) + "_" + title.replace(' ', '_').replace(':', "").replace("?", "") + ".mp3"

def convert_audio(name, text, sec):
    file_name = file(heading=name, section=sec)
    engine.save_to_file(text.text, file_name)
    engine.runAndWait()
```

## Conclusion 🎉

This project allows you to effortlessly convert educational content from the Angle One platform into audio format, enhancing your learning experience. Enjoy your trading journey while sipping your favorite tea! ☕️

