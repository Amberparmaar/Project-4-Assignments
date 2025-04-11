import streamlit as st
from datetime import datetime
import time
from PIL import Image


# Page config
st.set_page_config(page_title="My Personal Website", layout="centered")

# Load and show logo
logo = Image.open("assets/logo.png")
st.image(logo, width=150)

# Sidebar
st.sidebar.title("🧑‍💻 Your Info")
name = st.sidebar.text_input("What's your name?", "Guest")
st.sidebar.write(f"👋 Hello, {name}!")

st.sidebar.markdown("---")
st.sidebar.markdown("Made by ❤️ Amber Parmaar")

# Title
st.title("🌐 Welcome to My Python Website!")
st.subheader("Built in minutes using Streamlit.")

# Resume download
with open("assets/resume.pdf", "rb") as file:
    st.download_button("📄 Download My Resume", file, file_name="My_Resume.pdf", mime="application/pdf")


# Skills with progress bars
st.markdown("### 💼 My Skills")
st.progress(85)  # Python
st.text("Next Js - 65%")
st.progress(70)  # HTML
st.text("HTML & CSS - 70%")
st.progress(60)  # Streamlit
st.text("Streamlit - 60%")

# Live clock (optional)
current_time = datetime.now().strftime("%H:%M:%S")
st.markdown(f"🕒 Current Time: `{current_time}`")

# Contact form preview (real form in another page)
st.markdown("### 📬 Want to reach out?")
st.write("Go to the **Contact** page in the sidebar.")

