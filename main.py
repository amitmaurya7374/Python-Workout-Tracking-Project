"""In this Project we will learn about apis and how to fetch,post,put,delete methods.
we are using nutritionix api for workout tracking.

"""
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
