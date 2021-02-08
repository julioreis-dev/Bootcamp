from pymongo import MongoClient, errors
from bs4 import BeautifulSoup
from threading import Lock, Thread
import requests


# import time


class TableGames:
    def __init__(self):
        self.lock = Lock()

    @staticmethod
    def games(home, visitor, result, rod):
        list_game = []
        for index in range(0, len(visitor)):
            score_game = result[index].getText().split()
            if len(score_game) != 1:
                final_score = (int(score_game[0]), int(score_game[2]))
            else:
                final_score = ('-', '-')
            id_game = str(rod) + str(index)
            game = (int(id_game), home[index + 1].getText(), visitor[index].getText(), final_score, rod)
            list_game.append(game)
        return list_game

    def site(self, pag):
        # self.lock.acquire()
        new_url = f'https://www.api-futebol.com.br/campeonato/campeonato-brasileiro/2020/rodada/{pag}'
        new_response = requests.get(new_url)
        new_page = new_response.text
        new_soup = BeautifulSoup(new_page, 'html.parser')
        right = new_soup.find_all(name='div', class_='text-right')
        left = new_soup.find_all(name='div', class_='text-left')
        score = new_soup.find_all(name='div', class_='small text-center')
        values = self.games(right, left, score, pag)
        informations = self.prepare_dict(values)
        insert_game(informations)
        # self.lock.release()

    @staticmethod
    def prepare_dict(datas):
        list_result = []
        for data in datas:
            dict_data = {
                '_id': data[0],
                'mandante': data[1],
                'visitante': data[2],
                'score': data[3],
                'rodada': data[4],
            }
            if dict_data['score'][0] > dict_data['score'][1]:
                dict_data['resultado'] = dict_data['mandante']
            elif dict_data['score'][0] < dict_data['score'][1]:
                dict_data['resultado'] = dict_data['visitante']
            elif dict_data['score'] == ('-', '-'):
                dict_data['resultado'] = '-'
            else:
                dict_data['resultado'] = 'empate'
            list_result.append(dict_data)
        return list_result


def insert_game(*args):
    results = args[0]
    for result in results:
        try:
            client = MongoClient('localhost', 27017)
            bd = client['test_campeonato']
            album = bd['tabela_resultados']
            return_id = album.insert_one(result)
            print(return_id)
        except errors.DuplicateKeyError:
            pass


def contents_bd(myquery):
    client = MongoClient('localhost', 27017)
    bd = client['test_campeonato']
    album = bd['tabela_resultados']
    # myquery = {'resultado': '-'}
    draw = album.find_one(myquery)
    return draw


def missedgames(myquery):
    client = MongoClient('localhost', 27017)
    bd = client['test_campeonato']
    album = bd['tabela_resultados']
    # myquery = {'resultado': '-'}
    draw = album.find(myquery).sort([('_id', 1)])
    return draw


def drop_collection():
    client = MongoClient('localhost', 27017)
    bd = client['test_campeonato']
    album = bd['tabela_resultados']
    album.drop()


# drop_collection()
# list_content = contents_bd({})
# for n in list_content:
#     print(n)

def main():
    list_content = contents_bd({})
    if list_content is None:
        url = 'https://www.api-futebol.com.br/campeonato/campeonato-brasileiro/2020'
        response = requests.get(url)
        web_page = response.text
        soup = BeautifulSoup(web_page, 'html.parser')
        rodada = soup.find(name='h6', class_='mb-0 mt-1')
        number = rodada.getText().split()

        soccer = TableGames()
        for page in range(1, int(number[1]) + 1):
            # soccer.site(page)
            urls = Thread(target=soccer.site, args=(page,))
            urls.start()
    else:
        list_missedgames = missedgames({'resultado': '-'})
        for n in list_missedgames:
            print(n)


if __name__ == '__main__':
    main()
