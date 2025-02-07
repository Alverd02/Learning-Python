import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
# the number we get at the response is the HTTP status code i.e. 404(not found), 200(OK), 500(internal server error)

response.raise_for_status() #From the documentation,  it will tell the meaning of  every status code that is not successful

data = response.json() #json files are nothing more that dictionaries
print(data)
print(data["iss_position"])
iss_position = (data["iss_position"]["latitude"],data["iss_position"]["longitude"])
print(iss_position)