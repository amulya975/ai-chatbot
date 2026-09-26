import streamlit as st
import ollama
st.title("AI Chatbot")
st.caption("hii")
prompt=st.text_input("Ask me an")
if st.button("send"):
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