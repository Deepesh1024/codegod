import requests
import json

def test_api():
    # Base URL for the API
    base_url = "http://127.0.0.1:8000"
    
    def print_response(endpoint, response):
        print(f"\n=== Testing {endpoint} ===")
        print(f"Status Code: {response.status_code}")
        print("Response:")
        print(json.dumps(response.json(), indent=2))
        print("="*50)

    try:
        # Test 1: Generate Questions
        print("\nTesting question generation...")
        questions_response = requests.post(
            f"{base_url}/generate_questions",
            params={
                "topic": "array sorting algorithms",
                "difficulty": "intermediate"
            }
        )
        print_response("Generate Questions", questions_response)

        # Test 2: Generate Solution
        print("\nTesting solution generation...")
        solution_response = requests.post(
            f"{base_url}/generate_solution",
            params={
                "question": "Write a program to implement bubble sort algorithm",
                "difficulty": "beginner"
            }
        )
        print_response("Generate Solution", solution_response)

        # Test 3: Educational Query
        print("\nTesting educational query...")
        convo_response = requests.post(
            f"{base_url}/generate_convo",
            params={
                "query": "Can you explain how recursion works in programming?"
            }
        )
        print_response("Educational Query", convo_response)

        # Test 4: Code Check
        print("\nTesting code check...")
        sample_code = """
        int bubbleSort(int arr[], int n) {
            int i, j;
            for (i = 0; i < n-1; i++)
                for (j = 0; j < n-i-1; j++)
                    if (arr[j] > arr[j+1]) {
                        int temp = arr[j];
                        arr[j] = arr[j+1];
                        arr[j+1] = temp;
                    }
            return 0;
        }
        """
        code_check_response = requests.post(
            f"{base_url}/check_code",
            params={"code": sample_code}
        )
        print_response("Code Check", code_check_response)

        # Test 5: Generate Test Cases
        print("\nTesting test case generation...")
        test_cases_response = requests.post(
            f"{base_url}/generate_test_cases",
            params={
                "question": "Write a program to find two numbers in an array that sum up to a target value"
            }
        )
        print_response("Generate Test Cases", test_cases_response)

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_api()