import streamlit as st
st.title("My AI Chat Bot  ")
st.write("welcome Enter your question below.")
prompt=st.text_input("Enter your prompt:")
if st.button("Generate"):
    if prompt:
        st.success("prompt generates successfully!")
        st.write("### Your prompt:")
        st.write(prompt)
    else:
        st.warning("Please enter a prompt")