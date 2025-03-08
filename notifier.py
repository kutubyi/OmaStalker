import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
from config import RESERVATION_URL  

load_dotenv()  # Load credentials from .env file

def send_email_notification():
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    recipient_email = os.getenv("EMAIL_RECIPIENT")

    subject = "Reservation Available Notification"
    body = f"A reservation slot at {RESERVATION_URL} is now available."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
