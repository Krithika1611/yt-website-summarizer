import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain.schema import Document  # Correct Document class
from langchain_community.document_loaders import UnstructuredURLLoader
from yt_dlp import YoutubeDL
import re

# Streamlit App
st.set_page_config(page_title="YT and Website Summarizer : Powered by LangChain 🦜", page_icon="🦜")
st.title("YT and Website Summarizer : Powered by LangChain 🦜")
st.subheader('Summarize URL')

# Sidebar for API key
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

# Input for URL
generic_url = st.text_input("URL", label_visibility="collapsed")

# Helper function to check for YouTube URLs
def is_youtube_url(url):
    youtube_regex = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+"
    return re.match(youtube_regex, url) is not None

# Function to load YouTube content using yt-dlp
def get_youtube_transcript(url):
    try:
        ydl_opts = {
            "quiet": True,
            "format": "bestaudio/best",
            "skip_download": True,
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            transcript = info.get("description", "No description available.")
            title = info.get("title", "No title available.")
            return f"Title: {title}\n\nTranscript: {transcript}"
    except Exception as e:
        raise RuntimeError(f"Failed to extract YouTube content: {e}")

# LLM Initialization
if groq_api_key:
    llm = ChatGroq(model="Gemma2-9b-it", groq_api_key=groq_api_key)

# Prompt Template
prompt_template = """
Please summarize the following content into 300 words:
{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Summarize Button Logic
if st.button("Summarize the Content from YT or Website"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide both the API key and a valid URL to get started.")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL.")
    else:
        try:
            with st.spinner("Loading content and generating summary..."):
                # Determine loader based on URL type
                if is_youtube_url(generic_url):
                    content = get_youtube_transcript(generic_url)
                    docs = [Document(page_content=content)]  # Correct format
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        headers={
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
                        }
                    )
                    raw_docs = loader.load()
                    docs = [Document(page_content=doc.page_content) for doc in raw_docs]

                # Summarization Chain
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.run(docs)

                st.success(output_summary)
        except RuntimeError as re:
            st.error(f"Error: {re}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
