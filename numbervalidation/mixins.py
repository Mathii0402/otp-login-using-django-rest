from http import client
from django.conf import settings
from twilio.rest import Client
import random,os


class meshandler:
    mob_number =None
    otp =None

    def __init__(self,mob_number,otp) -> None:
        self.mob_number = mob_number
        self.otp = otp 
    

    def send_otp_on_mob(self):
      account_sid = ""
      auth_token = ""
      client = Client(account_sid, auth_token)

      message = client.messages.create(
        body=f"Your otp is {self.otp}",
        to=self.mob_number, 
        from_="+15184127632" 
    
      )
