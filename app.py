import streamlit as st
import google.generativeai as genai
import json
from datetime import datetime

# Configure basic page settings
st.set_page_config(
    page_title="Buddy AI",
    page_icon="🤖",
    layout="wide"
)

# Initialize variables to store chat history and settings
if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_mode" not in st.session_state:
    st.session_state.current_mode = "default"

if "chat" not in st.session_state:
    st.session_state.chat = None

if "api_key_from_secrets" not in st.session_state:
    st.session_state.api_key_from_secrets = None

# Different ways the AI can behave
prompts = {
    "default": """You are a helpful, friendly assistant named Buddy. 
    You provide concise and accurate information. 
    If you don't know something, admit it rather than making up an answer.
    Keep your responses short and to the point unless asked for detailed explanations.""",
    
    "expert": """You are now in EXPERT mode. You are a knowledgeable expert who provides 
    detailed, technical, and accurate information. Structure your answers with clear 
    headings and include relevant technical details when appropriate. Cite your sources 
    of information when possible.""",
    
    "creative": """You are now in CREATIVE mode. You are an imaginative and artistic 
    assistant. Make your responses colorful, metaphorical, and engaging. Feel free to 
    use stories, analogies, and creative examples to illustrate your points.""",
    
    "concise": """You are now in CONCISE mode. Provide extremely brief answers. 
    Use no more than 1-2 short sentences for any response. Focus only on the most 
    essential information."""
}

try:
    st.session_state.api_key_from_secrets = st.secrets.get("GOOGLE_API_KEY", "")
except:
    pass

# Set up new chat session
def init_chat(api_key):
    if not api_key:
        return None
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
    chat = model.start_chat(history=[])
    chat.send_message(prompts[st.session_state.current_mode])
    return chat

# Function to change persona mode
def change_mode(mode):
    if mode != st.session_state.current_mode:
        st.session_state.current_mode = mode
        
        try:
            if st.session_state.chat:
                response = st.session_state.chat.send_message(prompts[mode])
                st.session_state.messages.append({"role": "assistant", "content": f"Switched to {mode.upper()} mode!"})
        except Exception as e:
            st.error(f"Error changing mode: {str(e)}")
            
        st.rerun()

# Save chat history as JSON file
def download_chat_history():
    chat_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "messages": st.session_state.messages
    }
    
    chat_json = json.dumps(chat_data, indent=2)
    
    st.download_button(
        label="Download Chat History",
        data=chat_json,
        file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
        mime="application/json"
    )

# Handle chat reset/exit
def reset_chat():
    st.session_state.messages = []
    
    api_key = st.session_state.api_key_from_secrets
    if not api_key and "api_key" in st.session_state:
        api_key = st.session_state.api_key
        
    st.session_state.chat = init_chat(api_key)
    st.rerun()

# Function to handle API key submission
def handle_api_key_submit():
    # Called when the user inputs their API key
    if st.session_state.api_key:
        st.session_state.chat = init_chat(st.session_state.api_key)
        st.session_state.messages.append({"role": "assistant", "content": "Hi there! I'm Buddy, your AI assistant. How can I help you today?"})

# Main app layout
st.title("🤖 Buddy AI Assistant")

# Sidebar for API key and controls
with st.sidebar:
    st.header("Settings")
    
    if st.session_state.api_key_from_secrets:
        st.success("API key loaded from secrets!")
        active_api_key = st.session_state.api_key_from_secrets
        
        if st.session_state.chat is None:
            st.session_state.chat = init_chat(active_api_key)
            st.session_state.messages.append({"role": "assistant", "content": "Hi there! I'm Buddy, your AI assistant. How can I help you today?"})
    else:
        st.text_input(
            "Enter your Google AI Studio API key:", 
            type="password", 
            key="api_key",
            on_change=handle_api_key_submit
        )
        
        active_api_key = st.session_state.get("api_key", "")
    
    # Only show the rest of the controls if API key is provided
    if active_api_key:
        st.subheader("Persona Selection")
        st.write("Choose the AI assistant's persona:")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Default", use_container_width=True):
                change_mode("default")
            if st.button("Expert", use_container_width=True):
                change_mode("expert")
        with col2:
            if st.button("Creative", use_container_width=True):
                change_mode("creative")
            if st.button("Concise", use_container_width=True):
                change_mode("concise")
        
        st.info(f"Current mode: {st.session_state.current_mode.upper()}")
        
        # Download and reset options
        st.subheader("Chat Options")
        download_chat_history()
        
        if st.button("Reset Chat", type="primary", use_container_width=True):
            reset_chat()
        
        st.caption("Note: Chat history will be lost when you close the browser unless you download it.")

# Main chat interface
st.subheader("Chat with Buddy")

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

active_api_key = st.session_state.api_key_from_secrets
if not active_api_key and "api_key" in st.session_state:
    active_api_key = st.session_state.api_key

# Accept user input if API key is available
if active_api_key:
    if prompt := st.chat_input("Type your message here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            try:
                response = st.session_state.chat.send_message(prompt)

                message_placeholder.markdown(response.text)

                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
            except Exception as e:
                error_message = f"Error: {str(e)}"
                message_placeholder.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})
else:
    st.info("Please enter your Google AI Studio API key in the sidebar to start chatting.")

# Footer
st.markdown("---")
st.caption("Powered by Google Gemini AI. Created by Saif Siddique.")
