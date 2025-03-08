import requests
from bs4 import BeautifulSoup

def check_availability(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Check for the reservation button
    reservation_button = soup.select_one('.ui.button.primary.big.fluid')

    if reservation_button:
        print("✅ Reservation available!")
        return True
    else:
        print("❌ No available slots.")
        return False
