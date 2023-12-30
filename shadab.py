import pyttsx3  #pip install pyttsx3
import time
import datetime
import speech_recognition as sr  #pip install SpeechRecognition
import webbrowser
import os
import smtplib  #mail
import wikipedia
from gtts import gTTS
import random 
import cv2   #camera
import pyautogui  #for volume
import ctypes  #lock screen
import subprocess
from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from frontend import Ui_MainWindow


engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning! Sir")
        speak("Good Morning! Sir")         
    elif hour>=12 and hour<18:
        print("Good afternoon Sir")
        speak("Good afternoon Sir")       
    else:
        print("Good evening Sir")
        speak("Good evening Sir")
        
    print("I am SHADAB - The AI voice Assistant of Sahil and Satyendra. Please tell me how may I help you ?")
    speak("I am SHADAB - The AI voice Assistant of Sahil and Satyendra. Please tell me how may I help you ?")  


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()
        speak("please say wakeup to continue")
        while True:
            self.query = self.takecommand()
            if "wake up"in self.query or "are you there" in self.query or "hello" in self.query:
                self.TaskExecution()
    
    def takecommand(self):
        #it takes microphone input from the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening the query asked...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing the query asked...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")  
        except Exception as e:
            # print("Say that again please...")
            return "None"   
        return self.query

    def TaskExecution(self):
        clear = lambda: os.system('cls')
        clear()
        wishMe()
        while True:
         
            self.query = self.takecommand().lower()
    
            # Logic for executing  tasks based on self.query
            # All the commands said by user will be 
    
            if  (('quit' in self.query) or ('exit' in self.query) or ('leave' in self.query) or ('keep quite' in self.query) or ('Good night' in self.query)):
                if 'good night' in self.query:
                    hour =int(datetime.datetime.now().hour)
                    if ((hour>=21 and hour<24) or (hour>=0 and hour<=1)):
                        speak("ok sir , Good night ... I am always with you sir , bye , Take care..")
                    else:
                        speak("No sir.. Dont make me a Fool...  ")
                else:
                    speak("ok sir.. i hope , i did well, bye sir, Take care.. ")

            #code for the greeting messages 
            elif(('good morning' in self.query) or ('good afternoon' in self.query) or ('good evening' in self.query)):
    
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<12:
                    print("Good Morning! Sir")
                    speak("Good Morning Sir! how are you?")         
                elif hour>=12 and hour<18:
                    print("Good afternoon Sir")
                    speak("Good afternoon Sir! how are you?")       
                else:
                    print("Good evening Sir")
                    speak("Good evening Sir! how are you ?")
    
            #code for to say hello to your assistant
            elif 'hello' in self.query:
                print("Hello Sir , what can i do for you")
                speak("Hello Sir , what can i do for you")
            
            #code for knowing who is this AI
            elif 'name' in self.query:
                print("I am an A.I. based voice model and my short name is SHADAB and my full name is “Systematic and Helpful Artificially Developed Autonomous Brain ")
                speak("I am A.I. based voice model and my short name is SHADAB and my full name is “Systematic and Helpful Artificially Developed Autonomous Brain ")

            #code for to check the time
            elif(('the time' in self.query) or ('time' in self.query)):
                strTime = datetime.datetime.now().strftime("%H:%M:%S")  
                print(f"the time is {strTime}")
                speak(f"the time is {strTime}")
    
            #code for to check the date
            elif(('the date' in self.query) or ('date'in self.query)):
                strTime = datetime.datetime.now().strftime("%m/%d/%Y")  
                print(f"Sir the date is {strTime}")
                speak(f"Sir, the date is {strTime}")
    
            #code for opening the youtube
            elif 'open youtube' in self.query:
                print("opening Youtube")
                speak("ok sir, what should I search on Youtube")
                cm = self.takecommand().lower()
                webbrowser.open(f"https://www.youtube.com/search?q={cm}")
    
            #code for opening the google 
            elif 'open google' in self.query:
                speak("ok sir, what should I search on google.")
                cm = self.takecommand().lower()
                webbrowser.open(f"https://www.google.com/search?q={cm}")
     
            #code for closing chrome
            elif 'close chrome' in self.query:
                speak('ok sir closing chrome...')
                os.system('taskkill /F /IM chrome.exe')

            #code for opening stackoverflow
            elif(('open stackoverflow' in self.query) or ('flow' in self.query)):
                speak("Here you go to Stack Over flow. Happy coding")
                webbrowser.open("http://Stackoverflow.com")
            
            #code for opening whatsapp    
            elif 'open whatsapp' in self.query:
                webbrowser.open("https://web.whatsapp.com")
    
            #code for opening the college website
            elif (('open bist' in self.query) or ('university' in self.query)):
                speak('opening B.I.S.T website sir ')
                webbrowser.open("https://bgibhopal.com/bist/")        
    
            #code for opening vscode
            elif 'open vs code' in self.query:
                codePath = "C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code"
                os.startfile(codePath)
            
            #code for opening cmd
            elif 'command prompt' in self.query or 'open cmd' in self.query:
                speak('opening, command prompt')
                os.system("start cmd")
    
            #code for opening camera
            elif(('open camera' in self.query) or ('camera' in self.query)):
                speak("ok sir opening the camera")
                cap = cv2.VideoCapture(0)
                while True:     
                    ret, img = cap.read()                
                    cv2.imshow('Webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows

            #code for playing song
            elif 'song' in self.query:
                speak("ok sir playing music")
                song_dir = 'D:\\project songs\\songs'
                song = os.listdir(song_dir)
                print(song)
                random_number = random.randrange(1, 9)
                os.startfile(os.path.join(song_dir, song[random_number]))

            #code for closing vlc
            elif'close vlc' in self.query:
                speak('ok sir closing vlc..')
                os.system('taskkill /im vlc.exe')
    
            #code for locking system
            elif 'lock' in self.query:
                speak(" ok sir locking the device")
                ctypes.windll.user32.LockWorkStation()
            
            #code for restarting the system
            elif "restart" in self.query:
                speak("Please hold On a second sir ! Your system is on its way to restart")
                time.sleep(10)
                subprocess.call(["shutdown", "/r"])
    
            #code for shutdown the system
            elif 'shutdown system' in self.query:
                speak("Please hold On a second sir ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                
            #code for the else part of the elif
            else:
                print("Do you have any other work")
                speak("Sir please tell me what should I do now?")


startExecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:/minor project code/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/minor project code/T8bahf1.gif")        
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication([])
jarvis = Main()
jarvis.show() 
exit(app.exec_())