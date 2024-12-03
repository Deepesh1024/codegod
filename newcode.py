from langchain_groq import ChatGroq

API_KEY = "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"

def generate_code(prompt: str, output_file: str) -> None:
    """
    Uses LLM to generate Python code and writes it to a file.
    """
    llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0.2, api_key=API_KEY)
    
    print(f"Prompt to LLM:\n{prompt}\n")
    
    response = llm.invoke(prompt)  
    generated_code = response.content  
    import re
    code_pattern = r"```python\n(.*?)```"
    match = re.search(code_pattern, generated_code, re.DOTALL)
    if match:
        clean_code = match.group(1).strip()
    else:
        lines = generated_code.split('\n')
        code_lines = []
        in_code = False
        for line in lines:
            if line.strip().startswith('def ') or in_code:
                in_code = True
                code_lines.append(line)
        clean_code = '\n'.join(code_lines)
    
    print(f"Extracted Code:\n{clean_code}\n")
    with open(output_file, "w") as file:
        file.write(clean_code)
    print(f"Code written to {output_file}")
    
    print("\nExecuting the generated code:")
    try:
        # Execute the code in its own namespace
        namespace = {}
        exec(clean_code, namespace)
            
    except Exception as e:
        print(f"Error executing the code: {str(e)}")

def main():
    print("\nWhat kind of Python code would you like to generate?")
    print("For example: 'Write a function that calculates factorial of a number'")
    user_prompt = input("Your prompt: ")
    output_file = "generated_code.py"
    generate_code(user_prompt, output_file)
    print(f"\nGenerated code saved to {output_file}. Execute it using 'python {output_file}' in Bash.")

    
if __name__ == "__main__":
    main()
