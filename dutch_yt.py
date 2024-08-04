import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from youtube_transcript_api import YouTubeTranscriptApi
import re
import requests
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from dotenv import load_dotenv
load_dotenv()
import os

# Streamlit APP setup
st.set_page_config(page_title="LangChain: Summarize Dutch YouTube Video", page_icon="🦜")
st.title("🦜 LangChain:  Summarize Dutch YouTube Video")
st.subheader('Enter YouTube URL')

# Get the Groq API Key and YouTube URL
groq_api_key = os.getenv("GROQ_API_KEY")
youtube_url = st.text_input("YouTube URL", label_visibility="collapsed")

# Azure Translator setup
subscription_key = os.getenv("AZURE_API_KEY")
endpoint = 'https://api.cognitive.microsofttranslator.com/translate'
region = 'westeurope'

def translate_text(text, from_lang='nl', to_lang='en'):
    body = [{'text': text}]
    params = {
        'api-version': '3.0',
        'from': from_lang,
        'to': to_lang
    }
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Region': region
    }
    response = requests.post(endpoint, params=params, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()[0]['translations'][0]['text']
    else:
        raise Exception(f"Translation failed with status code {response.status_code}")

def summarize_text(text):
    llm = ChatGroq(model="Gemma-7b-It", groq_api_key=groq_api_key)
    prompt_template = """
    Summarize the following text in a concise manner:

    1. Provide a brief title for the summary (2-5 words).
    2. Write a paragraph summarizing the main points and key ideas.
    3. If applicable, mention any specific techniques or exercises described.
    4. Conclude with the overall purpose or takeaway of the content.

    Text: {text}
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
    chat_message = [
        SystemMessage(content="You are an expert at summarizing video content concisely."),
        HumanMessage(content=prompt.format(text=text))
    ]
    return llm(chat_message).content

if st.button("Summarize Video"):
    if not groq_api_key.strip() or not youtube_url.strip():
        st.error("Please provide both the API key and YouTube URL to get started")
    elif not validators.url(youtube_url):
        st.error("Please enter a valid YouTube URL")
    else:
        try:
            with st.spinner("Summarizing..."):
                video_id = re.search(r"v=([^&]+)", youtube_url).group(1)
                transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['nl'])
                combined_text = ' '.join(segment['text'] for segment in transcript if 'text' in segment).strip()
                translated_text = translate_text(combined_text)
                summary = summarize_text(translated_text)
                st.markdown(summary)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
