# AI Chatbot with Google Gemini and Streamlit

![Chatbot Demo](https://img.shields.io/badge/demo-live-success)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.32.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A beginner-friendly AI chatbot using Google's Gemini AI model and Streamlit for the web interface. This project demonstrates how to create a conversational agent with multiple personas and basic prompt engineering techniques.

## Live Demo

Try the chatbot live: [AI Chatbot Demo](https://buddy-ai-assistant.streamlit.app/)

## Video Demo

[Watch the video demonstration](https://example.com/video-demo)


## Features

- Interactive chat interface with message history
- Multiple AI personas (Default, Expert, Creative, Concise)
- Download chat history as JSON
- Reset chat functionality
- Secure API key handling
- Responsive design for desktop and mobile

## Technologies Used

- [Python](https://www.python.org/) - Core programming language
- [Streamlit](https://streamlit.io/) - Web app framework
- [Google Gemini AI](https://ai.google.dev/) - Large Language Model API

## Prerequisites

Before you begin, make sure you have:

1. Python 3.7 or newer installed
2. A Google AI Studio API key (see instructions below)
3. Basic knowledge of terminal/command prompt

## Getting a Google AI Studio API Key

1. Visit [Google AI Studio](https://ai.google.dev/)
2. Sign in with your Google account
3. Click on "Get API key" or navigate to the API section
4. Create a new API key
5. Keep this key secure and never commit it to public repositories

## Installation and Setup

1. Clone this repository:
   ```
   git clone https://github.com/SaifSiddique009/buddy_ai_assistant.git
   cd buddy_ai_assistant
   ```

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   venv\Scripts\activate 
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

5. The app will open in your default web browser. Enter your API key in the sidebar to start chatting.

## Quick Try

To test this chatbot:

1. Visit the live demo link at the top of this README
2. Or follow the installation instructions to run locally
3. You'll need your own Google AI Studio API key for testing
4. If you don't have an API key, please [contact me](mailto:saif.siddique009@gmail.com) for a demonstration

## Usage Notes

- The free Google AI Studio API has usage limits. If you encounter errors, you may have reached these limits.
- Your API key is processed securely and is never stored on the server.
- Chat history is not permanently saved unless you download it.

## Prompt Engineering

This project demonstrates several prompt engineering techniques:

1. **System Prompts**: Setting clear instructions for the AI's behavior
2. **Persona Switching**: Changing the AI's tone and style based on different personas
3. **Response Formatting**: Specifying how answers should be structured
4. **Contextual Instructions**: Building specific expectations into the prompt
