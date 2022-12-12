import smtplib
import random
import datetime as dt

my_email = "pythontesting810@gmail.com"
my_password = "jflzmvkrbbuhavxz"

with open("./quotes.txt") as file:
    data = file.read()
    quotes = data.split("\n")

message = random.choice(quotes)

now = dt.datetime.now()
if now.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="shivamsaini948@gmail.com",
            msg=f"Subject:Hello, This is your quote for the day\n\n{message}"
        )
