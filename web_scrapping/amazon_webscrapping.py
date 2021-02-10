from bs4 import BeautifulSoup
import requests
import smtplib
import datetime as dt
import random

def email_recomendation(price):
    my_email = 'jrfirmino01@gmail.com'
    my_password = 'Manuela01*'
    now = dt.datetime.now()
    weekday = now.weekday()
    with smtplib.SMTP('smtp.gmail.com', 587) as conection:
        conection.starttls()
        conection.login(my_email, my_password)
        conection.sendmail(from_addr=my_email,
                           to_addrs='juliofirminoreis@hotmail.com',
                           msg=f'Subject:[URGENTE] Alerta de Preco\n\nJulio,\nO preco do produto caiu para R${price}, o valor '
                               f'esta abaixo do preco estipulado de R$350,35.'
                           )

url = 'https://www.amazon.com.br/Panela-El%C3%A9trica-Press%C3%A3o-Midea-Prata/dp/B0778VCKX4/ref=sr_1_6?__mk_pt_' \
      'BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=325B4LY6SM6UM&dchild=1&keywords=panela+de+pressao&qid=1612822864&sprefix=panela%2Caps%2C306&sr=8-6'
params_amazon = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    "Accept-Language":'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
}

response = requests.get(url=url, headers=params_amazon)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())
price = soup.find(name='span', class_='a-size-medium a-color-price priceBlockBuyingPriceString').getText()
number = price.split('$')[1]
number_float = float(number.replace(',', '.'))
if number_float < 550.35:
    email_recomendation(number_float)
    print('Email encaminhado!!!')
else:
    print(number_float)
