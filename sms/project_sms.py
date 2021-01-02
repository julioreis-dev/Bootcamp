import requests
from twilio.rest import Client

# Twilio autentication
account_sid = 'AC20331eaa7a6b923fe7208daf2d1848d0'
auth_token = '679a45d175b6148e327f5ca2bd98c624'

# Openweather endpoint
end_point = 'https://api.openweathermap.org/data/2.5/onecall'
weather = {
    'lat': -22.803850,
    'lon': -43.372631,
    'appid': 'ad87b8a03735d2aa78d2d90359a80162',
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
