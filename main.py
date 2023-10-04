import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# YOUR INFO
SEX = os.getenv("SEX")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

# Describe Workout
TODAYS_WORKOUT = "Lifted weights for 2 hours"


# Nutritionix API INFO
load_dotenv(".env")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

HEADERS_N = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

params = {
    "query": TODAYS_WORKOUT,
    "gender": SEX,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# Make req to Nutritionix and get res
nutritionix_res = requests.post(url=API_ENDPOINT, headers=HEADERS_N, json=params)
nutritionix_res.raise_for_status()

data = nutritionix_res.json()["exercises"][0]

# Get workout entry time and date
today = datetime.now()
time = today.strftime("%X")
date = today.strftime("%b %d, %Y")

# Save data from Nutritionix res in a dict, ready to send to Sheety API
workout = {
    "exercise": data["name"].title(),
    "duration": data["duration_min"],
    "calories": data["nf_calories"],
    "time": time,
    "date": date,
}

# Sheety API INFO
SHEETY_ENDPOINT = "https://api.sheety.co/8aa11738f65c35963040478cb15014cf/pythonWorkoutsProject/workouts"
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

HEADERS_S = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json",
}

body = {
    "workout": workout,
}

# Write to Google sheets using Sheety API
sheety_res = requests.post(url=SHEETY_ENDPOINT, headers=HEADERS_S, json=body)
sheety_res.raise_for_status()


