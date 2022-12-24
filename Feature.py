import pyttsx3
import pywhatkit
from pywikihow import WikiHow,search_wikihow
import os
import webbrowser as web
import smtplib 
import wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def Speak(audio):
    print(f"Karen:{audio}")
    engine.say(audio)
    engine.runAndWait()
def youtubesearch(term):
    result="https://www.youtube.com/results?search_query="+term
    web.open(result)
    Main.Speak("This is what I found for you")
    pywhatkit.playonyt(term)
def sendEmail(to, content):
    f = open('C:\\Users\\Asus\\Documents\\a.txt', 'r')
    a = f.read()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shradulyasingh96@gmail.com', password= a)
    server.sendmail('shradulyasingh96@gmail.com', to, content)
    server.close()
    f.close()
def GoogleSearch(query):
    query = query.replace("karen","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what do you mean by","")
    query=query.replace("google search","")

    writeab = str(query)

    oooooo = open('E:\\karen\\Database\\database.txt','a')
    oooooo.write(writeab)
    oooooo.close()

    pywhatkit.search(query)

    if 'how to' in query:

        max_result = 1

        how_to_func = search_wikihow(query,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()

        Speak(how_to_func[0].summary)

    else:

        search = wikipedia.summary(query,2)
        Speak(search)
def Alarm(query):

    TimeHere=  open('E:\\karen\\Database\\database.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("E:\\karen\\Database\\extra\\Alarm.py")
def Image(query):
    query=query.replace("download","")
    query=query.replace("image","")
    query=query.replace("of", "")
    q=open('E:\\karen\\Database\\database.txt','a')
    q.write(query)
    q.close()
    os.startfile("E:\\karen\\Database\\extra\\start.py")
Image('download image of jarvis2')