import speech_recognition as sr
import smtplib
# import pyaudio
# import platform
# import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
global translation11,translation1
from translate import Translator


#fetch project name
tts = gTTS(text="Voice based Email for blind", lang='en')
ttsname=("D:/name.mp3") 
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

#login from os
login = os.getlogin
print ("You are Sign in sucessfully from  "+login()+"System")

#choices
print ("1. composed a Your mail")
tts = gTTS(text="option 1. composed a Your mail.", lang='en')
ttsname=("D:/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

print ("2. Check your inbox")
tts = gTTS(text="option 2. Check your inbox", lang='en')
ttsname=("D:/second.mp3")
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

#this is for input choices
tts = gTTS(text="Please Speak Your Choice ", lang='en')
ttsname=("D:/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

#voice recognition part
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Your choice is:")
    audio=r.listen(source)
    print ("Voice Recognised Successfully")
    tts = gTTS(text="Voice Recognised Successfully", lang='en')
    ttsname=("hello1.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

try:
    text=r.recognize_google(audio)
    print ("You said your choice as: "+text)
    tts = gTTS(text="You said your choice as: "+text, lang='en')
    ttsname=("hello2.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)
    if text == '1' or text == 'One' or text == 'one'or text == '11':
            global translation11,translation1
            
            TTS = gTTS(text='Please said  body of mail ')
            TTS.save("voice.mp3")
            os.system("voice.mp3")
        
            r = sr.Recognizer()
            print("Please talk")
            with sr.Microphone() as source:
             # read the audio data from the default microphone
                audio_data = r.record(source, duration=10)
                print("Recognizing...")
                # convert speech to text
                bd = r.recognize_google(audio_data)
                print("Body of mail is:"+bd)
                translator= Translator(from_lang="English",to_lang="English")
                translation1 = translator.translate(bd)
                print(translation1)
                TTS = gTTS(text=translation1)
                TTS.save("voice.mp3")
                os.system("voice.mp3")
        
            
            with sr.Microphone() as source:    
                print ("Sender Mail ID :")
                # audio1=r.listen(source)
                # print ("Voice Recognised Successfully")
                # tts = gTTS(text="Voice Recognised Successfully", lang='en')
                # ttsname=("hello3.mp3") 
                # tts.save(ttsname)
                # music = pyglet.media.load(ttsname, streaming = False)
                # music.play()
                # time.sleep(music.duration)
                # os.remove(ttsname)
                
                TTS = gTTS(text='Please said  Receiver Mail id ')
                TTS.save("voice.mp3")
                os.system("voice.mp3")
        
                r = sr.Recognizer()
                print("Please talk")
                with sr.Microphone() as source:
               # read the audio data from the default microphone
                  audio_data = r.record(source, duration=10)
                print("Recognizing...")
                # convert speech to text
                text = r.recognize_google(audio_data)
                print("Mail ID is is:"+text)
                str1 = text.replace(" ", "")
                str1 = text.replace("dot", ".")
                str1 = text.replace("at the rate", "@")
                translator= Translator(from_lang="English",to_lang="English")
                translation1 = translator.translate(text)
                print(translation1)
                TTS = gTTS(text=translation1)
                TTS.save("voice.mp3")
                os.system("voice.mp3")
                print(str1)
                mail = smtplib.SMTP('smtp.gmail.com',587)    #host and port area
                mail.ehlo()  #Hostname to send for this command defaults to the FQDN of the local host.
                mail.starttls() #security connection
                mail.login('pragati.code@gmail.com',' grqheqzoutabdfzd') #login part
                mail.sendmail('shital.sct@gmail.com','ankita.sctcode@gmail.com',bd) #send part
                print ("Congrates! Your mail has send. ")
                tts = gTTS(text="Congrates! Your mail has send ", lang='en')
                ttsname=("D:/send.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
                tts.save(ttsname)
                music = pyglet.media.load(ttsname, streaming = False)
                music.play()
                time.sleep(music.duration)
                os.remove(ttsname)
                mail.close()   
        
                
        
        
    if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' :
        mail = imaplib.IMAP4_SSL('imap.gmail.com',993) #this is host and port area.... ssl security
        #unm = ('srcdocs190@gmail.com')  #username
        #psw = ('3847@V!nodmrun@l')  #password
        mail.login('pragati.code@gmail.com','grqheqzoutabdfzd')  #login
        stat, total = mail.select('Inbox')  #total number of mails in inbox
        print ("Number of mails in your inbox :"+str(total))
        tts = gTTS(text="Total mails are :"+str(total), lang='en') #voice out
        ttsname=("D:/total.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        
        #unseen mails
        unseen = mail.search(None, 'UnSeen') # unseen count
        print ("Number of UnSeen mails :"+str(unseen))
        tts = gTTS(text="Your Unseen mail :"+str(unseen), lang='en')
        ttsname=("D:/unseen.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        # music = pyglet.media.load(ttsname, streaming = False)
        # music.play()
        # time.sleep(music.duration)
        os.remove(ttsname)
        
        #search mails
        result, data = mail.uid('search',None, "ALL")
        inbox_item_list = data[0].split()
        new = inbox_item_list[-1]
        old = inbox_item_list[0]
        result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
        raw_email = email_data[0][1].decode("utf-8") #decode
        email_message = email.message_from_string(raw_email)
        print ("From: "+email_message['From'])
        print ("Subject: "+str(email_message['Subject']))
        tts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
        ttsname=("D:/mail.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        
        #Body part of mails
        stat, total1 = mail.select('Inbox')
        stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
        msg = data1[0][1]
        soup = BeautifulSoup(msg, "html.parser")
        txt = soup.get_text()
        print ("Body :"+txt)
        tts = gTTS(text="Body: "+txt, lang='en')
        ttsname=("D:/body.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        mail.close()
        mail.logout()

except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio.")
     
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

#choices details
