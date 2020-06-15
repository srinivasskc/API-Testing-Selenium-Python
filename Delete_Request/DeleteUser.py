import requests

# Delete User
url = "https://reqres.in/api/users/2"

#  Deleting the User.
response = requests.delete(url)
print(response)

print(response.headers)
print(response.cookies)
print(response.status_code)

# Again verifying the request using GET request
get_response = requests.get(url)
print(get_response)
print(get_response.text)