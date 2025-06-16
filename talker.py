import google.generativeai as genai

# ✅ Setup
genai.configure(api_key="AIzaSyBB0irbxOR59HdylF49270dEDI2dNjpWuw")  # Use dotenv in production

# ✅ Load interview.txt once
with open("interview.txt", "r", encoding="utf-8") as file:
    persona_data = file.read()

# ✅ Talker: Send user input with persona
def talker(user_prompt):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        full_prompt = f"""
You are Furkan Khan, answering as yourself.

Here is your background and personality:
{persona_data}

Now respond to this question as Furkan would: "{user_prompt}"

If the answer is not in the profile, respond thoughtfully in his tone (concise, practical, and honest).
"""
        response = model.generate_content(full_prompt)
        print("🔍 Gemini raw response:\n", response.text)
        return response.text or "No response from Gemini."
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "Gemini failed to generate content."
