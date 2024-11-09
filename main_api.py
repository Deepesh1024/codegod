from fastapi import FastAPI, HTTPException
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import logging
import uvicorn
import os

# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Coding Question and Solution API",
    version="1.0",
    description="An API for generating coding questions, solutions, and test cases."
)

# Initialize the Ollama model
llm = Ollama(model="llama3:8b")

# Define prompts
prompts = {
    "question": ChatPromptTemplate.from_messages([
        ("system", "Generate exactly 5 coding questions inspired by real-life scenarios on the topic: {topic} and difficulty level: {difficulty}. Each question should start on a new line without any introductory or concluding text. Just the questions.")
    ]),
    "solution": ChatPromptTemplate.from_messages([
        ("system", "Generate the solution for the coding question in C language. Question: {question}. Difficulty level: {difficulty} and also explain the code by taking small code snippets and code examples and real life examples.")
    ]),
    "convo": ChatPromptTemplate.from_messages([
        ("system", "You are a computer science assistant professor. Reply to all the student education related queries {query}.")
    ]),
    "code_check": ChatPromptTemplate.from_messages([
        ("system", "You are a computer science assistant professor. Check the code {code} given to you by the user is correct or not.")
    ]),
    "test_case": ChatPromptTemplate.from_messages([
        ("system", "Create exactly 10 unique test cases for this coding question: {question}. Each test case should be formatted as follows:\n\n"
                   "Input: <array of integers>, Target: <target integer> | Output: <indices or values that satisfy the condition>\n\n"
                   "Return only the 10 test cases without extra text.")
    ])
}

# Endpoint to generate coding questions
@app.post("/generate_questions")
async def generate_questions(topic: str, difficulty: str):
    try:
        formatted_prompt = prompts["question"].format_prompt(topic=topic, difficulty=difficulty)
        response = llm.invoke(formatted_prompt.to_messages())
        return {"questions": response}
    except Exception as e:
        logger.error(f"Error generating questions: {e}")
        raise HTTPException(status_code=500, detail="Error generating questions.")

# Endpoint to generate solution and explanation
@app.post("/generate_solution")
async def generate_solution(question: str, difficulty: str):
    try:
        formatted_prompt = prompts["solution"].format_prompt(question=question, difficulty=difficulty)
        response = llm.invoke(formatted_prompt.to_messages())
        return {"solution": response}
    except Exception as e:
        logger.error(f"Error generating solution: {e}")
        raise HTTPException(status_code=500, detail="Error generating solution.")

# Endpoint for educational query conversation
@app.post("/generate_convo")
async def generate_convo(query: str):
    try:
        formatted_prompt = prompts["convo"].format_prompt(query=query)
        response = llm.invoke(formatted_prompt.to_messages())
        return {"response": response}
    except Exception as e:
        logger.error(f"Error generating conversation: {e}")
        raise HTTPException(status_code=500, detail="Error generating conversation.")

# Endpoint to check if the code is correct
@app.post("/check_code")
async def check_code(code: str):
    try:
        formatted_prompt = prompts["code_check"].format_prompt(code=code)
        response = llm.invoke(formatted_prompt.to_messages())
        return {"code_check": response}
    except Exception as e:
        logger.error(f"Error checking code: {e}")
        raise HTTPException(status_code=500, detail="Error checking code.")

# Endpoint to generate test cases
@app.post("/generate_test_cases")
async def generate_test_cases(question: str):
    try:
        formatted_prompt = prompts["test_case"].format_prompt(question=question)
        response = llm.invoke(formatted_prompt.to_messages())
        return {"test_cases": response}
    except Exception as e:
        logger.error(f"Error generating test cases: {e}")
        raise HTTPException(status_code=500, detail="Error generating test cases.")

# Middleware for request logging
@app.middleware("http")
async def log_requests(request, call_next):
    logger.info(f"Request URL: {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
