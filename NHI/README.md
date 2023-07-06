
# 健保規定詢問 Chatbot

This is a chatbot designed to assist doctors in answering questions based on provided documents. It is implemented using OpenAI's language model (GPT-4 or GPT-35-turbo) and can output in traditional Chinese. It is developed using Python and the Streamlit framework.

The bot also has a feature to extract medications from texts and search relevant documents based on the extracted drugs.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/voho0000/SemanticPDF-QA-GPT.git
```

2. Navigate to the project directory:

```bash
cd SemanticPDF-QA-GPT
cd NHI
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the App

To run the app, use the command:

```bash
streamlit run app.py
```

## Environment Variables

The app requires the following environment variables.
These variables should be placed in a `.env` file in your project directory.
```bash
OPENAI_API_KEY = Your OpenAI API key
AZURE_API_KEY = Your Azure API key
PINECONE_API_KEY = Your Pinecone API key
```
