import os
from twilio.rest import Client
from twilio.rest.api.v2010.account import message

account_sid='ACa0f6570074381e69f07c5e8a74bdd32b'
auth_token='083c83191a98ae7890e290d57f4710b5'

client=Client(account_sid,auth_token)

def send_sms(user_code,phone_number):
    message=client.messages.create(
        body= f'Hi your verification code is {user_code}',
        messaging_service_sid='MG97ce71b6088f63f592908214dfd5a5a5',
        to=f'{phone_number}'
    )
    print(message.sid)