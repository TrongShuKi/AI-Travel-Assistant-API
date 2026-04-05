import requests

API_URL = "https://hlwza-136-117-190-117.run.pinggy-free.link"

print("1. Kiểm tra Endpoint Giới thiệu (GET /)")
response = requests.get(f"{API_URL}/")
print(response.json())
print()

print("2. Kiểm tra Endpoint HEALTH (GET /health)")
response = requests.get(f"{API_URL}/health")
print(response.json())
print()

print("3. Kiểm tra chức năng Tạo Sinh (POST /generate)")
test_cases = [
    {"prompt": "Nội thành Huế có gì thu hút khách du lịch?"},
    {"prompt": "Hãy review chi tiết về khu du lịch trượt tuyết, tuyết rơi quanh năm ở Bến Tre."},
    {"prompt": ""}
]
for i, data in enumerate(test_cases):
    print(f"==== TestCase {i+1}")
    print(f"Prompt: {data['prompt']}")
    
    response = requests.post(f"{API_URL}/generate", json=data)
    
    if response.status_code == 200:
        print("AI Trả lời: ", response.json()["generated_text"])
    else:
        print(f"Lỗi {response.status_code}:", response.json())