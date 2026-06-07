import os
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token) 

    def send_sms(self, cheapest):
        self.message = self.client.messages \
            .create(
             body=f"Alert! Flight from {cheapest.origin_airport} to {cheapest.destination_airport} was never been this cheap before! at just {cheapest.price}",
             from_=os.environ.get("twilio_number"),
             to=os.environ.get("phone_number")
        ),

