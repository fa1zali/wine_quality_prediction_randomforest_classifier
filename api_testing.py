import json
import requests

url = "http://127.0.0.1:8000/get_wine_quality"

payload = {
            "fixed_acidity": 7.9,
            "volatile_acidity": 0.35,
            "citric_acid": 0.46,
            "residual_sugar": 3.6,
            "chlorides": 0.078,
            "free_sulfur_dioxide": 15,
            "total_sulfur_dioxide": 37,
            "density": 0.9973,
            "pH": 3.35,
            "sulphates": 0.86,
            "alcohol": 12.8
            }

json_payload = json.dumps(payload)

response = requests.post(url, data = json_payload)
print(response)
print(response.text)