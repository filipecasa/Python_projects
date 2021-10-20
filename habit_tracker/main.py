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

today = datetime.now().strftime("%Y%m%d")
# print(today.strftime("%Y%m%d"))
distance_km = 1.1 # amount of km as a float ex: 1.1"

pixel_config = {
    "date": today,
    "quantity": input("How many kilometers did you cycle today?: "),
}

# Add a pixel to your graph in Pixe.la
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

date_to_update = today
new_distance_km = "km to be updated"

update_pixel_endpoint = f"{pixel_endpoint}/{date_to_update}"

update_pixel_config = {
    "quantity": f"{new_distance_km}",
}

# Update a pixel
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

date_to_delete = "date of pixel to be deleted"

delete_pixel_endpoint = f"{pixel_endpoint}/{date_to_delete}"

# Delete a pixel
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)