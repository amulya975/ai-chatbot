import streamlit as st
import ollama
st.title("Welcome to AI Chatbot")
st.caption("hii")
prompt=st.text_input("Ask me anything")
if st.button("Generate"):
    if  prompt:
       st.success("Generate response...")
       st.error
    else:
        st.warning("Please enter a question.")
    response=ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content":prompt
            }
        ]
    )
    st.write(response["message"]["content"])
    