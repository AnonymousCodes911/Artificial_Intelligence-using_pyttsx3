
import pyttsx3                        # pip install pyttsx3


import speech_recognition as sr       # pip install speech_recognition



import datetime


import wikipedia                      # pip install wikipedia


import webbrowser


import os


import smtplib


import googlesearch                 #pip install googlesearch


from googlesearch import search






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id) #id [1], for female voice.


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
        speak("Wonderfull evening")  

    speak("I am /NameOfYourAI\, what can i do for you, Master ")       

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Let me listen")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("i am processing")    
        query = r.recognize_google(audio, language='en-in')                     # Google is the best when inputing audio data from user
        print(f"your query: {query}\n")

    except Exception:
                                                                            #keeps the Loop working until terminating command is run
        speak(f'what else i can do for you?')  
        print("Please repeat")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()



        if 'what is' in query :
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'                     #Your Google Chore directory
            speak(f'let me  search it for you')
            query1=""
            list_needed=""
            str1=""
            if 'what is' in query :
                list_name=list(query)
                list_needed=list_name[8:]
                
                for ele in list_needed:  
                    str1 += ele   
            

            for url in search(str1, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % str1)
        
        
        
        
        elif 'who is' in query:
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s' 
            speak(f'let me see who are you talking about')
            query2=""
            list_needed=""
            str2=""
            if 'who is' in query :
                list_name=list(query)
                list_needed=list_name[7:]
                
                for word in list_needed:  
                    str2 += word   
            

            for url in search(str2, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % str2)


           

        
        
        

    
       
        elif 'wikipedia' in query :
            
            print('Fetching results from Wikipedia, PLease stay patient')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(f' i ll fetch the results from wiki pedia , it takes me , seconds to read that data base, please wait')
            speak("Wikipedia says")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("Opening Youtube in a new window")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("Opening Google")
            webbrowser.open("google.com")

        elif 'open facebook' in query: 
            print("Opening facebook")
            webbrowser.open("facebook.com")   


        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time by my atomic clock is {strTime}")
            print(strTime)
        
        
        elif 'who are you' in query:
            speak(f'I am a brainchild of my sole creator, /YourName\.')

        elif 'why were you created' in query:
           speak(f'#yourCreativeAnswer')
        
        elif 'what is the best coding language' in query:
            speak(f'Obviously Python and its other varyants, how come you even ask that, but more likely i should be biased, hence all are pretty amazing')
        

        elif 'where to study coding' in query:
            speak(f'there are a lot of websites that teach coding, still my favourite is W3 Schools, and geeks for geeks')
            webbrowser.open("www.w3schools.com")
            webbrowser.open("www.geeksforgeeks.org")
            
        ''''
        elif 'where is' in query:
            speak(f'let me see where you want to go')                          
            list_needed=""
            str3=""
            if 'where is' in query :
                list_name=list(query)                                                            # This section is underdevelopment, using the Google_Maps API
            query2=""
                list_needed=list_name[7:]
                
                for word in list_needed:  
                    str3 += word   
            

            for url in search(str3, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://www.google.com/search?q=%s" % str3)
        ''''


        elif 'please open' in query:
            speak(f'let me open it via your chosen browser')
            list_needed=""
            str4=""
            if 'please open' in query :
                list_name=list(query)
                list_needed=list_name[11:]
                
                for word in list_needed:  
                    str4 += word   
            

            for url in search(str4, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://www.google.com/search?q=%s" % str4)
            

        


        elif 'bye take care' in query:
            speak(f"Thank you for listening to /YourAI\ ")
            print("Exiting, thanks for using my interface")
            break
        
# add your queries at will
# happy coding


            

        


        
