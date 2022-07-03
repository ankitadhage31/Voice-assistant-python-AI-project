import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #microsoft API for voices
engine.setProperty('voice', voices[1].id) #1 for girls voice


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

    speak("I am Tina. Please tell me how may I help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() 
    server.starttls()
    server.login('sender email id', 'sender password') #  enter your email and password here from which email has to be sent
    server.sendmail('reciever email id', to, content) #enter email id where u want to send the email to
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Home Data\\Ankita\\Ankita\\mobi2016\\UCDownloads\\' #put music file path from ur own computer
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Ankita, the time is {strTime}")

        elif 'open photoshop' in query:
            codePath = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe" #put path for the app here
            os.startfile(codePath)

        elif 'email' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand()
                to = "reciever email id here" #reciver email id here    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Ankita. I am not able to send this email")
        elif "end this program" in query:
            break
