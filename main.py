import streamlit as st
from mainbot import generate_questions, generate_answers, generate_convo, check_code, test_case
import subprocess
import tempfile
import os

if 'page' not in st.session_state:
    st.session_state.page = "Main"

st.title("The Shikshak App")
st.markdown("Explore questions and answers generation tailored to different topics and difficulty levels.")
st.sidebar.title("Navigation")
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
    st.write("Enter your code below and click 'Run Code' to execute it, or 'Check Code' to get feedback.")

    # Programming language dropdown within Code Ground section
    language = st.selectbox("Select Programming Language", ("Python", "JavaScript", "C", "C++"))

    # Code editor
    code = st.text_area("Write your code here:", placeholder="Write code here...", height=300, key="code_input")

    # Buttons for running and checking code
    col1, col2 = st.columns([1, 1])
    run_button = col1.button("Run Code")
    check_button = col2.button("Check Code")

    # Execute code
    if run_button and code.strip():
        if language == "Python":
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
                temp_file.write(code.encode("utf-8"))
                file_path = temp_file.name
            try:
                result = subprocess.run(["python", file_path], capture_output=True, text=True, check=True)
                st.success("Output:")
                st.code(result.stdout)
            except subprocess.CalledProcessError as e:
                st.error("Error in your code:")
                st.code(e.stderr)
            finally:
                os.remove(file_path)

        elif language == "JavaScript":
            with tempfile.NamedTemporaryFile(suffix=".js", delete=False) as temp_file:
                temp_file.write(code.encode("utf-8"))
                file_path = temp_file.name
            try:
                result = subprocess.run(["node", file_path], capture_output=True, text=True, check=True)
                st.success("Output:")
                st.code(result.stdout)
            except subprocess.CalledProcessError as e:
                st.error("Error in your code:")
                st.code(e.stderr)
            finally:
                os.remove(file_path)

        elif language == "C":
            with tempfile.NamedTemporaryFile(suffix=".c", delete=False) as temp_file:
                temp_file.write(code.encode("utf-8"))
                file_path = temp_file.name
                output_file = tempfile.NamedTemporaryFile(delete=False).name
            try:
                compile_result = subprocess.run(["gcc", file_path, "-o", output_file], capture_output=True, text=True)
                if compile_result.returncode == 0:
                    run_result = subprocess.run([output_file], capture_output=True, text=True)
                    st.success("Output:")
                    st.code(run_result.stdout)
                else:
                    st.error("Compilation Error:")
                    st.code(compile_result.stderr)
            finally:
                os.remove(file_path)
                if os.path.exists(output_file):
                    os.remove(output_file)

        elif language == "C++":
            with tempfile.NamedTemporaryFile(suffix=".cpp", delete=False) as temp_file:
                temp_file.write(code.encode("utf-8"))
                file_path = temp_file.name
                output_file = tempfile.NamedTemporaryFile(delete=False).name
            try:
                compile_result = subprocess.run(["g++", file_path, "-o", output_file], capture_output=True, text=True)
                if compile_result.returncode == 0:
                    run_result = subprocess.run([output_file], capture_output=True, text=True)
                    st.success("Output:")
                    st.code(run_result.stdout)
                else:
                    st.error("Compilation Error:")
                    st.code(compile_result.stderr)
            finally:
                os.remove(file_path)
                if os.path.exists(output_file):
                    os.remove(output_file)

    elif run_button:
        st.warning("Please enter some code to run.")

    # Check Code feature
    if check_button and code.strip():
        result = check_code(code)
        st.write("### Code Feedback:")
        st.write(result)
    elif check_button:
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
    
    st.image("/Users/deepeshjha/Desktop/codespace/new1.png", use_column_width=False, width=250)
