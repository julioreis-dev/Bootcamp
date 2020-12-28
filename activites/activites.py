import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN = 'oCc2OdZg2jjrMu'
USERNAME = 'jrfirmino'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_params = {
    'id': 'manu1',
    'name': 'Exercise',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}
headers = {'X-USER-TOKEN': TOKEN}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_endpoint = f'{graph_endpoint}/manu1'
today = datetime(year=2020, month=12, day=24)
pixel_params ={
    'date': today.strftime('%Y%m%d'),
    'quantity': '10',
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
