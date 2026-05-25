import os
import cv2
import time
import speech_recognition as sr
from gtts import gTTS
from translate import Translator

# ------------------ COMMON FUNCTIONS ------------------

def speak(text, filename="voice.mp3"):
    tts = gTTS(text=text)
    tts.save(filename)
    os.system(filename)
    time.sleep(1)

def listen(duration=7):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.record(source, duration=duration)
    print("Recognizing...")
    return r.recognize_google(audio)

def speak_and_listen(prompt):
    speak(prompt)
    text = listen()
    translator = Translator(from_lang="English", to_lang="English")
    text = translator.translate(text)
    speak(text)
    return text

# ------------------ MAIN PROGRAM ------------------

try:
    speak("Welcome to Blind Email Registration. Speak your first name")
    first_name = speak_and_listen("Speak your first name")
    print("first_name: ", first_name)

    speak("Speak your last name")
    last_name = speak_and_listen("Speak your last name")
    print("last_name: ", last_name)

    speak("Please say your username")
    username = speak_and_listen("Say your username")
    print("username: ", username)

    speak("Please say your user ID, for example one two three")
    user_id = speak_and_listen("Say your user ID")
    user_id = user_id.replace(" ", "")
    print("user_id: ",user_id)

    # ------------------ PHOTO CAPTURE ------------------

    speak("Do you want to capture your photo?")
    choice = listen().lower()

    if choice in ["yes", "yes yes"]:
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        cap = cv2.VideoCapture(0)
        sampleN = 0

        os.makedirs("Image", exist_ok=True)

        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                sampleN += 1
                cv2.imwrite(
                    f"Image/User.{user_id}.{sampleN}.jpg",
                    gray[y:y+h, x:x+w]
                )
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                cv2.waitKey(100)

            cv2.imshow("Face Capture", img)
            if cv2.waitKey(1) & 0xFF == ord('q') or sampleN >= 40:
                break

        cap.release()
        cv2.destroyAllWindows()

        speak("Photo captured successfully")

    # ------------------ TRAIN MODEL ------------------

    speak("Do you want to train your photo?")
    train_choice = listen().lower()

    if train_choice == "yes":
        speak("Training started")
        os.system("python train.py")

    # ------------------ FINISH ------------------

    speak("Registration successful. Welcome to login page")
    os.system("python face_login.py")

# ------------------ EXCEPTIONS ------------------

except sr.UnknownValueError:
    speak("Sorry, I could not understand your voice")

except sr.RequestError as e:
    speak("Speech recognition service error")
    print(e)
