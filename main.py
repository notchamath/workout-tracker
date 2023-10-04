import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

params = {
    "query": "Lifted weights for 2 hours"
}

res = requests.post(url=API_ENDPOINT, headers=HEADERS, json=params)
res.raise_for_status()

data = res.json()
print(data)


