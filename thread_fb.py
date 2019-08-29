from threading import Thread

def create_thread(func, s):
    return Thread(target=func, args=[s])