## integrate code with OpenAI API
import os
from langchain.llms import OpenAI

import streamlit as st

os.environ['OPENAI_API_KEY'] = "sk-proj-V6kd5GR4DKJ0y3WSJpIGT3BlbkFJFIpJHkaMmRy8Ou9BFxWJ"

# streamlit framework

st.title('Langchain Demo with OpenAI API')
input_text = st.text_input("Search the topic you want")

## OPENAI LLMS
llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
