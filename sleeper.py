from threading import Event
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
