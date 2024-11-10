import json
import random

# Function to generate test cases
def sum_test_cases(num_cases=100):
    test_cases = []
    
    for _ in range(num_cases):
        # Random numbers for input
        a = random.randint(10, 2345)
        b = random.randint(-2345, 3456)
        
        # Generating the test case in the requested format
        test_case = {
            "code": "Sum of two numbers",
            "language": "cpp",
            "input": [a, b],
            "output": a + b
        }
        
        test_cases.append(test_case)
    
    return test_cases

def diff_test_cases(num_cases=100):
    test_cases = []
    
    for _ in range(num_cases):
        # Random numbers for input
        a = random.randint(-567, 999)
        b = random.randint(3, 34556)
        
        # Generating the test case in the requested format
        test_case = {
            "code": "Difference of two numbers",
            "language": "cpp",
            "input": [a, b],
            "output": a - b
        }
        
        test_cases.append(test_case)
    
    return test_cases

def product_test_cases(num_cases=100):
    test_cases = []
    
    for _ in range(num_cases):
        # Random numbers for input
        a = random.randint(1, 100)
        b = random.randint(-5000, 100)
        
        # Generating the test case in the requested format
        test_case = {
            "code": "Product of two numbers",
            "language": "cpp",
            "input": [a, b],
            "output": a*b
        }
        
        test_cases.append(test_case)
    
    return test_cases

def sum_of_array_test_cases(num_cases=100, min_length=3, max_length=10, min_value=-500, max_value=500, language="cpp"):
    test_cases = []
    
    for _ in range(num_cases):
        # Generate a random list of numbers with a random length
        array_length = random.randint(min_length, max_length)
        numbers = [random.randint(min_value, max_value) for _ in range(array_length)]
        
        # Calculate the expected sum
        expected_sum = sum(numbers)
        
        # Generating the test case in the requested format
        test_case = {
            "code": "Sum of the array",
            "language": language,
            "input": numbers,
            "output": expected_sum
        }
        
        test_cases.append(test_case)
    
    return test_cases

def two_sum_test_cases(num_cases=100):
    test_cases = []
    
    for _ in range(num_cases):
        # Generate a random list of numbers
        numbers = [random.randint(-100, 100) for _ in range(5)]
        
        # Choose two distinct indices to form a valid target
        idx1, idx2 = random.sample(range(len(numbers)), 2)
        target = numbers[idx1] + numbers[idx2]
        
        # Generating the test case in the requested format
        test_case = {
            "code": "Two Sum",
            "language": "cpp",
            "input": {
                "numbers": numbers,
                "target": target
            },
            "output": [idx1, idx2]
        }
        
        test_cases.append(test_case)
    
    return test_cases

def linear_search_test_cases(num_cases=100):
    test_cases = []
    
    for _ in range(num_cases):
        # Generate a random list of numbers
        numbers = [random.randint(-100, 100) for _ in range(5)]
        
        # Randomly decide if the target should be in the list or not
        if random.choice([True, False]):
            # Select a random index and use its value as the target
            target_idx = random.randint(0, len(numbers) - 1)
            target = numbers[target_idx]
            output = target_idx
        else:
            # Select a target not in the list
            target = random.randint(-100, 100)
            while target in numbers:
                target = random.randint(-100, 100)
            output = -1  # Target not found in the list
        
        # Generating the test case in the requested format
        test_case = {
            "code": "Linear Search",
            "language": "cpp",
            "input": {
                "numbers": numbers,
                "target": target
            },
            "output": output
        }
        
        test_cases.append(test_case)
    
    return test_cases
# Generate 100 test cases
test_cases = sum_test_cases(1000)
test_cases1 = diff_test_cases(1000)
test_cases2 = product_test_cases(1000)
test_cases3 = sum_of_array_test_cases(1000)
test_cases4 = two_sum_test_cases(1000)
test_cases5 = linear_search_test_cases(1000)


# Convert to JSON format
json_output = json.dumps([test_cases, test_cases1, test_cases2, test_cases3, test_cases4], indent=4)

# Save to a file (optional)
with open("test_cases.json", "w") as file:
    file.write(json_output)
