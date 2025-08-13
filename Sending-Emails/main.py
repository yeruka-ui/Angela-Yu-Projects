import datetime as dt
import os
import random
import smtplib
import csv

my_email = "sample@gmail.com"
password = "samplepassword"

now = dt.datetime.now()
month = now.month
day = now.day

with open("birthdays.csv", "r", encoding= "utf-8") as f:
    b_file = csv.reader(f)

    for row in b_file:
        # Skip empty or incomplete rows
        if len(row) < 5:
            continue

        b_month = int(row[-2])
        b_day = int(row[-1])
        name = row[0]

        if month == b_month and day == b_day:
            random_letter = random.choice(os.listdir("letter_templates")) #chooses a random letter
            letter_path = os.path.join("letter_templates", random_letter) #path to the random letter

            with open(letter_path, "r") as rand_letter:
                content = rand_letter.read()
            updated_content = content.replace("[NAME]", name).strip()

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()  # encrypted for people trying to tap into the email
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="sample@edu.ph",
                    msg=f"Subject: Happy birthday!\n\n{updated_content}")

