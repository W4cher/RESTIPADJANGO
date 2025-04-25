import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"


get_response = requests.get(endpoint)

if get_response.status_code == 200:
    try:
        print(get_response.json())
    except ValueError:
        print("erro ao decodificar JSON")
else:
    print(f" erro na requisição:{get_response.status_code}")
# print(get_response.text)

# print(get_response.json)