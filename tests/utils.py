import requests
import json

API_URL = "http://127.0.0.1:5000/classify"

def run_tests(test_cases):
    total_tests, successful_tests, failed_tests = 0, 0, 0
    failed_test_names = []

    for test_case in test_cases:
        total_tests += test_case.get("repeat", 1)
        for i in range(test_case.get("repeat", 1)):
            result = run_test(test_case)
            if result:
                successful_tests += 1
            else:
                failed_tests += 1
                failed_test_names.append(test_case['name'])

    success_rate = (successful_tests / total_tests) * 100
    failure_rate = (failed_tests / total_tests) * 100

    print("\nTest Results Summary:")
    print(f"Total tests: {total_tests}")
    print(f"Successful tests: {successful_tests} ({success_rate:.2f}%)")
    print(f"Failed tests: {failed_tests} ({failure_rate:.2f}%)")

    if failed_tests > 0:
        print("\nFailed test names:")
        for failed_test_name in failed_test_names:
            print(f"- {failed_test_name}")

def run_test(test_case):
    print(f"Running test: {test_case['name']}")
    input_data = test_case["input"]
    expected_output = test_case["expected_output"]
    response = requests.post(API_URL, headers={"Content-Type": "application/json"}, data=json.dumps(input_data))

    if response.status_code == 200:
        response_data = response.json()
        if response_data == expected_output:
            print(f"Test '{test_case['name']}' passed")
            return True
        else:
            print(f"Test '{test_case['name']}' failed")
            print("Input:")
            print(json.dumps(input_data, indent=4))
            print("Expected output:")
            print(json.dumps(expected_output, indent=4))
            print("Actual output:")
            print(json.dumps(response_data, indent=4))
            return False
    else:
        print(f"Test '{test_case['name']}' failed with status code {response.status_code}")
        return False
