import requests
from datetime import datetime
import os

nutritionix_endpoint = os.environ['NT_nutritionix_endpoint']
nutritionix_exercise = os.environ['NT_nutritionix_exercise']
APP_ID = os.environ['NT_APP_ID']
API_KEY = os.environ['NT_API_KEY']

adress = f'{nutritionix_endpoint}/{nutritionix_exercise}'
GENDER = 'male'
WEIGHT_KG = 84
HEIGHT_CM = 169.03
AGE = 40

headers = { "x-app-id": APP_ID, "x-app-key": API_KEY,}
exercise_text = input("Tell me which exercises you did: ")

nutritionix_params = {
     "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=adress, json=nutritionix_params, headers=headers)
result = response.json()


sheety_endpoint = os.environ['NT_sheety_endpoint']
today = datetime.now()
date = today.strftime('%d/%m/%Y')
schedule = today.strftime('%X')
headers_sheety = {"Authorization": os.environ['NT_Authorization']}
for n in range(len(result['exercises'])):
    sheets_params = {
        "workout": {
            "date": date,
            "time": schedule,
            "exercise": result['exercises'][n]['name'].title(),
            "duration": result['exercises'][n]['duration_min'],
            "calories": result['exercises'][n]['nf_calories']
        }
    }
    sheet_response = requests.post(sheety_endpoint, json=sheets_params, headers=headers_sheety)
    print(sheet_response.json())
