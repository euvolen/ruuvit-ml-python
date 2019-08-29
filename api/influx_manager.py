from flask_restful import Resource
from sleeper import Sleep
from thread_fb import create_thread
from workers.influx_manager import influx_to_mongo_loop, stop_worker, start_worker
#TODO Security, Auth - admin level



thread = None
sleep = Sleep()

class InfluxStart(Resource):
    def get(self):
        global thread
        if thread is None:
            thread = create_thread(influx_to_mongo_loop, sleep)
            thread.start()
            return {'msg': f'{thread} is started', 'status': True}
        if not thread.is_alive():
            start_worker()
            thread = create_thread(influx_to_mongo_loop, sleep)
            thread.start()
            return {'msg': f'{thread} is started', 'status': True}
        else:
            return {'msg': 'Thread has been started already', 'status': True}


class InfluxStop(Resource):
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


class InfluxTest(Resource):
    def get(self):
      return f'{thread}'