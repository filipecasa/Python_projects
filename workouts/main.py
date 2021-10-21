import requests
from datetime import datetime
import os

GENDER = "your gender"
WEIGHT_KG = "your weight as integer"
HEIGHT_KG = "your height as integer"
AGE = "your age as integer"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("API_KEY")
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_KG,
    "age": AGE
}

# Get the amount of calories and exercise_type from Nutritionix
response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")
exercise_type = result["exercises"][0]["name"].title()
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

sheet_inputs = {
    "workout": {
        "date": today,
        "time": time_now,
        "exercise": exercise_type,
        "duration": duration,
        "calories": calories
    }
}
print(sheet_inputs)

bearer_headers = {
    "Authorization": f"Bearer {os.environ.get('BEARER_TOKEN')}",
    "Content-Type": "application/json",
}

sheety_endpoint = "your api url from Sheety"

# Add a row to your sheet
sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=bearer_headers)

print(sheet_response.text)


