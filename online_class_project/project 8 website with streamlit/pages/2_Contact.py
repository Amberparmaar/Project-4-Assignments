import streamlit as st

st.title("📬 Contact Me")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send")

    if submit:
        st.success(f"Thanks {name}, your message has been sent!")
