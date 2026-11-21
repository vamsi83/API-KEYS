###BY USING GEMINI API KEY


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
#from dotenv import load_dotenv

os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6IKucDp2bBN66WeHkAzPnRO8SwVf4FP3Ll0cpuD4mIo5A"
#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

## Langmith tracking
os.environ["LANGSMITH_TRACING_V2"]="true"

#os.environ["LANGSMITH_API_KEY"]= "la773"
os.environ["LANGSMITH_API_KEY"]="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"

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","I am chatbot. I am hear to assist you. Please type your queries"),
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('LLM-OPENAI PROJECT - CUSTOM GEMINI 3.5 FLASH LITE BY VAMSI')
input_text=st.text_input("How may I help you")

# openAI LLm
llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=1)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))