
# YT and Website Summarizer : Powered by LangChain 🦜

## Overview

A YouTube and Website Summarizer powered by LangChain and Groq AI that generates concise summaries of YouTube videos or web articles from URLs. Built with Streamlit, it uses yt-dlp to extract video content and Groq's LLM (Gemma2-9b-it) for summarization.

## Features

- **Summarize YouTube Videos**: Extracts titles and descriptions from YouTube using yt-dlp and generates summaries.
- **Summarize Websites**: Processes website content and provides a concise summary.
- **Interactive UI**: User-friendly interface built with Streamlit.
- **Advanced LLM**: Uses Groq's Gemma2-9b-it model for accurate summarization.

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/yt-website-summarizer.git
cd yt-website-summarizer
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the app:
```bash
streamlit run app.py
```

## Prerequisites

- Python 3.8+
- Groq API Key (required for the LLM)
- Stable internet connection

## Usage

Start the app using `streamlit run app.py`.  
Enter your **Groq API Key** in the sidebar.  
Input a valid URL (YouTube or website) in the text field.  
Click **"Summarize the Content from YT or Website"**.  
View the summarized content.

## Code Overview

### Main File: `app.py`

The core logic for the summarizer resides in `app.py`. Key components include:

- **Input Handling**: Accepts YouTube or website URLs via the Streamlit interface.
- **Validation**: Uses `validators` to verify valid URLs.
- **YouTube Content Extraction**: Utilizes yt-dlp to extract video title and description.
- **Website Content Loading**: Leverages `UnstructuredURLLoader` to process website text.
- **Summarization**: Employs LangChain's summarization chain and Groq AI's Gemma2-9b-it model.

### Dependencies

- **Streamlit**: Interactive web app framework.
- **LangChain**: Summarization pipeline framework.
- **Groq AI**: Advanced language model for summarization.
- **yt-dlp**: Extracts content from YouTube videos.
- **validators**: URL validation.

## Future Enhancements

- Add support for other document formats (e.g., PDFs).
- Include multilingual summarization.
- Enable customizable summary lengths.
- Enhance error handling for edge cases.

## Troubleshooting

- **Invalid URL Error**: Ensure the URL is correct and starts with `http://` or `https://`.
- **API Key Issues**: Verify your Groq API key is entered correctly in the sidebar.
- **Content Loading Errors**: Ensure the URL points to publicly accessible content.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.
