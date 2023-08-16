import requests

username = "max00217"
api_token = "6ac4304b6f0de3ac1630e7c13fc02501292847bc"
domain_name = "max00217.pythonanywhere.com"

response = requests.post(
    f"https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/",
    headers={"authorization": "Token {token}".format(token=api_token)}
)
if response.status_code == 200:
    print("reloaded OK (Code: {})".format(response.status_code))
else:
    print("Got unexpected status code {}: {!r}".format(response.status_code, response.content))