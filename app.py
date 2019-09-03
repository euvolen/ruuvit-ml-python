from flask import Flask, render_template
from flask_restful import  Api
from flask_cors import CORS

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

from config import jwt_secret
from api.ml_manager import ML_Start, ML_Stop, ML_Test
from api.influx_manager import InfluxStart, InfluxStop, InfluxTest
from auth import AdminLogin
app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = jwt_secret
jwt = JWTManager(app)
CORS(app)

@app.route('/')
@jwt_required
def home():
    current = get_jwt_identity()
    print(current)
    return render_template('index.html')

api.add_resource(AdminLogin, '/admin')
api.add_resource(ML_Start, '/ml/start')
api.add_resource(ML_Stop, '/ml/stop')
api.add_resource(ML_Test, '/ml/test')

api.add_resource(InfluxStart, '/influx/start')
api.add_resource(InfluxStop, '/influx/stop')
api.add_resource(InfluxTest, '/influx/test')

if __name__ == '__main__':
    app.run()

