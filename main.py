import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "bc177e4137a265140f7a1ef975"

def speak(text):
    engine.say(text)
    engine.runAndWait()
   
# def speak_new(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3')
#     pygame.mixer.init()
#     pygame.mixer.music.load('temp.mp3')
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#        pygame.time.Clock().tick(10)
#        os.remove('temp.mp3')
    
def aiProcessor(command):
   client = OpenAI(
    api_key="LnKhsBJ4OvT7h-w5wIBggqmrCTMeLSHsak_JIMKk_5cWOt9aajoe2zRtyYYpC0jTlAS3cC13oyT3BlbkFJdMUtzpjH3p6KcIwjZSKgF3cbq-f32zfgRx08GpIyOep8JvF6iixzJ0o_KBNwvr4-8gLHLHPv8A"
    )

   completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "You are a virtual assistant named jarvis skilled in "
            "general tasks like Alexa and Google Cloud. Give stat response please "},
            {"role": "user", "content": command}
        ]
    )

   return completion.choices[0].message.content

def processCommand(c):
     if "open youtube" in command.lower():
       webbrowser.open("https://www.youtube.com")
       speak("Opening YouTube")

     elif "open google" in command.lower():
       webbrowser.open("https://www.google.com")
       speak("Opening Google")

     elif "open stack overflow" in command.lower():
       webbrowser.open("https://stackoverflow.com")
       speak("Opening Stack Overflow")

     elif "open github" in command.lower():
       webbrowser.open("https://github.com")
       speak("Opening GitHub")

     elif "open facebook" in command.lower():
       webbrowser.open("https://www.facebook.com")
       speak("Opening Facebook")

     elif "open linkedin" in command.lower():
       webbrowser.open("https://www.linkedin.com")
       speak("Opening LinkedIn")

     elif "open instagram" in command.lower():
       webbrowser.open("https://www.instagram.com")
       speak("Opening Instagram")

     elif "open twitter" in command.lower():
       webbrowser.open("https://twitter.com")
       speak("Opening Twitter")

     elif "open whatsapp" in command.lower():
       webbrowser.open("https://web.whatsapp.com")
       speak("Opening WhatsApp")

     elif "open telegram" in command.lower():
       webbrowser.open("https://web.telegram.org")
       speak("Opening Telegram")

     elif "play" in command.lower():
         song = c.lower().split(" ")[1]
         link = musicLibrary.music[song]
         webbrowser.open(link)
         speak(f"Playing {song}")

     elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
           data = r.json()
           articles = data.get('articles', [])
           for article in articles:
              speak(article['title'])
      
     elif "goodbye" in command.lower():
        speak("Goodbye Sir! Have a nice day. See you soon. Take care.")
        exit()
     else:
        response = aiProcessor(command)
        print(response)
        speak(response)
        
if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I help you?")
    while True:
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5)
                word = recognizer.recognize_google(audio)
                if(word.lower() == "jarvis"):
                    speak("Yes")
                    with sr.Microphone() as sourse:
                        print("Jarvis Activated...")
                        audio = recognizer.listen(source)
                        word = recognizer.recognize_google(audio)
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")
                speak(f"you said: {command}")
                processCommand(command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print("Could not request results: {0}".format(e))
            speak("Could not request results. Please check your internet connection.")