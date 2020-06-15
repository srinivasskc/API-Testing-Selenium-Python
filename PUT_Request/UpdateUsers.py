# PUT REQUEST
import requests
import json
import jsonpath

# API URLS
url = "https://reqres.in/api/users/2"

# Opening the File
file = open("C:\\development\\python-scripts\\APIAutomation\\PUT_Request\\updateuser.json","r")
readable = file.readable()
print(readable)

# Reading the File.
input_file = file.read()
print(input_file)

# Convert Input File Text to JSON
json_file = json.loads(input_file)
print(json_file)

# Making a PUT Request with JSON
response = requests.put(url, json_file)
print(response)
print(response.status_code)
print(response.text)
print(response.content)

# Assert Validation Status Code
assert response.status_code == 200

# Parse the JSON Response to Get a Value
response_json = json.loads(response.text)
print(response_json)

# Fetching the Value.
updated_list=jsonpath.jsonpath(response_json,'updatedAt')
print(updated_list[0])


