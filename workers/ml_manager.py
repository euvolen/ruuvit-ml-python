
from connect_mongo import get_all_users, update_db
from ml_mutation import mutate_data

started = True
data = None

def start_worker():
    global started
    started = True
    return started


def stop_worker():
    global started
    started = False
    return started

def get_data(sleeper):
    count = 0
    while started:
        global data
        data = get_all_users()
        #TODO ML alghorithm
        mutated = mutate_data(data)
        update_db('users', str(count))
        count +=1
        sleeper.sleep(30)