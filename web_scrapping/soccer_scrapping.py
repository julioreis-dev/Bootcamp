from bs4 import BeautifulSoup
import requests
import project_mongo as mg


def results_score(result_games):
    list_result = []
    score_game = []
    for score in result_games:
        try:
            placar_score = int(score.getText())
            if len(score_game) == 1:
                score_game.append(placar_score)
                list_result.append(score_game)
                score_game = []
            else:
                score_game.append(placar_score)
        except ValueError:
            placar_score = '-'
            if len(score_game) == 1:
                score_game.append(placar_score)
                list_result.append(score_game)
                score_game = []
            else:
                score_game.append(placar_score)
    return list_result


def list_games(hom, awa):
    list_game = []
    flag = True
    n = 0
    while flag:
        left = hom[n]
        right = awa[n]
        game = (left.getText(), right.getText())
        list_game.append(game)
        n += 1
        if n == len(home):
            flag = False
    return list_game


def connectar_bd():
    for index in range(0, len(all_scores)):
        final_result = {
            '_id': index + 1,
            'mandante': all_games[index][0],
            'visitante': all_games[index][1],
            'placar': all_scores[index],
            'resultado': '-',
        }

        if final_result['placar'][0] > final_result['placar'][1]:
            final_result['resultado'] = final_result['mandante']
        elif final_result['placar'][0] < final_result['placar'][1]:
            final_result['resultado'] = final_result['visitante']
        elif final_result['placar'] == ['-', '-']:
            pass
        else:
            final_result['resultado'] = 'empate'
        content = mg.find_one(final_result['_id'])
        if content is not None:
            consult_bd(final_result, content)
        else:
            mg.insert_one(final_result)
            print(f'Resultado do jogo de id {final_result["_id"]} entre '
                  f'{final_result["mandante"]} X {final_result["visitante"]} foi inserido no banco de dados '
                  f'com sucesso!!!')


def consult_bd(final, cont):
    if final == cont:
        print(f'Resultado de id {cont["_id"]} já foi inserido anteriormente!!!')
    else:
        mg.delete_data({'_id': final["_id"]})
        mg.insert_one(final)
        print(f'Resultado do jogo de id {final["_id"]} entre {final["mandante"]} X {final["visitante"]} '
              f'foi atualizado com sucesso!!!')


if __name__ == '__main__':
    url = 'https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/'
    response = requests.get(url)
    web_page = response.text
    soup = BeautifulSoup(web_page, 'html.parser')
    home = soup.find_all(name='abbr', class_='team-abbr team-abbr-home')
    away = soup.find_all(name='abbr', class_='team-abbr team-abbr-away')
    score_games_site = soup.find_all(name='div', class_='team-score')
    all_scores = results_score(score_games_site)
    all_games = list_games(home, away)
    connectar_bd()
