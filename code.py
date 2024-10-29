import streamlit as st
import subprocess
import tempfile
import os

# Set up the layout and app title
st.set_page_config(page_title="Simple Coding IDE", layout="wide")
st.title("Simple Coding IDE")

# Sidebar to select language
language = st.sidebar.selectbox("Select Programming Language", ("Python", "JavaScript", "C", "C++"))

# Main code editor
st.write("### Code Editor")
code = st.text_area("Write your code here:", height=300)

# Button to run code
if st.button("Run Code"):
    if not code.strip():
        st.warning("Please write some code before running!")
    else:
        if language == "Python":
            # Python code execution
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
                temp_file.write(code.encode("utf-8"))
                temp_file.flush()
                file_path = temp_file.name

            try:
                result = subprocess.run(["python", file_path], capture_output=True, text=True, check=True)
                st.success("Output:")
                st.code(result.stdout)
            except subprocess.CalledProcessError as e:
                st.error("Error in your code:")
                st.code(e.stderr)

        elif language == "JavaScript":
            # JavaScript code execution
            with tempfile.NamedTemporaryFile(suffix=".js", delete=False) as temp_file:
                temp_file.write(code.encode("utf-8"))
                temp_file.flush()
                file_path = temp_file.name

            try:
                result = subprocess.run(["node", file_path], capture_output=True, text=True, check=True)
                st.success("Output:")
                st.code(result.stdout)
            except subprocess.CalledProcessError as e:
                st.error("Error in your code:")
                st.code(e.stderr)

        elif language == "C":
            # C code execution
            with tempfile.NamedTemporaryFile(suffix=".c", delete=False) as temp_file:
                temp_file.write(code.encode("utf-8"))
                temp_file.flush()
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
            # C++ code execution
            with tempfile.NamedTemporaryFile(suffix=".cpp", delete=False) as temp_file:
                temp_file.write(code.encode("utf-8"))
                temp_file.flush()
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
