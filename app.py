import streamlit as st
from google import genai
import time

# UI Setup (Browser Version)
st.set_page_config(page_title="Jarvis AI", page_icon="🤖")
st.title("J.A.R.V.I.S  MAINFRAME (Cloud)")

# API Setup
# Ab hum chabi Streamlit ke secret locker se nikalenge!
GOOGLE_API_KEY = st.secrets["MY_SECRET_KEY"]
client = genai.Client(api_key=GOOGLE_API_KEY)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Kaise ho Jarvis?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

   # AI Brain Call
    with st.chat_message("assistant"):
        with st.spinner("Soch raha hoon..."):
            try:
                response = client.models.generate_content(
                   model='gemini-2.5-flash',
                    contents=f"You are Jarvis. Reply in cool Hinglish: {prompt}"
                )
                full_response = response.text
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                # Ye line Streamlit ki security bypass karke asli error dikhayegi
                st.error(f"🚨 ASLI ERROR: {e}")
