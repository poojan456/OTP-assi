#Importing requires libraries
import smtplib
import random
from twilio.rest import Client



#Sender's Email and Password
senders_mail = 'pooja1713953@gmail.com'
senders_password = 'kaxwlziuipezhgih'

#Sender's Mobile
account_sid = 'ACb5baf5f93fe0d1ec919cae3a2d66bf41'
auth_token = 'a5206483ad0d5cfaf854a97372f9c63e'
client = Client(account_sid, auth_token)
twilio_num = '+17027238962'

#Function to generate OTP
def generateOtp():
    otp = random.randint(100000, 999999)
    return otp

#Function to validate Email
def validateEmailID(receiver_mail):
    if "@" not in receiver_mail or "." not in receiver_mail:
        return False
    return True

#Function to validate mobile
def validateMobile(mobile):
    return len(mobile) == 10 and mobile.isdigit()

# Send OTP over mobile using Twilio
def sendOTPOverMobile(target, otp):
    if(validateMobile(target)):
        target = "+91" + str(target)
        message = client.messages.create(
            body = "Your OTP is " + str(otp) ,
            from_= twilio_num,
            to=target
        )
        print("OTP Sent to "+str(target)+" successfully")
    else:
        print("Enter valid mobile number!!")

# Send OTP over email
def sendOTPOverEmail(receiver_mail, otp):
    message = 'Your otp is '+str(otp)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senders_mail, senders_password)
    server.sendmail(senders_mail, receiver_mail, message)
    server.quit()
    print("OTP sent sucessfully on ", receiver_mail)

#Main code
otp = generateOtp() #generating Otp

#Sending OTP over Email
print("\nSending OTP via Email")
receiver_mail  = input("Enter your Email: ")  #input user email
if(validateEmailID(receiver_mail)):
    sendOTPOverEmail(receiver_mail, otp)
else:
    print("Please Enter valid mail!!")

#Sending OTP over SMS
print("\nSending OTP via SMS")
target = input("Enter Mobile number: ")
sendOTPOverMobile(target, otp)