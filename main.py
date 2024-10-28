import streamlit as st
from mainbot import generate_questions, generate_answers, generate_convo, check_code, test_case

if 'page' not in st.session_state:
    st.session_state.page = "Main"

st.title("__The Shikshak App__")
st.markdown("Explore questions and answers generation tailored to different topics and difficulty levels.")

st.sidebar.title("Side Bar 2 Hell")
st.session_state.page = st.sidebar.radio("Choose a page:", ["Home", "Generate Questions", "Generate Answers", "Code Ground", "Test Cases"])

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
            st.write(f"### Here are your questions on **{topic}** (Difficulty: **{difficulty}**)")
            for idx, question in questions.items():
                st.write(f"{idx}: {question}")
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

elif st.session_state.page == "Code Ground":
    st.markdown("### 🖥️ Code Ground")
    st.write("Enter your code below and click 'Check Code' to process it.")

    st.markdown("""
        <style>
            .big-text-area {
                width: 100%;  /* Set to full width */
                height: 500px; /* Adjust this height as needed */
            }
        </style>
    """, unsafe_allow_html=True)

    code_input = st.text_area("Enter your code:", placeholder="Write your code here...", height=500, key="code_input", help="Max length: 5000 characters")

    if st.button("Check Code"):
        if code_input:
            st.session_state['user_code'] = code_input
            result = check_code(st.session_state['user_code'])
            st.write("### Code Output:")
            st.write(result)
        else:
            st.warning("Please enter some code to check.")

elif st.session_state.page == "Test Cases":
    st.markdown("### 🧪 Test Case Generator")
    st.write("Generate input-output test cases for a coding question.")
    
    question_input = st.text_input("Enter the coding question:", placeholder="e.g., Implement a stack using arrays.")

    if st.button("Generate Test Cases"):
        if question_input:
            cases = test_case(question_input)  # Call the function
            st.write(f"### Test Cases for: **{question_input}**")
            
            st.write("Raw Output from LLM:")
            st.write(cases)  # Debugging: print the raw output

            if cases.get("Error"):
                st.warning("No test cases were generated. Try refining the question or use simpler phrasing.")
            else:
                st.write("### Generated Test Cases:")
                for inp, out in cases.items():
                    st.write(f"Input: {inp} | Output: {out}")
        else:
            st.warning("Please enter a coding question before generating test cases.")

else:
    st.write("### Hi!! Use the text box below to talk to me")
    user_input = st.text_input("Enter your message:", placeholder="Type your question or message here...")

    if st.button("Submit"):
        if user_input:
            response = generate_convo(user_input)
            st.write("### Response:")
            st.write(response)
        else:
            st.warning("Please enter a message before submitting.")
    
    st.image("new1.png", use_column_width=False, width=250)
