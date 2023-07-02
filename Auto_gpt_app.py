
import os 
from apikey import apikey

import streamlit as st 
from transformers import pipeline 


import langchain 
from langchain.llms import OpenAI
from langchain.prompts import 

os.environ['OPENAI_API_KEY'] = apikey

# App framework 
st.title('Youtube Script Generator')
prompt = st.text_input('Plug in your promt here')

# llms -> using the Huggingface gpt2 because OpenAi is paid now 
generator = pipeline('text-generation', model='gpt2')

if prompt:
    response = generator(prompt, max_length=100)[0]['generated_text']
    st.write(response)
