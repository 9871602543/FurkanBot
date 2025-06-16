import streamlit as st
from listen_to_user import listen_to_user
from speak_text import speak
from talker import talker

st.set_page_config(page_title="🎤 Furkan Voice Bot", layout="centered")

st.title("🧠 Furkan Khan Voice Bot")
st.write("Ask me anything, and I’ll respond as myself!")

# Main interaction
if st.button("🎙️ Ask Your Question"):
    question = listen_to_user()
    
    if question:
        st.success(f"🗣️ You asked: {question}")
        
        with st.spinner("🤔 Thinking..."):
            response = talker(question)

        st.markdown("**🤖 Furkan says:**")
        st.write(response)

        # Automatically speak response
        speak(response)
    else:
        st.error("⚠️ Sorry, I couldn’t understand your voice. Try again.")
