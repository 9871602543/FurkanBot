import streamlit as st
import google.generativeai as genai
import tempfile
import os
from gtts import gTTS
from io import BytesIO
from dotenv import load_dotenv
import base64
import speech_recognition as sr

genai.configure(api_key="AIzaSyBB0irbxOR59HdylF49270dEDI2dNjpWuw")

# Load persona
with open("interview.txt", "r", encoding="utf-8") as file:
    persona_data = file.read()

# Gemini response
def talker(user_prompt):
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    full_prompt = f"""
You are Furkan Khan, answering as yourself.

Here is your background and personality:
{persona_data}

Now respond to this question as Furkan would: "{user_prompt}"

If the answer is not in the profile, respond thoughtfully in his tone (concise, practical, and honest).
"""
    response = model.generate_content(full_prompt)
    return response.text or "No response from Gemini."

# Convert text to speech and return as audio bytes
def generate_audio(text):
    tts = gTTS(text)
    with BytesIO() as audio_bytes:
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes.read()

# Transcribe audio file
def transcribe_audio(file):
    recognizer = sr.Recognizer()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name
    with sr.AudioFile(tmp_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        return None

# UI
st.title("🎙️ Furkan Khan Voice Bot")
st.write("Ask me a question by uploading your voice, and I’ll answer as myself!")

audio_file = st.file_uploader("Upload your question (WAV only)", type=["wav"])

if audio_file is not None:
    with st.spinner("🧠 Transcribing..."):
        user_text = transcribe_audio(audio_file)

    if user_text:
        st.success(f"🗣️ You asked: {user_text}")

        with st.spinner("🤖 Thinking..."):
            ai_response = talker(user_text)
            st.markdown("**Furkan says:**")
            st.write(ai_response)

            with st.spinner("🔊 Generating voice..."):
                audio_bytes = generate_audio(ai_response)
                b64 = base64.b64encode(audio_bytes).decode()
                audio_html = f"""
                <audio autoplay controls>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
                st.markdown(audio_html, unsafe_allow_html=True)
    else:
        st.error("⚠️ Could not transcribe your question. Please try again.")
