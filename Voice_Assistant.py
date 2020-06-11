"""
Created on Mon Aug 26 20:28:01 2019

@author:Rohan Dixit
"""

import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
from pyowm import OWM
import re


engine = pyttsx3.init('sapi5')#sapi5 is id for voice 
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

for i in range(0,2):
   print(voices[i].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    
    else:
        speak("Good Evening!")  
    
    speak("  I   am  Victoria. I am your Virtual assistant. ")       

def takeCommand():
#It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)    
        print("Say that again please...") 
        speak("Say that again please...") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 588)
    server.ehlo()
    server.starttls()
    server.login('MAIL ID', 'PASSWORD')
    server.sendmail('FROM ID', to, content)
    server.close()

if __name__ == "__main__":
    
    wishMe()
while True:
    

    query = takeCommand().lower()

    # Logic for executing tasks based on query
    if 'ok victoria' in query:
        speak("Hello Rohan Sir ! How can i help you")

    elif 'how are you' in query:
        speak("I m Fine ! What about you")
        
    elif 'i am fine' in query:
        speak("ok sir ! How can i help you")
        
    elif "who are you" in query or "define yourself" in query: 
        speak ('''Hello, I am Person. Your personal Assistant. 
        I am here to make your life easier. You can command me to perform 
        various tasks such as calculating sums or opening applications etcetra''')
  
    elif "who made you" in query or "created you" in query: 
        speak("I have been created by Rohan Dixit.")
        
    elif "wiki search" in query:
        speak('please wait i am searching.')
        query = query.replace("wikipedia", query[12:])
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

        
    elif 'open youtube' in query:
        speak("plaese wait Youtube is Opening ")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query:
        speak("plaese wait google is Opening ")
        webbrowser.open("https://www.google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("https://www.stackoverflow.com")   

    elif 'play music' in query:
        speak("OK let me find Suggestion for you")
 #           music_dir = 'D:\\'
#            songs = os.listdir(music_dir)
#           print(songs)    
        os.startfile('D:\\d.mp3')

    elif 'what is the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Rohan Sir, the time is {strTime}")
        
    elif 'what is the date' in query:
        strDate =datetime.date.today() 
        speak(f"Rohan Sir, the Date is {strDate}")
        
    elif 'open notepad plus plus' in query:
        speak("plaese wait Notepad plus plus is Opening ")
        codePath = "C://Program Files//Notepad++//notepad++.exe"
        os.startfile(codePath)
        
    elif 'open calculator' in query:
        speak("plaese wait Calculator is Opening ")
        os.system('start calc.exe')
    elif 'open word' in query:
        speak("Please wait Word is opening")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk")

    elif 'open excel' in query:
        speak("Please wait excel is opening")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007.lnk")

        
    elif 'email to rohan' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "rohandixit67@gmail.com"    
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry Rohan Sir . I am not able to send this email") 
            
    elif 'open whatsapp' in query:
        speak("plaese wait whatsapp is Opening ")
        webbrowser.open("https://web.whatsapp.com")
        
    elif 'open facebook' in query:
        speak("plaese wait facebook is Opening ")
        webbrowser.open("https://www.facebook.com")
        
    elif 'open twitter' in query:
        speak("plaese wait twitter is Opening ")
        webbrowser.open("https://www.twitter.com")
        
    elif 'open linkedin' in query:
        speak("plaese wait linkeden is Opening ")
        webbrowser.open("https://www.linkedin.com")
        
    elif 'wish me' in query:
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   
        else:
            speak("Good Evening!")         
            
    elif 'current weather' in query:
        reg_ex = re.search('current weather in (.*)', query)
        if reg_ex:
             city = reg_ex.group(1)
             owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
             obs = owm.weather_at_place(city)
             w = obs.get_weather()
             k = w.get_status()
             x = w.get_temperature(unit='celsius')
             speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
             print('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))

            
                
    elif 'exit' in query:
        speak('Bye bye Sir. Have a nice day')
        break
