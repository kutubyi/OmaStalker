import time
from datetime import datetime
from scraper import check_availability
from notifier import send_email_notification
from config import RESERVATION_URL

CHECK_INTERVAL = 300  # Check every 5 minutes

if __name__ == "__main__":
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        print(f"[{now}] Checking for available reservations...")

        if check_availability(RESERVATION_URL):
            print(f"[{now}] Reservation available! Sending email notification...")
            send_email_notification()
            print(f"[{now}] Email notification sent successfully.")
            break  
        
        print(f"[{now}] No available slots. Retrying in {CHECK_INTERVAL // 60} minutes...")
        time.sleep(CHECK_INTERVAL)
