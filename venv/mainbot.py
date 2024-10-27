from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Generate exactly 5 coding questions inspired by real-life scenarios on the topic: {topic} and difficulty level: {difficulty}. Each question should start on a new line without any introductory or concluding text. Just the questions.")
    ]
)
prompt2 = ChatPromptTemplate.from_messages(
    [
        ("system", "Generate the solution for the coding question in C language. Question: {question}. Difficulty level: {difficulty}.")
    ]
)

def generate_answers(question, difficulty): 
    formatted_prompt = prompt2.format_prompt(question=question, difficulty=difficulty)
    llm = Ollama(model="llama3:8b")
    response = llm.invoke(formatted_prompt.to_messages())
    return ''.join(response) if isinstance(response, list) else response

# Example usage
question = "Implement a queue using a linked list in C with enqueue and dequeue operations."
difficulty = "3"

solution = generate_answers(question, difficulty)
print("Solution:\n", solution)

# def generate_questions(topic, difficulty):
#     formatted_prompt = prompt.format_prompt(topic=topic, difficulty=difficulty)
#     llm = Ollama(model="llama3:8b")
#     response = llm.invoke(formatted_prompt.to_messages())
#     questions_text = ''.join(response) if isinstance(response, list) else response
    
#     questions = {}
#     for i, question in enumerate(questions_text.split('\n\n'), start=1):
#         if question.strip():
#             questions[f"Question {i}"] = question.strip()
#     return questions

# topic = "queues"
# difficulty = "3"

# questions = generate_questions(topic, difficulty)
# for key, value in questions.items():
#     # print(f"{key}:\n{value}\n")
