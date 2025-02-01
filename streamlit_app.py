import streamlit as st
from streamlit_chat import message as st_message
from src.chatbot import Chatbot

def chat(message, history):
    """Processes the chat message and returns the chatbot response."""
    chatbot = Chatbot()

    if not history:  # If history is empty, create a new chatbot object
        chatbot.clear_history()
    else:
        # Reconstruct chat history from stored format
        for user_message, bot_message in history:
            chatbot.chat_history.append({"role": "user", "parts": [user_message]})
            chatbot.chat_history.append({"role": "model", "parts": [bot_message]})

    response = chatbot.process_message(message)
    return response

# Streamlit UI
st.title("Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

# Chat display
chat_container = st.container()
with chat_container:
    for user_message, bot_message in st.session_state.history:
        st_message(user_message, is_user=True)
        st_message(bot_message, is_user=False)

# Fixed input section at the bottom
st.markdown("""
    <style>
        .chat-input-container {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: white;
            padding: 10px;
            box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chat-input-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([8, 2, 2])
    with col1:
        message = st.text_input("", "", key="chat_input", placeholder="Type a message...")
    with col2:
        if st.button("Send") and message:
            bot_response = chat(message, st.session_state.history)
            st.session_state.history.append((message, bot_response))
    with col3:
        if st.button("Clear Chat"):
            st.session_state.history = []
    st.markdown('</div>', unsafe_allow_html=True)
