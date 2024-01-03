from twilio.rest import Client

TWILIO_SID = "SCAC35908559e4b634d2c2eb2339747e67f8324"
TWILIO_AUTH_TOKEN = "mnbc650a0f79c5b3b47551fcb1a26537d250"
TWILIO_VIRTUAL_NUMBER = "+17700142440"
TWILIO_VERIFIED_NUMBER = "+2347597044364"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
