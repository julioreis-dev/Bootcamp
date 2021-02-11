from bs4 import BeautifulSoup
import requests
# import lxml

with open('curriculo.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.p)
# print(soup.li)
anchor_tags = soup.find_all(name='a')
heading = soup.find(name='h1', class_='format')
heading1 = soup.find(name='h1', id='name')
# print(heading1.getText())
# print(heading.getText())
# company = soup.select_one(selector='b a')
company = soup.select_one(selector='.format')
print(company)
for tag in anchor_tags:
    # print(tag.getText())
    # print(tag.get('href'))
    pass

left = soup.find_all(name='img', class_='icon escudo x45 pull-left')
list_mandante = [team_host['title'] for team_host in right]
list_visitor = [team_visitor['title'] for team_visitor in left]

