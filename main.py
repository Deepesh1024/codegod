import streamlit as st
from mainbot import generate_questions, generate_answers, generate_convo
if 'page' not in st.session_state:
    st.session_state.page = "Main"
st.title("The Shikshak App")
st.markdown("Explore questions and answers generation tailored to different topics and difficulty levels.")
st.sidebar.title("SIDE BAR TO HELL")
st.session_state.page = st.sidebar.radio("Choose a page:", ["Home", "Generate Questions", "Generate Answers"])
if st.session_state.page == "Generate Questions":
    st.markdown("### 📝 Question Generator")
    st.write("Generate customized questions based on a topic and difficulty level.")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            topic = st.text_input("Enter the topic:", placeholder="e.g., Machine Learning")
        with col2:
            difficulty = st.selectbox("Select difficulty level:", ["1", "2", "3", "4", "5"])
    if st.button("Generate Questions"):
        if topic:
            questions = generate_questions(topic, difficulty)
            st.write(f"### Here are your five questions on **{topic}** with difficulty level: **{difficulty}**")
            for idx, question in questions.items():
                st.write(f"{idx}. {question}")
        else:
            st.warning("Please enter a topic before generating questions.")
elif st.session_state.page == "Generate Answers":
    st.markdown("### 🧩 Answer Generator")
    st.write("Get answers for specific questions based on your topic and difficulty level.")
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            question = st.text_input("Enter the question:", placeholder="e.g., What is supervised learning?")
        with col2:
            difficulty = st.selectbox("Difficulty level:", ["1", "2", "3", "4", "5"])
    if st.button("Generate Answer"):
        if question:
            solution = generate_answers(question, difficulty)
            st.write(f"### Answer for: **{question}**")
            st.write(solution)
        else:
            st.warning("Please enter a question before generating an answer.")
else:
    st.write("### HI!! Use the text box below to talk to me")
    user_input = st.text_input("Enter your message:", placeholder="Type your question or message here...")

    if st.button("Submit"):
        if user_input:
            response = generate_convo(user_input)
            st.write(f"### Response:")
            st.write(response)
        else:
            st.warning("Please enter a message before submitting.")
    st.image("/Users/deepeshjha/Desktop/codespace/Screenshot 2024-10-27 at 3.12.46 PM.png", use_column_width=False, width=250)
