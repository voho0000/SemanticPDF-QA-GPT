import requests
from dotenv import load_dotenv
import os
import streamlit as st
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI, AzureChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory
import ast

def answer_question(docs, user_question, useAzure):
    # add Azure gpt-4 api support in the future
    if useAzure:
        os.environ["OPENAI_API_TYPE"] = "azure"
        os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
        os.environ["OPENAI_API_BASE"] = "https://user1-create-gpt.openai.azure.com/" 
        os.environ["OPENAI_API_KEY"] = os.getenv("AZURE_API_KEY")
        chat = AzureChatOpenAI(deployment_name="gpt-4", openai_api_version="2023-03-15-preview")
        # chat = AzureChatOpenAI(deployment_name="gpt-35-turbo", openai_api_version="2023-03-15-preview")
    else:
        os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
        chat = ChatOpenAI(temperature=0.1)

    messages = [SystemMessage(
        content="You are a helpful bot for doctor. If needed, you can use the following document to help you answer the question in traditional Chinese.")]

    # Add the relevant documents to the chat context
    for i, doc in enumerate(docs):
        messages.append(SystemMessage(content=f"Document {i+1}: {doc}"))

    messages.append(HumanMessage(content=user_question))

    response = chat(messages).content
    # messages.append(AIMessage(content=response))

    return response

def classify_drug(user_question, useAzure):
    try:
        if useAzure:
            os.environ["OPENAI_API_TYPE"] = "azure"
            os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
            os.environ["OPENAI_API_BASE"] = "https://user1-create-gpt.openai.azure.com/" 
            os.environ["OPENAI_API_KEY"] = os.getenv("AZURE_API_KEY")
            chat = AzureChatOpenAI(deployment_name="gpt-4", openai_api_version="2023-03-15-preview")
            # chat = AzureChatOpenAI(deployment_name="gpt-35-turbo", openai_api_version="2023-03-15-preview")
        else:
            os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
            chat = ChatOpenAI(temperature=0.1)

        messages = [SystemMessage(
            content="You are a helpful bot for doctor. Please extract the medications of the texts and output in the format of ['drug1', 'drug2', 'drug3']. No other explanation is needed. If there is no medication, output:[]")]

        messages.append(HumanMessage(content=user_question))

        response = chat(messages).content
        # messages.append(AIMessage(content=response))

        return response
    
    except Exception as e:
        st.error(f"Error answering question: {e}")
        return "I'm sorry, I couldn't process your question. Please try again."

def search_documents(drugs):
    load_dotenv()
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY_2')
    PINECONE_API_ENV = 'asia-southeast1-gcp-free'
    INDEX_NAME = "nhi-v2"
    # Initialize Pinecone
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)
    # Initialize embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY'))

    # Load Pinecone index
    docsearch = Pinecone.from_existing_index(index_name=INDEX_NAME, embedding=embeddings)

    docs = []
    drugs = ast.literal_eval(drugs)
    if len(drugs)>0:
        for drug in drugs:
            drug_docs = docsearch.similarity_search(drug, include_metadata=True)
            if len(drugs)>4:
                docs.extend(drug_docs[0])
            else:
                docs.extend(drug_docs[0:2])
    return docs

def display_chat_history(chat_history_container):
    with chat_history_container:
        chat_history_html = "<div style='height: 500px; overflow-y: scroll;'>"
        st.header("Chat History")
        for msg in st.session_state.chat_history:
            chat_history_html += (
                f"<div style='text-align: right; color: blue;'>You: {msg['user']}</div>"
            )
            chat_history_html += (
                f"<div style='text-align: left; color: green;'>GPT-4: {msg['response']}</div>"
            )
        
        chat_history_html += "</div>"
        
        st.write(chat_history_html, unsafe_allow_html=True)

def display_selected_documents(col, docs):
    if not docs:
        return

    for idx, doc in enumerate(docs):
        title = f"Document {idx+1}"
        with col.expander(title):
            st.write(doc.page_content)
        
def main():
    # Load the .env file located in the project directory
    load_dotenv()
    useAzure = True
    
    st.set_page_config(page_title="Ask 健保規定", layout="wide")

    st.header("Ask 健保規定 💬")

    # Initialize docs and selected_documents
    docs = []

    col1, col2 = st.columns([0.4, 0.6])  # Adjust column width
    
    # Store chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    with col1:
        # Show user input
        user_question = st.text_input("Ask a question about 健保規定:")

        # Send button
        if st.button("Send"):
            drugs = classify_drug(user_question, useAzure = useAzure)
            docs = search_documents(drugs)

            response = answer_question(docs, user_question,  useAzure = useAzure)
            st.session_state.chat_history.append({"user": user_question, "response": response})

            # Clear user input
            user_question = ""

        # Display document 
        display_selected_documents(col1, docs)

    with col2:
        # Initialize chat history container
        chat_history_container = st.empty()

        # display chat
        display_chat_history(chat_history_container)

if __name__ == "__main__":
    main()