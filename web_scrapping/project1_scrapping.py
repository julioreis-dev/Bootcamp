from bs4 import BeautifulSoup
import requests

url = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(url)
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')
movies = soup.find_all(name='h3', class_='title')
movies_titles = [movie.getText() for movie in movies]
movies_titles.reverse()
with open('movies.csv', mode='w', encoding="utf-8") as file:
    for movie_title in movies_titles:
        file.write(f'{movie_title}\n')
