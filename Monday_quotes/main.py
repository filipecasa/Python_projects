import smtplib
import datetime as dt
import random


MY_EMAIL = "your email"
MY_PASSWORD = "your password"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.mail.yahoo.com or smtp.google.com or from the email you want") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )







