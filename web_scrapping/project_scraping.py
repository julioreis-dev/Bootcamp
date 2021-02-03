from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name='a', class_='storylink')
list_article_text = []
list_article_link = []
for article_tag in articles:
    text = article_tag.getText()
    list_article_text.append(text)
    link = article_tag.get('href')
    list_article_link.append(link)
article_score = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
# article_score = soup.find(name='span', class_='score')
# print(article_score)
largest_number = max(article_score)
largest_index = article_score.index(largest_number)
print(list_article_text[largest_index])
print(list_article_link[largest_index])
print(article_score[largest_index])