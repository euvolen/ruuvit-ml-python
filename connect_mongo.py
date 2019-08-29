from pymongo import MongoClient
from config import url

def get_all_users():
    with MongoClient(url) as client:
        users = list(client.get_database()['users'].find())
    return users

def get_collection_by_name(name):
    with MongoClient(url) as client:
        data = list(client.get_database()[name].find())
    return data


def update_db(name, data= 'Volen', id=None):
    updated = f'Volen {data}'
    if id:
        with MongoClient(url) as client:
            client.get_database()[name].update_many({'patient': id}, {'$set': {data}})
        return
    else:
        with MongoClient(url) as client:
            users = client.get_database()[name].update_many({'firstname':'Evgenii'}, {'$set': {'lastname': updated}})
        return users

