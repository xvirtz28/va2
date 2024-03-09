import speech_recognition as sr
import pyttsx3
import webbrowser


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("User said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble accessing the recognition service.")
        return ""

def main():
    speak("Hello! How can I assist you today?")

    while True:
        command = take_command()

        if "reminder" in command:
            speak("Sure, what's the reminder?")
            reminder = take_command()
            speak(f"Reminder set for {reminder}")

        elif "to do" in command:
            speak("Let's add items to your to-do list. What would you like to add?")
            item = take_command()
            speak(f"Added {item} to your to-do list.")

        elif "search web" in command:
            speak("What do you want to search for?")
            query = take_command()
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")

        elif "search youtube" in command:
            speak("What do you want to search on YouTube?")
            query = take_command()
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
            speak(f"Here are the YouTube search results for {query}")

        elif "exit" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
