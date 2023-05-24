
# FAQ Chatbot with OpenAI and Asana

This is a script for a FAQ chatbot application using OpenAI's GPT-3.5 for language processing, Streamlit for the user interface, FAISS for similarity search, and Asana for retrieving FAQ documents.

## Dependencies

The required libraries can be installed with pip:

```
pip install requests python-dotenv streamlit langchain faiss-cpu
```

## Setup

- Create a `.env` file in the project directory and add your OpenAI API key and Asana API key:

```env
OPENAI_API_KEY=your_openai_api_key
ASANA_API_KEY=your_asana_api_key
```

- Replace the `ASANA_PROJECT_GID` in the script with the GID of the Asana project you want to retrieve tickets from.

## Usage

- Run the script:

```bash
streamlit run app_FAQ.py
```

- The Streamlit app will start and be available at `http://localhost:8501`.

- You can ask questions in the text input field and press the Send button to get an answer. The chat history and selected documents will be displayed on the right side of the page.

