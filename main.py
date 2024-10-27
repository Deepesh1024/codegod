import streamlit as st
from mainbot import generate_questions, generate_answers, generate_convo, check_code, test_case

# Initialize the session state for page if not already set
if 'page' not in st.session_state:
    st.session_state.page = "Main"

# Title and Sidebar
st.title("The Shikshak App")
st.markdown("Explore questions and answers generation tailored to different topics and difficulty levels.")
st.sidebar.title("Navigation")
st.session_state.page = st.sidebar.radio("Choose a page:", ["Home", "Generate Questions", "Generate Answers", "Code Ground", "Test Cases"])

# Define the Generate Questions Page
if st.session_state.page == "Generate Questions":
    st.markdown("### 📝 Question Generator")
    st.write("Generate customized questions based on a topic and difficulty level.")
    
    # Input fields for topic and difficulty
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            topic = st.text_input("Enter the topic:", placeholder="e.g., Machine Learning")
        with col2:
            difficulty = st.selectbox("Select difficulty level:", ["1", "2", "3", "4", "5"])
    
    # Generate Questions button
    if st.button("Generate Questions"):
        if topic:
            questions = generate_questions(topic, difficulty)
            st.write(f"### Here are your questions on **{topic}** (Difficulty: **{difficulty}**)")
            for idx, question in questions.items():
                st.write(f"{idx}: {question}")
        else:
            st.warning("Please enter a topic before generating questions.")

# Define the Generate Answers Page
elif st.session_state.page == "Generate Answers":
    st.markdown("### 🧩 Answer Generator")
    st.write("Get answers for specific questions based on your topic and difficulty level.")
    
    # Input fields for question and difficulty
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            question = st.text_input("Enter the question:", placeholder="e.g., What is supervised learning?")
        with col2:
            difficulty = st.selectbox("Difficulty level:", ["1", "2", "3", "4", "5"])
    
    # Generate Answer button
    if st.button("Generate Answer"):
        if question:
            solution = generate_answers(question, difficulty)
            st.write(f"### Answer for: **{question}**")
            st.write(solution)
        else:
            st.warning("Please enter a question before generating an answer.")

# Define the Code Ground Page
elif st.session_state.page == "Code Ground":
    st.markdown("### 🖥️ Code Ground")
    st.write("Enter your code below and click 'Check Code' to process it.")

    # Custom CSS for wider text area
    st.markdown("""
        <style>
            .big-text-area {
                width: 100%;  /* Set to full width */
                height: 500px; /* Adjust this height as needed */
            }
        </style>
    """, unsafe_allow_html=True)

    # Code input box with custom class
    code_input = st.text_area("Enter your code:", placeholder="Write your code here...", height=500, key="code_input", help="Max length: 5000 characters")

    # Check Code button
    if st.button("Check Code"):
        if code_input:
            st.session_state['user_code'] = code_input
            result = check_code(st.session_state['user_code'])
            st.write("### Code Output:")
            st.write(result)
        else:
            st.warning("Please enter some code to check.")

# Define the Test Cases Page
elif st.session_state.page == "Test Cases":
    st.markdown("### 🧪 Test Case Generator")
    st.write("Generate input-output test cases for a coding question.")
    
    # Input field for the question
    question_input = st.text_input("Enter the coding question:", placeholder="e.g., Implement a stack using arrays.")

    # Generate Test Cases button
    if st.button("Generate Test Cases"):
        if question_input:
            cases = test_case(question_input)  # Call the function
            st.write(f"### Test Cases for: **{question_input}**")
            
            # Display the raw output for debugging
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

# Define the Home Page
else:
    st.write("### Hi!! Use the text box below to talk to me")
    user_input = st.text_input("Enter your message:", placeholder="Type your question or message here...")

    # Submit button for conversation
    if st.button("Submit"):
        if user_input:
            response = generate_convo(user_input)
            st.write("### Response:")
            st.write(response)
        else:
            st.warning("Please enter a message before submitting.")
    
    # Image display
    st.image("/Users/deepeshjha/Desktop/codespace/Screenshot 2024-10-27 at 3.12.46 PM.png", use_column_width=False, width=250)
