from flask import Flask, render_template
from flask_restful import  Api
from WierdApi import Start, Stop, Test

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return render_template('index.html')


api.add_resource(Start, '/start')
api.add_resource(Stop,'/stop')
api.add_resource(Test,'/test')


if __name__ == '__main__':
    app.run()

