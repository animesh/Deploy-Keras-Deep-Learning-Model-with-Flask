import requests

data = {
"LFQ intensity 4_TK9_apim1": 21.943673,
"LFQ intensity 5_TK9_apim_2": 0.000000,
"LFQ intensity 6_TK9_apim_3": 22.097802
}

TEST_URL = "http://localhost:5000"

r = requests.post(TEST_URL, json=data)
print(r.json())
