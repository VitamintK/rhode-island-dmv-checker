import requests
from datetime import datetime

url = "https://ridmvreservations.ri.gov/WebAPI/reservation/slots?visitTypeId=20"

response = requests.get(url)
response.raise_for_status()

data = response.json()

def parse_slot(slot):
    date_time = datetime.fromisoformat(slot["scheduleDate"].replace("T00:00:00", "T") + slot["startTime"])
    return {**slot, "date_time": date_time}

slots = [parse_slot(s) for s in data["reservationSlots"]]

for slot in slots:
    print(slot)
