import requests

# API URLS
url = "https://reqres.in/api/users?page=2"

# Send GET Request
response = requests.get(url)
print(response)

response_content = response.content
print(response_content)

print(response.cookies)

print(response.encoding)

print(response.status_code)

print(response.url)

print(response.headers)
