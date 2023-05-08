# Ask Your PDF

Ask Your PDF is a web application that allows users to upload a PDF or Markdown file and ask questions about the content. It utilizes GPT-3.5 to answer questions based on the uploaded document, providing a helpful interface for users to get quick answers.

## Demo
![Demo Video Link](https://youtu.be/8gNazoCVwuY)


## Features

- Supports PDF and Markdown files
- Displays the uploaded file for reference
- Allows users to ask questions about the document
- Provides answers from GPT-3.5
- Displays similar documents to the question
- Toggleable display for selected documents

## Installation

To install the required dependencies, use the following command:

To use this project, first ensure you have Python 3.x installed on your system. Next, you will need to install the required dependencies:

```bash
pip install streamlit
pip install PyPDF2
pip install langchain
pip install python-dotenv
pip install faiss-cpu
```

## Setting up the API key
1. Create a new file named .env in the root folder of your project if it doesn't already exist.

2. Add your OpenAI API key to the .env file as follows:
```makefile
OPENAI_API_KEY=your_api_key_here
```

## Usage

To run the web application, execute the following command:

```bash
streamlit run app_UI.py
```

The web application will be accessible at `http://localhost:8501`.

## How It Works

The application uses `streamlit` to create a web interface for users to upload documents and ask questions. It processes the uploaded document, extracting the text and creating a knowledge base using OpenAI Embeddings and FAISS. 

When users ask a question, the application searches the knowledge base for similar documents and generates a response using the ChatOpenAI model. The response is based on the user's question and relevant documents from the knowledge base.

The chat history is displayed to the user in a scrollable container, and the similar documents found are displayed as expandable sections below the chat input.

## Simplified version in `notebooks` folder

## Contributing

Contributions to improve the application or fix issues are welcome. Please open an issue to discuss your ideas or submit a pull request with your changes.

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).