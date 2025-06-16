from gtts import gTTS
import os
import tempfile
import platform
import subprocess

def speak(text):
    print(f"🔊 Speaking: {text}")
    tts = gTTS(text)
    
    # Save audio to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        audio_path = fp.name
        tts.save(audio_path)

    # Play based on OS
    if platform.system() == "Windows":
        os.startfile(audio_path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.call(["afplay", audio_path])
    else:  # Linux
        subprocess.call(["mpg123", audio_path])
