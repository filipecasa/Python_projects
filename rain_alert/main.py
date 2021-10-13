import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "your api key from openweathermap.org"

account_sid = "your account sid from openweathermap.org"
auth_token = "your auth token from openweathermap.org"

weather_params = {
    "lat": "latitude you want as integer",
    "lon": "longitude you want as integer",
    "exclude": "current,minutely,daily",#this way you are getting the weather hourly#
    "appid": api_key
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    # print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700: # numbers bellow 700 mean the forecasts are raining related
        will_rain = True

if will_rain:
    # print("Bring an umbrella!")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, bring an umbrella. ☂☔",
        from_='your phone number from Twilio',
        to='the phone you want to send the message'
    )
    print(message.status)
#
# option on how to do from Twilio page 

# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client
#
#
# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+15017122661',
#                      to='+15558675310'
#                  )
#
# print(message.sid)