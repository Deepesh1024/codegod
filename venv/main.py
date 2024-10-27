# 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
import streamlit as st
from mainbot import generate_questions
# Set up the title and description
st.title("Question generator")
# Create two columns for side-by-side input fields
col1, col2 = st.columns(2)
# Place the inputs in each column
with col1:
    topic = st.text_input("Enter the topic:")
with col2:
    difficulty = st.selectbox("Select difficulty level:", ["1", "2","3", "4", "5"])


questions = generate_questions(topic, difficulty)
# Displaying the result
if st.button("Submit"):
    if topic:
        # st.write(f"You selected the topic: {topic}")
        # st.write(f"Difficulty level chosen: {difficulty}")
        st.write(f"Here are you five questions on {topic} and the difficulty level chosen: {difficulty}")
        for key, value in questions.items():
            st.write(f"{value}\n")
    else:
        st.write("Please enter a topic before submitting.")
