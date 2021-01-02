import requests
from twilio.rest import Client

# Twilio autentication
account_sid = 'my_account_sid'
auth_token = 'my_token'

# Openweather endpoint
end_point = 'https://api.openweathermap.org/data/2.5/onecall'
weather = {
    'lat': -22.803850,
    'lon': -43.372631,
    'appid': 'My_appid',
    'exclude': 'current,minutely,daily',
}

flag = False
response = requests.get(url=end_point, params=weather)
response.raise_for_status()
weathear_json = response.json()
weather_condition = weathear_json['hourly'][0:12]
for hour_data in weather_condition:
    result_condition = hour_data['weather'][0]['id']
    if result_condition < 700:
        flag = True

if flag:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="Alerta: Cuidado!!!. Se você precisar sair de casa leve guarda chuva. As "
                                          "ultimas 12 horas tivemos registro de previsão de chuva para a sua região.",
                                     from_='+19548073107',
                                     to='+5521980379545')
    print(message.status)
    print('SMS, enviado com sucesso!!!')
else:
    print('Finalizando aplicação')
