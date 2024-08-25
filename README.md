# Dutch YouTube Video Summarizer
***
This repository contains the code for a YouTube video summarizer that translates Dutch content to English and provides concise summaries using AI technology.
***
## Project Description
**_NOTE:_** This project is a web-based tool that allows users to input a Dutch YouTube video URL and receive an English summary of its content. It leverages various APIs and AI models to extract transcripts, translate content, and generate summaries.

### Features
* YouTube URL Input: Simple interface to input Dutch YouTube video URLs.
* Transcript Extraction: Automatically extracts video transcripts using YouTube's API.
* Dutch to English Translation: Translates Dutch content to English using Azure Translator.
* AI-Powered Summarization: Generates concise summaries using Groq's language model.
* User-Friendly Interface: Built with Streamlit for easy interaction and result display.

### Prerequisites

* Python 3.x
* Streamlit
* LangChain
* YouTube Transcript API
* Azure Translator API key
* Groq API key

### Clone the repository

```
git clone (https://github.com/Savoyevatel/Dutch-video-summarization)
```
### Setup

Navigate to the project directory

```
cd Dutch-video-summarization
```

### Create a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### Install the required packages
```
pip install -r requirements.txt
```

## Set up environment variables

Copy your .env variables

### Edit the .env file and add your API keys:

AZURE_API_KEY=your_azure_translator_api_key

GROQ_API_KEY=your_groq_api_key

### Running the ProjectStart the Streamlit app

```
streamlit run app.py
```
### Using the Summarizer

Open the provided URL in your web browser.
Enter a Dutch YouTube video URL in the input field.
Click the "Summarize Video" button.
Wait for the summary to be generated and displayed.

### How It Works

The app extracts the transcript from the YouTube video.
The Dutch transcript is translated to English using Azure Translator.
The translated text is then summarized using Groq's AI model via LangChain.
The summary is displayed in a structured format on the web interface.


### Alternative installation using Docker

#### Running the Application

#### Clone the repository:

   ```
   git clone https://github.com/Savoyevatel/Dutch-video-summarization.git
   cd Dutch-video-summarization

   ```
   
#### Build the Docker image:

   ```
docker build -t dutch_yt .
   ```

#### Run the Docker container:

   ```
docker run -d -p 8501:8501 dutch_yt
   ```


Access the application in your web browser at http://localhost:8501.

### Alternative Deployed version
https://videosummarizationfromanylanguage.streamlit.app/

## References
[Streamlit documentation](https://docs.streamlit.io/get-started)
[LangChain documentation](https://python.langchain.com/v0.2/docs/introduction/)
[YouTube Transcript API documentation](https://pypi.org/project/youtube-transcript-api/)
[Azure Translator documentation](https://learn.microsoft.com/en-us/azure/ai-services/translator/)
[Groq API documentation](https://console.groq.com/docs/api-reference)
