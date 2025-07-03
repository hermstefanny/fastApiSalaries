import requests

response_1 = requests.get("http://127.0.0.1:8000/")
print("===========")
print(response_1.content)

for i in range(10):
    print(requests.get(f"http://127.0.0.1:8000/number/{i}").content)

response_3 = requests.post(
    "http://127.0.0.1:8000/message", json={"message": " This is a test"}
)
print("\n===========")
print(response_3.content)

response_4 = requests.post(
    "http://127.0.0.1:8000/salary_computation",
    json={"salary": 2500, "bonus": 200, "taxes": 400},
)
print("\n===========")
print(response_4.content)
