import requests
import json
import jsonpath

# API URLS
url = "https://reqres.in/api/users"

# Opening the File
file = open("C:\\development\\python-scripts\\APIAutomation\\Post_Request\\createusers.json","r")
readable = file.readable()
print(readable)

# Reading the File
input_file = file.read()
print(input_file)
# The text is in Str Format

# Parse the input file to JSON Format
request_json = json.loads(input_file)
print(request_json)

# Make POST Requests with JSON INPUT Body
response = requests.post(url, request_json)
print(response)
print(response.content)
print(response.headers)
print(response.text)
print(response.url)
print(response.headers.get('Content-Type'))
print(response.headers.get('Content-Length'))

# Parse Response to JSON Format
response_json = json.loads(response.text)
print(response_json)

# Pick ID From JSON Response
id = jsonpath.jsonpath(response_json, 'id')
print(id)


# Assert Status Code
assert response.status_code == 201


