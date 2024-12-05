from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

prompt5 = ChatPromptTemplate.from_messages([
    ("system", 
     "You are the AI backbone of an AI-based coding platform. Based on the given question {question} and language {language}, generate a class and function template. "
     "The class should be appropriately named (default to `Solution` if unspecified), and the function should be named and parameterized according to the problem's requirements. "
     "Ensure the output adheres to the syntax and conventions of the specified language, and avoid adding comments or explanations in the code. and don't give the answer just the class and the function")
])


def temp_gen(question, language): 
    formatted_prompt = prompt5.format_prompt(question= question, language = language)
    llm = ChatGroq(api_key="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", model="llama-3.1-70b-versatile")
    template = llm.invoke(formatted_prompt.to_messages())
    return template.content


result = temp_gen("Sum of two numbers", "Python")
print(result)