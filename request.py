import requests
import json

url = "http://localhost:5000/"  # Setting the URL for the API
data = {"year": 2021, "month": 1}  # Setting the data to send to the API

data_json = json.dumps(data)  # Converting the data to JSON format

headers = {'Content-Type': 'application/json'}  # Setting the headers for the request
response = requests.post(url, data=data_json, headers=headers)  # Making a POST request to the API

# Converting the response from byte format to string format
response_str = response.content.decode("utf-8")

# Converting the string to a JSON object
response_json = json.loads(response_str)

# Printing the JSON object
print(response_json)
