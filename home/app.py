# -*- coding: utf-8 -*-
import sys
from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from flask_migrate import Migrate
import json
from functools import wraps

app = Flask(__name__)

api = Api(app)

def as_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        res = f(*args, **kwargs)
        res = json.dumps(res, ensure_ascii=False).encode('utf8')
        return Response(res, content_type='application/json; charset=utf-8')
    return decorated_function


class Login(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            _userEmail = args['email']
            _userPassword = args['password']
            return {'Email': args['email'], 'Password': args['password']}
        except Exception as e:
            return {'error': str(e)}
api.add_resource(Login, '/login')

@app.route("/name/<name>")
@as_json
def get_book_name(name):
    return {'name' : name}
@app.route("/")
@as_json
def first():
    return {'name':'경준'}

@app.route("/details")
def get_book_details():
    author=request.args.get('author')
    published=request.args.get('published')
    return "Author : {}, Published: {}".format(author,published)

if __name__ == '__main__':
    app.run()