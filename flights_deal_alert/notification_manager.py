from twilio.rest import Client

TWILIO_SID = "your twilio sid"
TWILIO_AUTH_TOKEN = "your twilio auth token"
TWILIO_VIRTUAL_NUMBER = "your twilio phone number"
TWILIO_VERIFIED_NUMBER = "your verified phone number in twilio"


class NotificationManager:
    '''This class is responsible for sending notifications with the deal flight details.'''

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        # Prints if sucessfully sent
        print(message.sid)