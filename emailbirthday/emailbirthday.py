import smtplib
import datetime as dt
import random
import pandas as pd


my_email = 'jrfirmino01@gmail.com'
my_password = 'My_password'

now = dt.datetime.now()
tuplebirth = (now.month, now.day)

data = pd.read_csv('Solution+-+birthday-wisher-end/birthdays.csv')
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

if tuplebirth in birthdays_dict:
    birth_name = birthdays_dict[tuplebirth]
    file_path = f'Solution+-+birthday-wisher-end/letter_templates/letter_{random.randint(1,3)}.txt'

    with open(file_path, encoding='utf8') as content:
        contents = content.read()
        contents = contents.replace("[NAME]", birth_name['name'])

    with smtplib.SMTP('smtp.gmail.com', 587) as conection:
        conection.starttls()
        conection.login(my_email, my_password)
        conection.sendmail(from_addr=my_email,
                           to_addrs='juliofirminoreis@hotmail.com',
                           msg=f'Subject:Feliz aniversario!!!\n\n{contents}')
