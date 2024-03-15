import requests

input_data = {"selfies_sequence": "[C]",
              "target_location": "bah"}

response = requests.post("http://127.0.0.1:1456/", json=input_data)
text = response.text

print(text)
