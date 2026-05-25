# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 12:59:56 2022

@author: audum
"""
import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import speech_recognition as sr
import time
from playsound import playsound 
from translate import Translator
import os
from gtts import gTTS
import cv2


TTS = gTTS(text='You want to capture your photo')     
    
TTS.save("voice.mp3")
os.system("voice.mp3")

r = sr.Recognizer()
print("Please talk")
with sr.Microphone() as source:        
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=10)
    print(audio_data)
    
              
print("Recognizing...")
    # convert speech to text
text = r.recognize_google(audio_data)
if  text == 'yes': 
 
        from subprocess import call
        call(["python", "demo camera.py"]) 

    
print("capture your photo Sucessfully:"+text)
translator= Translator(from_lang="English",to_lang="English")
translation1 = translator.translate(text)
print(translation1)
TTS = gTTS(text=translation1)
TTS.save("voice.mp3")
os.system("voice.mp3")
   