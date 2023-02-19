# from twilio.rest import Client
# import os
# # Your Account SID from twilio.com/console
# account_sid = "ACc6daa3259b94d95025224582c7ebb9fc"
# # Your Auth Token from twilio.com/console
# auth_token  = "chMBEyQ7jSWpbh77qlHPCZ9BUrl9oTVs"

# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     to="+916384089068", 
#     from_="+916384089068",
#     body="Hello from Python!")

# print(message.sid)
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACc6daa3259b94d95025224582c7ebb9fc"
auth_token = "8064f66981bb32cf745ff602c3e28e13"
verify_sid = "VA2ac55094e4acc285d771277ad4238689"
verified_number = "+916384089068"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)