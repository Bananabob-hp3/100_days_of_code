import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 29.594
MY_LONG = 79.302

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "tzid": "Asia/Kolkata",
    "formatted": 0
}

def is_night():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()


    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

MY_EMAIL = "harahitpant999@gmail.com"
MY_PASSWORD = "rqeciymoxgkdvuen"

while True:
    time.sleep(60)
    if is_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:ISS Alert!\n\nLook up! ISS is above you!"
            )
            print("Email sent!")














#starttls() → encrypts the connection 🔒
#Use App Password not your real Gmail password
#\n\n separates subject from body
 #checks every 60 second













