import bcrypt
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from connect_mongo import get_user_by_email


parser = reqparse.RequestParser()

class AdminLogin(Resource):
    def post(self):
        parser.add_argument('email')
        parser.add_argument('password')
        data = parser.parse_args()
        user = get_user_by_email(data['email'])
        if user['role'] != 'admin':
            return {'msg': 'Unauthorized'}
        if bcrypt.checkpw(data['password'].encode('utf-8'), user['password'].encode('utf-8')):
            return {'token':create_access_token(identity=user['email'])}
        else:
            return {'msg': 'Passwords don\'t match'}


