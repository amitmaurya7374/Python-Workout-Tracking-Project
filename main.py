"""In this Project we will learn about apis and how to fetch,post,put,delete methods.
we are using nutritionix api for workout tracking.

"""
from datetime import datetime

import requests

from keys import Keys

keys = Keys()
app_id = keys.appId
api_key = keys.apikey

exercise_text = input("Tell me which exercises you did: ")
api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
google_sheet_endpoint = "https://api.sheety.co/314fb9cdff3bcd4af866b869420d561c/myWorkouts/workouts"

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}
sheet_header = {
    "Authorization": keys.auth
}
parameters = {
    "weight_kg": 80,
    "height_cm": 162.56,
    "gender": "male",
    "age": 24,
    "query": exercise_text,
}
response = requests.post(url=api_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(result)
# name,nf_calories,duration_min,date,time column sheets
# test_data = [{'tag_id': 317, 'user_input': 'run', 'duration_min': 31.08, 'met': 9.8, 'nf_calories': 406.11,
#               'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg',
#                         'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg',
#                         'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None,
#               'benefits': None},
#              {'tag_id': 100, 'user_input': 'walked', 'duration_min': 37.28, 'met': 3.5, 'nf_calories': 173.97,
#               'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_highres.jpg',
#                         'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_thumb.jpg',
#                         'is_user_uploaded': False}, 'compendium_code': 17190, 'name': 'walking', 'description': None,
#               'benefits': None}]

# extracting data from nutrition api
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(google_sheet_endpoint, json=sheet_inputs,headers=sheet_header)

    print(sheet_response.text)
