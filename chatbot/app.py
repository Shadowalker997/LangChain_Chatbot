

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

#Load the environment variables from the .env file
load_dotenv()

#Set the OPENAI_API_KEY environment variable to the value of the OPENAI_API_KEY environment variable
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
#
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")



##Prompt Template
#Prompt template is used to define the prompt for the model
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries"),
    ("user", "Question:{question}")
])

##Streamlit framework
#Streamlit is a framework to create web apps for data science and AI
st.title("Langchain Demo With OPEN API")
input_text = st.text_input("Search the topic you want")

#OPEN AI LLM
#ChatOpenAI is a class to create a chat model
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
#Chain is a class to create a chain of LLM calls
chain = prompt|llm|output_parser


#If the user input is not empty, then the chain is invoked with the user input
#Takes the user input and returns the response from the model
if input_text:
    st.write(chain.invoke({'question': input_text}))

