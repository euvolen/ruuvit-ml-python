from flask_restful import Resource
from simpe_deamon import start, stop, test
#TODO Security, ErrorHandlers, Auth - admin level
thread = None

class Start(Resource):
    def get(self):
        global thread
        thread = start()
        return 'Start'


class Stop(Resource):
    def get(self):
        stop(thread)
        return 'Stop'


class Test(Resource):
    def get(self):
        test(thread)
        return 'Test'

