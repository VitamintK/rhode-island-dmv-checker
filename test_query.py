import json
import requests

url = "https://ridmvreservations.ri.gov/WebAPI/reservation/slots?visitTypeId=20"

response = requests.get(url)
response.raise_for_status()

try:
    data = response.json()
    print(json.dumps(data, indent=2))
except ValueError:
    print(response.text)
