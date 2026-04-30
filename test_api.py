import requests

def validate_api(url, expected_fields):
    response = requests.get(url)

    print("Testing API:", url)
    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print("API Failed, Skipping Validation")
        print("Result: FAILED")
        print("-----")
        return False

    data = response.json()

    if isinstance(data, list) and len(data) > 0:
        all_passed = True

        for field in expected_fields:
            if field in data[0]:
                print(f"{field} field present")
            else:
                print(f"{field} field missing")
                all_passed = False

        if all_passed:
            print("Result: PASSED")
            print("-----")
            return True
        else:
            print("Result: FAILED")
            print("-----")
            return False

    else:
        print("Unexpected format")
        print("Result: FAILED")
        print("-----")
        return False


api_tests = [
    {
        "url": "https://jsonplaceholder.typicode.com/users",
        "fields": ["name", "email", "username"]
    },
    {
        "url": "https://jsonplaceholder.typicode.com/posts",
        "fields": ["title", "body", "userId"]
    },
    {
        "url": "https://jsonplaceholder.typicode.com/invalid",
        "fields": ["name"]
    }
]


passed = 0
failed = 0

for api in api_tests:
    result = validate_api(api["url"], api["fields"])

    if result:
        passed += 1
    else:
        failed += 1


print("Final Summary")
print("Passed:", passed)
print("Failed:", failed)