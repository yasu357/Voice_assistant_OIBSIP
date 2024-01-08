import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("Hello! I am your basic voice assistant. How can I help you today?")

def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def main():
    wish_me()

    while True:
        command = listen_command()

        if "hello" in command:
            speak("Hello! How can I assist you today?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {current_date}")

        elif "search" in command:
            speak("What do you want to search for?")
            search_query = listen_command()

            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
                speak(f"Here is what I found for {search_query} on the web.")
    
        elif "reminder" in command or "remind" in command:
           speak("Sure, what would you like me to remind you about?")
           reminder_text = listen_command()
           speak(f"Okay, I will remind you: {reminder_text} at a later time.")

        elif "exit" in command or "bye" in command:
            speak("Goodbye! Have a great day.")
            break

if __name__ == "__main__":
    main()
