import OpenAI
import streamlit as st 

def main():
  st.title('Youtube Script Generator')
  prompt = st.text_input('Plug in your promt here')

  llm = OpenAI(temperature=0.9)
  if prompt:
    response = llm(prompt)
    st.write(response)

if __name__ == '__main__':
  main()
