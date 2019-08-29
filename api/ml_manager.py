from flask_restful import Resource
from thread_fb import  create_thread
from workers.ml_manager import get_data, start_worker, stop_worker
from sleeper import Sleep

#TODO Security, Auth - admin level

thread = None
sleep = Sleep()

class ML_Start(Resource):
    def get(self):
        global thread
        if thread is None:
            thread = create_thread(get_data, sleep)
            thread.start()
            return {'msg': f'{thread} is started', 'status': True}
        if not thread.is_alive():
            start_worker()
            thread = create_thread(get_data, sleep)
            thread.start()
            return {'msg': f'{thread} is started', 'status': True}
        else:
            return {'msg': 'Thread has been started already', 'status': True}


class ML_Stop(Resource):
    def get(self):
        if thread is None:
            return {'msg': 'No running threads', 'status': False}
        if thread.is_alive():
            stop_worker()
            sleep.wake()
            thread.join()
            return {'msg': f'{thread} stopped', 'status': False}
        else:
            return {'msg': 'Thread has been stopped already', 'status': False}


class ML_Test(Resource):
    def get(self):
      return f'{thread}'