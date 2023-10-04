import requests
import os
from dotenv import load_dotenv

# API INFO
load_dotenv(".env")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# YOUR INFO
SEX = os.getenv("SEX")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

# Describe Workout
TODAYS_WORKOUT = "Lifted weights for 2 hours"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

params = {
    "query": TODAYS_WORKOUT,
    "gender": SEX,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

res = requests.post(url=API_ENDPOINT, headers=HEADERS, json=params)
res.raise_for_status()

data = res.json()
print(data)


