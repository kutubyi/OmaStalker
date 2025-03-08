# OmaStalker

This project automates reservation monitoring for high-demand restaurants (e.g., Sugita—the mythical sushi spot that never has openings, doesn’t send notifications for canceled slots, and haunts my dreams. I built this in the hope that I might actually get to try it before I die 😢) on [omakase.in](https://omakase.in).  

It checks availability at preset intervals and sends an email notification when a reservation becomes available.

## Usage
### 1. Install dependencies:
```bash
pip install -r requirements.txt
```
### 2. Create a .env file with your email credentials:
⚠️ For Gmail, enable App Passwords ([Guide](https://support.google.com/mail/answer/185833?hl=en)).
```bash
EMAIL_SENDER=sender@gmail.com
EMAIL_PASSWORD=app_password
EMAIL_RECIPIENT=example@email.com
```
### 3. Edit ```config.py``` and replace with the restaurant’s reservation link:
```bash
RESERVATION_URL = "https://omakase.in/restaurant_id"
```
### 4. Run the script:
```bash
python main.py
```
