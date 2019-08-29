from flask import Flask, render_template
from flask_restful import  Api
from flask_cors import CORS
from api.ml_manager import ML_Start, ML_Stop, ML_Test
from api.influx_manager import InfluxStart, InfluxStop, InfluxTest

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')


api.add_resource(ML_Start, '/ml/start')
api.add_resource(ML_Stop, '/ml/stop')
api.add_resource(ML_Test, '/ml/test')

api.add_resource(InfluxStart, '/influx/start')
api.add_resource(InfluxStop, '/influx/stop')
api.add_resource(InfluxTest, '/influx/test')

if __name__ == '__main__':
    app.run()

