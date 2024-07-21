import requests
import os
import datetime
USER_INP = input("Tell me which exercise you did?: ")
APP_ID = ""  ##Your APP id goes here#
APP_KEY = ""  #your APP key goes here#
API_SITE = ""  #your API site goes here#
SHEETY_API = ""  #your SHeety API goes here#
PARAM = {
    "query": USER_INP,
}
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
EXER_SITE = f"{API_SITE}/v2/natural/exercise"

response = requests.post(url=EXER_SITE, json= PARAM, headers=HEADERS)
data = response.json()
date = datetime.datetime.now()
exact_date = date.strftime("%d/%m/%Y")
time = date.time()
exact_time = time.strftime("%X")
for result in data["exercises"]:
    PARAM2 = {
        "workout": {
            "date": exact_date,
            "time": exact_time,
            "exercise": result["name"].title(),
            "duration": result["duration_min"],
            "calories": result["nf_calories"],
        }
    }
    response2 = requests.post(url=SHEETY_API, json=PARAM2)
    print("Your data has been uploaded")
