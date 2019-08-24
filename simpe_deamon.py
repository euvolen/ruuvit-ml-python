from threading import Thread, Event
import time
from connect_mongo import get_all_users, update_db
from ml_mutation import mutate_data
started = True
data = None

class Sleep():
    def __init__(self, seconds=600, immediate=False):
        self.seconds = seconds
        self.event = Event()
        if immediate:
            self.sleep()

    def sleep(self, seconds=None):
        if seconds is None:
            seconds = self.seconds
        self.event.clear()
        self.event.wait(timeout=seconds)

    def wake(self):
        self.event.set()

s = Sleep()

def get_data(sleeper):
    count = 0
    while started:
        global data
        #time.sleep(30)
        data = get_all_users()
        #TODO ML alghorithm
        mutated = mutate_data(data)
        update_db('users', str(count))
        count +=1
        sleeper.sleep(30)



def start():
    #TODO Exception handler and Decorator probably?
    global started
    started = True
    main_thread = Thread(target=get_data, args=[s], daemon=True)
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
    print(main_thread.is_alive())