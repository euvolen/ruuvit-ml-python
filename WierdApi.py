from flask_restful import Resource
from simpe_deamon import start, stop, test
#TODO Security, Auth - admin level

thread = None


class Start(Resource):
    def post(self):
        global thread
        if thread is None:
            thread = start()
            return {'msg': f'{thread} is started', 'status': True}
        if not thread.is_alive():
            thread = start()
            return {'msg': f'{thread} is started', 'status': True}
        else:
            return {'msg': 'Thread has been started already', 'status': True}


class Stop(Resource):
    def post(self):
        if thread is None:
            return {'msg': 'No running threads', 'status': False}
        if thread.is_alive():
            stop(thread)
            return {'msg': f'{thread} stopped', 'status': False}
        else:
            return {'msg': 'Thread has been stopped already', 'status': False}


class Test(Resource):
    def post(self):
        if thread is not None:
            return { 'msg': test(thread), 'test': True}
        else:
            return  { 'msg': 'No running threads', 'test':True}
