
import imaplib
import email
from email.header import decode_header
from gtts import gTTS
import pyglet
import os, time
import speech_recognition as sr
global translation11,translation1
from translate import Translator
# account credentials
print ("Please said  login Mail id")
tts = gTTS(text="login Mail id.", lang='en')
ttsname=("D:/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
tts.save(ttsname)


music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)


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
TTS = gTTS(text='Please said login mail id ')
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

imap = imaplib.IMAP4_SSL("imap.gmail.com")    #host and port area
# mail.ehlo()  #Hostname to send for this command defaults to the FQDN of the local host.
# mail.starttls() #security connection
imap.login('pragati.code@gmail.com',' grqheqzoutabdfzd')
#imap.login('mrajole02@gmail.com','dpndjpcxwtgmrtib')

# username = "'madhurihangarge5@gmail.com"
# password = "Yahoo1@5"

# create an IMAP4 class with SSL 

# authenticate
#imap.login(username, password)



print ("Please Select Mailbox I want to delete in")
tts = gTTS(text="Inbox.", lang='en')
ttsname=("D:/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
tts.save(ttsname)
# select the mailbox I want to delete in
# if you want SPAM, use imap.select("SPAM") instead
imap.login('pragati.code@gmail.com',' grqheqzoutabdfzd')
imap.select("INBOX")
# search for specific mails by sender
#status, messages = imap.search(None, 'FROM "googlealerts-noreply@google.com"')
# to get all mails
# status, messages = imap.search(None, "ALL")
# to get mails by subject
status, messages = imap.search(None,'SUBJECT "mail send"')
# to get mails after a specific date
# status, messages = imap.search(None, 'SINCE "01-JAN-2020"')
# to get mails before a specific date
# status, messages = imap.search(None, 'BEFORE "01-JAN-2020"')
# convert messages to a list of email IDs
messages = messages[0].split(b' ')
for mail in messages:
    _, msg = imap.fetch(mail, "(RFC822)")
    # you can delete the for loop for performance if you have a long list of emails
    # because it is only for printing the SUBJECT of target email to delete
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes type, decode to str
                subject = subject.decode()
            print("Deleting", subject)
            TTS = gTTS(text='Deleted Mail ')
            TTS.save("voice.mp3")
            os.system("voice.mp3")
    # mark the mail as deleted
    imap.store(mail, "+FLAGS", "\\Deleted")
# permanently remove mails that are marked as deleted
# from the selected mailbox (in this case, INBOX)
imap.expunge()
# close the mailbox
imap.close()
# logout from the account
imap.logout()
