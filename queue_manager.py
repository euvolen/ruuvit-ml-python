import time
import queue
from threading import Thread
from connect_mongo import get_all_users
get_dataqueue = queue.Queue()
mutate_data_with_ml = queue.Queue()
post_dataqueue = queue.Queue()

stop = False


def _mutate(data):

    return [u['firstname'] for u in data]

def _post(data):

    for u in data:
        print(u)


def get_data_manager():

    while not stop:
        data = get_dataqueue.get()
        mutate_data_with_ml.put(data)
        get_dataqueue.task_done()

def mutation_manager():
    while not stop:
        data = mutate_data_with_ml.get()
        new_data = _mutate(data)
        post_dataqueue.put(new_data)

def post_data_manager():
    while not stop:
        data = post_dataqueue.get()
        _post(data)
        post_dataqueue.task_done()
        get_data()

gdm = Thread(target=get_data_manager )
mm = Thread(target=mutation_manager )
pdm = Thread(target=post_data_manager)

def start_main_threads():

    gdm.start()
    mm.start()
    pdm.start()


def get_data():
    global stop
    stop = False
    time.sleep(5)
    users = get_all_users()
    get_dataqueue.put(users)


def simple_test():
    print(gdm.is_alive())
    print(mm.is_alive())
    print(pdm.is_alive())


def join_all_theads():
    global stop
    stop = True
    get_dataqueue.join()
    mutate_data_with_ml.join()
    post_dataqueue.join()
    gdm.join()
    mm.join()
    pdm.join()
