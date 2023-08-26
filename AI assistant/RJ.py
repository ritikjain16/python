import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


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

    speak("I am RJ. Please tell me how may I help you")       


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




if __name__ == "__main__":
    wishMe()

    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        # if 'wikipedia' in query:
        #     speak('Searching Wikipedia...')
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     speak("According to Wikipedia")
        #     print(results)
        #     speak(results)

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\\Users\\DA0327TU\\Desktop\\Python\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open VS code' in query:
            codePath = "C:\\Users\\DA0327TU\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open android studio' in query:
            myFilePath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(myFilePath)

        elif 'open excel' in query:
            speak("opening M S Excel in few seconds...")
            myFilePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(myFilePath)

        elif 'open powerpoint' in query:
            speak("opening M S Powerpoint in few seconds...")
            myFilePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(myFilePath)

        elif 'open outlook' in query:
            speak("opening Outlook in few seconds...")
            myFilePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(myFilePath)

        elif 'open 1 note' in query:
            speak("opening One Note in few seconds...")
            myFilePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(myFilePath)
        
        elif 'open word' in query:
            speak("opening M S word in few seconds...")
            myFilePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(myFilePath)
        
        else:
            speak("Oops! Try Again sir!..")



