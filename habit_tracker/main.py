import requests
from datetime import datetime

USERNAME = "your username"
TOKEN = "your token"
GRAPH_ID = "your graph id"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create an account in Pixe.la
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create a graph in Pixe.la
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))
distance_km = 1.1 # amount of km as a float ex: 1.1"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": f"{distance_km}",
}

# Add a pixel to your graph in Pixe.la
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)
