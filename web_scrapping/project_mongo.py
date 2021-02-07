from pymongo import MongoClient, errors


def insert_one(*args):
    return_id = None
    try:
        client = MongoClient('localhost', 27017)
        bd = client['test_campeonato']
        album = bd['myresultados']
        results = args[0]
        return_id = album.insert_one(results)
    except errors.DuplicateKeyError:
        pass
    finally:
        return return_id


def contents_bd(myquery):
    client = MongoClient('localhost', 27017)
    bd = client['test_campeonato']
    album = bd['myresultados']
    # myquery = {'resultado': '-'}
    draw = album.find(myquery)
    return draw


def find_one(id_game):
    client = MongoClient('localhost', 27017)
    bd = client['test_campeonato']
    album = bd['myresultados']
    myquery = {'_id': id_game}
    content = album.find_one(myquery)
    return content


def drop_collection():
    client = MongoClient('localhost', 27017)
    bd = client['test_campeonato']
    album = bd['myresultados']
    album.drop()


def last():
    client = MongoClient('localhost', 27017)
    bd = client['test_campeonato']
    album = bd['myresultados']
    x = album.find().sort([("_id", -1)]).limit(1)
    return x


def delete_data(myquery):
    client = MongoClient('localhost', 27017)
    bd = client['test_campeonato']
    album = bd['myresultados']
    # myquery = {'_id': 328}
    album.delete_one(myquery)

# delete_data()
# y = last()
# for n in y:
#     print(n)
# drop_collection()
# x = find_one(335)
# print(x)
# if x['placar'] == [1, 1]:
#     print(True)
# else:
#     print(False)
# k = contents_bd({})
# for w in k:
#     print(w)
