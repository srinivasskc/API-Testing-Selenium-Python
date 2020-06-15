import requests
import json
import jsonpath


# API URLS
url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response)
print(response.content)

# Fetch Specific Value from Response Content.
# First we need to parse response in the form of JSON.
# To Do: Import JSON

json_response = json.loads(response.text)
print(json_response)

# Fetch Values using JSONPath
# TO DO: Import JSONPath
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])

total_pages = jsonpath.jsonpath(json_response, 'total')
print(total_pages[0])


# Assert Pages
assert pages[0] == 2

