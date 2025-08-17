import smtplib
import requests
from datetime import datetime
import time

MY_LAT = 12.879721
MY_LNG = 121.774017

my_email = "sample@gmail.com"
password = "samplepassword"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

def iss_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (iss_latitude - 5 <= parameters["lat"] <= iss_latitude + 5) and (iss_longitude - 5 <= parameters["lat"] <= iss_longitude + 5):
        return True
#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if iss_over_head() and is_night():
         with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()  # encrypted for people trying to tap into the email
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="sample@edu.ph",
                    msg=f"Subject: The ISS is near you!")

