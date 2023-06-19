import requests

url = "https://dps-ai-task-goksu-7343c3186a4c.herokuapp.com/"

data = {
    "year": 2021,
    "month": 1
}

response = requests.post(url, json=data)

if response.status_code == 200:
    try:
        prediction = response.json()["prediction"]
        print("Prediction:", prediction)
    except ValueError:
        print("Invalid JSON response")
else:
    print("Request failed with status code:", response.status_code)
