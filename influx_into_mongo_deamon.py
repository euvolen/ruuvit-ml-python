from threading import Thread, Event
from sleeper import Sleep
from connect_mongo import get_all_users, update_db
from connect_influx import get_userdata, erase_db
from ml_mutation import mutate_data
started = True
data = None

s = Sleep()

def get_data(sleeper):
    count = 0
    while started:
        global data
        data = [u['rbl'] for u in get_all_users()]
        threads = []

        for rbl in data:
            threads.append(start(get_userdata))

        for t in threads:
            t.join()

        mutated = mutate_data(data)
        update_db('users', str(count))
        count +=1
        sleeper.sleep(30)



def start(func):
    #TODO Exception handler and Decorator probably?
    global started
    started = True
    main_thread = Thread(target=func if func else get_data, args=[s])
    main_thread.start()
    return main_thread

def stop(main_thread):
    # TODO Exception handler and Decorator probably?
    global started
    started = False
    s.wake()
    main_thread.join()


def test(main_thread):
    # TODO Exception handler
    return f'{main_thread}'