from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
prompt = ChatPromptTemplate.from_messages([
    ("system", "Generate exactly 5 coding questions inspired by real-life scenarios on the topic: {topic} and difficulty level: {difficulty}. Each question should start on a new line without any introductory or concluding text. Just the questions.")
])

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "Generate the solution for the coding question in C language. Question: {question}. Difficulty level: {difficulty} and also explain the code by taking small code snippets and code examples and real life examples.")
])

prompt3 = ChatPromptTemplate.from_messages([
    ("system", "You are a computer science assistant professor. Reply to all the student education related queries {query}.")
])
prompt4 = ChatPromptTemplate.from_messages([
    ("system", "You are a computer science assistant professor. Check the code {code} given to you be the user is correct or not.")
]
)
prompt5 = ChatPromptTemplate.from_messages([
    ("system", "Create exactly 10 unique test cases for this coding question: {question}. Each test case should be formatted as follows:\n\n"
               "Input: <array of integers>, Target: <target integer> | Output: <indices or values that satisfy the condition>\n\n"
               "Example test case:\n"
               "Input: [1, 2, 3, 4], Target: 5 | Output: [0, 3]\n"
               "Input: [3, 6, 8, 12], Target: 14 | Output: [0, 2]\n\n"
               "Return only the 10 test cases without extra text.")
])
def generate_answers(question, difficulty): 
    formatted_prompt = prompt2.format_prompt(question=question, difficulty=difficulty)
    llm = Ollama(model="llama3:8b")
    response = llm.invoke(formatted_prompt.to_messages())
    return ''.join(response) if isinstance(response, list) else response
def generate_questions(topic, difficulty):
    formatted_prompt = prompt.format_prompt(topic=topic, difficulty=difficulty)
    llm = Ollama(model="llama3:8b")
    response = llm.invoke(formatted_prompt.to_messages())
    questions_text = ''.join(response) if isinstance(response, list) else response
    questions = {}
    for i, question in enumerate(questions_text.split('\n\n'), start=1):
        if question.strip():
            questions[f"Question {i}"] = question.strip()
    return questions
def generate_convo(query):
    formatted_prompt = prompt3.format_prompt(query=query)
    llm = Ollama(model="llama3:8b")
    reply = llm.invoke(formatted_prompt.to_messages())
    return reply
def check_code(code):
    formatted_prompt = prompt4.format_prompt(code=code)
    llm = Ollama(model="llama3:8b")
    review = llm.invoke(formatted_prompt.to_messages())
    return review
def test_case(question):
    formatted_prompt = prompt5.format_prompt(question=question)
    llm = Ollama(model="llama3:8b")
    response = llm.invoke(formatted_prompt.to_messages())
    response_text = ''.join(response) if isinstance(response, list) else response
    print("Debug - Raw LLM Response:", response_text)  # Debugging print
    test_cases = {}
    lines = response_text.splitlines()  # Split response by line
    for line in lines:
        if "Input:" in line and "Output:" in line:
            try:
                input_part = line.split("Input:")[1].split("|")[0].strip()
                output_part = line.split("Output:")[1].strip()
                test_cases[input_part] = output_part
            except IndexError:
                continue
    if not test_cases:
        test_cases["Error"] = "No test cases generated. Adjust prompt or try different phrasing."
    return test_cases


