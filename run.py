# -*- encoding: utf-8 -*-
from functools import wraps
from logging import DEBUG, basicConfig, error, info
from os import environ
from sys import stdout
import logging

from flask import Flask, abort, request
from flask_restx import Api, Resource, fields


from apps.src.core import word_count

        
basicConfig(
    stream=stdout,
    level=DEBUG,
)

authorizations = {
    'api_key': {
        'type': 'apiKey',
        'in': 'query',
        'name': 'api_key',
        'required': False,
    }
}

app = Flask(__name__)
app.config.from_envvar('YOURAPPLICATION_SETTINGS')
api = Api(app, authorizations=authorizations)

payload = api.model('Payload', {
    'text': fields.String(description='entre le texte', required=True, example="j'aime la data , et je suis des podcasts de hymaia pour me cultiver "),
})

@api.route('/api/word_count', doc={'description': 'Launch count'})
class CatchAll(Resource):
    @staticmethod
    @api.doc(body=payload, security='api_key')
    @api.response(200, 'Success')
    @api.response(400, 'Bad Request')
    @api.response(401, 'Unauthorized')
    @api.response(404, 'Not Found')
    @api.response(500, 'Internal Server Error')
    def post():
        data = request.get_json()
        info(f'Request body: {data}')
        return word_count(data["text"]),200
        
@api.route('/health', doc={'description': 'Health Check'})
class Health(Resource):
    @staticmethod
    @api.doc(security='api_key')
    @api.response(200, 'Success')
    @api.response(401, 'Unauthorized')
    @api.response(404, 'Not Found')
    @api.response(500, 'Internal Server Error')
    def get():
        return 'OK'


if __name__ == '__main__':
    app.run()
