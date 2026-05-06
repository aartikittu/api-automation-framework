import json
import requests

def generate_test_cases(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "phi3",   # 👈 use phi3 (faster)
        "prompt": prompt,
        "stream": False
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers, timeout=120)

    data = response.json()

    return data["response"]


output = generate_test_cases(
    'Return ONLY a valid JSON array. No markdown. No explanation. Use double quotes for all keys and string values. Generate 3 login API test cases with fields: "username", "password", "expected_status". expected_status must be numeric like 200, 401, 400.'
)


print("RAW OUTPUT START")
print(output)
print("RAW OUTPUT END")

clean_output = output.replace("```json", "").replace("```", "").strip()
test_cases = json.loads(clean_output)

print(type(test_cases))
print(test_cases[0])

for test in test_cases:
    print("Username:", test["username"])
    print("Password:", test["password"])
    print("Expected:", test["expected_status"])
    print("-----")