from flask_restful import Resource
from simpe_deamon import start, stop, test
#TODO Security, Auth - admin level

thread = None


class Start(Resource):
    def get(self):
        global thread
        if thread is None:
            thread = start()
            return {'msg': 'Started', 'success': True}
        if not thread.is_alive():
            thread = start()
            return {'msg': 'Started', 'success': True}
        else:
            return {'msg': 'Thread has been started already', 'success': False}


class Stop(Resource):
    def get(self):
        if thread is None:
            return {'msg': 'No running processes', 'success': False}
        if thread.is_alive():
            stop(thread)
            return {'msg': 'stopped', 'success': True}
        else:
            return {'msg': 'Thread has been stopped already', 'success': False}


class Test(Resource):
    def get(self):
        if thread is not None:
            return { 'is thread alive': test(thread)}
        else:
            return  { 'is thread alive': 'No running threads'}
