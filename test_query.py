import json
import time
import requests
from datetime import datetime
from pathlib import Path

url = "https://ridmvreservations.ri.gov/WebAPI/reservation/slots?visitTypeId=20"

response = requests.get(url)
response.raise_for_status()

data = response.json()

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

now = time.time()
recent = any(now - f.stat().st_mtime < 60 for f in DATA_DIR.glob("*.json"))

if not recent:
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    (DATA_DIR / f"{timestamp}.json").write_text(json.dumps(data, indent=2))
    print(f"Saved {timestamp}.json")
else:
    print("Skipped save: file already saved in the last minute")

def parse_slot(slot):
    date_time = datetime.fromisoformat(slot["scheduleDate"].replace("T00:00:00", "T") + slot["startTime"])
    return {**slot, "date_time": date_time}

slots = [parse_slot(s) for s in data["reservationSlots"]]

cranston_available = [s for s in slots if s["location"] == "Cranston" and s["availableSlotCount"] > 0]
earliest = min(cranston_available, key=lambda s: s["date_time"])
print(earliest)
