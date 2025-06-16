import speech_recognition as sr

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening... Please ask your question.")
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("⚠️ Could not understand the audio.")
        return None
    except sr.RequestError:
        print("⚠️ Speech Recognition service unavailable.")
        return None

listen_to_user()