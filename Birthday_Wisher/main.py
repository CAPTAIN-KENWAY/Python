##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import random
import smtplib
import datetime as dt

data = pandas.read_csv("./birthdays.csv")
data_list = data.to_dict(orient="records")

now = dt.datetime.now()
todays_day = now.day
todays_month = now.month

my_email = "pythontesting810@gmail.com"
my_password = "jflzmvkrbbuhavxz"


def send_mail(name, email):
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as file:
        data = file.read()
        data = data.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday\n\n{data}"
        )


for i in data_list:
    if i["day"] == todays_day and i["month"] == todays_month:
        send_mail(i["name"], i["email"])
