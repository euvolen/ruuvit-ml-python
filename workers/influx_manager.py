from connect_influx import get_userdata, erase_db
from threading import Thread
from connect_mongo import get_all_users, update_db
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

def influx_to_mongo_loop(sleeper):
    while started:
        global data
        users =[u for u in  get_all_users() if u['rbl']]
        threads =[]
        for u in users:
            t = Thread(target=_from_influx_to_mongo, args=[u['rbl'], u['_id']])
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        sleeper.sleep(30)

def _from_influx_to_mongo(link, id):
    data = get_userdata(link)
    update_db('userdata', data, id)
