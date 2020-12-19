from twilio.rest import Client
import requests

# todo 1 - acessar a biblioteca request
# ENDPOINT
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'http://newsapi.org/v2/everything'

# API_KEY
ALPHA_API_KEY = ''
NEWS_API_KEY = ''
ASSET = 'TSLA'

# Twilio autentication
account_sid = ''
auth_token = '679a45d175b6148e327f5ca2bd98c624'

# todo 2 - acessar os parametros
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': ASSET,
    'apikey': ALPHA_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

# todo 3 - extrair do json as informações relativo ao ativo
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_closing = data_list[0]['4. close']
day_before_yesterday_closing = data_list[1]['4. close']
dif = float(yesterday_closing) - float(day_before_yesterday_closing)
dif_flag = None
if dif > 0:
    dif_flag = '🔺'
else:
    dif_flag = '🔻'

# todo 4 - estabelecer os critérios de interesse
percentual = round(abs((dif * 100) / float(yesterday_closing)), 2)
if percentual > 0.1:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': ASSET,
        # 'language':'pt',
    }
    response_news = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response_news.raise_for_status()
    principal_news = response_news.json()['articles'][0:3]
    formated = [f'{ASSET} - {dif_flag}{percentual}% - Título:{material["title"]}.' for material in principal_news]
    # formated = [f'título:{material["title"]}.\nconteudo:{material["description"]}' for material in principal_news]

# todo 5 - Enviar SMS para o cliente
    client = Client(account_sid, auth_token)
    for sms in formated:
        message = client.messages.create(body=sms,
                                         from_='+19548073107',
                                         to='+5521980379545')
        print(message.status)
        print('SMS, enviado com sucesso!!!')
else:
    print(percentual)
