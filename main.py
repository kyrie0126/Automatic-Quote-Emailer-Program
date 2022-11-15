import smtplib
import datetime as dt
from random import choice

# -------------- Retrieve data ---------------------
with open("quotes.txt") as file:
    quotes = file.readlines()

# --------------- Datetime -------------------
now = dt.datetime.now()
day_of_the_week = now.weekday()

# ----------------- Email Function ---------------------
# SMTP addresses:
# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com

# modify these to fit your scenario!
sender_email = "sender_email_address"
sender_password = "app_specific_password"
smtp_code = "smtp.gmail.com"  # change accordingly based on email provider
recipient_email = "recipient_email"


def send_email(message):
    with smtplib.SMTP_SSL(smtp_code, 465) as connection:
        connection.login(sender_email, sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=f"Motivational Quote\n\n{message}"
        )


# ---------------- Message Sent -----------------------
# send motivational quote if day == Tuesday (1)
# change the day of the week to your preference
if day_of_the_week == 1:
    random_quote = choice(quotes)
    send_email(random_quote)

