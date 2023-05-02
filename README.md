# SemanticPDF-QA-GPT

## Introduction

The Langchain project is a Python implementation designed to provide an interface for extracting text from a PDF file, splitting the text into smaller chunks, generating embeddings, and performing semantic search on the chunks for answering a given question. The project leverages the PyPDF2, OpenAI API, and various vector search libraries.

## Installation

To use this project, first ensure you have Python 3.x installed on your system. Next, you will need to install the required dependencies:

```bash
pip install PyPDF2
pip install langchain
pip install python-dotenv
pip install faiss-cpu
```

Please note that other vector search libraries (such as Pinecone or Weaviate) may have their own installation requirements.

## Usage

1. Create a `.env` file in your project directory containing your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

2. Replace the `local_pdf_path` variable value with the path to the desired PDF file:

```python
local_pdf_path = "path/to/your/PDF/file.pdf"
```

3. Update the `query` variable with the question you want the system to answer based on the contents of the PDF file:

```python
query = "Your question here"
```

4. Run the script, which will output the answer to your question based on the information in the PDF file.

## Components

- `PdfReader`: Extracts text from a given PDF file.
- `OpenAIEmbeddings`: Generates embeddings for the extracted text using the OpenAI API.
- `RecursiveCharacterTextSplitter`: Splits the extracted text into smaller chunks to avoid token size limits.
- `ElasticVectorSearch`, `Pinecone`, `Weaviate`, `FAISS`: Vector search libraries for searching through text embeddings.
- `load_qa_chain`: Loads a question-answering chain using the OpenAI API.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.