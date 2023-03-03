# -*- encoding: utf-8 -*-
from functools import wraps
from logging import DEBUG, basicConfig, error, info
from os import environ
from sys import stdout

from flask import Flask, abort, current_app, request
from flask_restx import Api, Resource, fields
from werkzeug.exceptions import HTTPException

from application.src.core import run

        
basicConfig(
    stream=stdout,
    level=DEBUG,
)

tasks = {}
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



get_status_response_model = api.model('Status', {
    'id': fields.String(description='Job ID', required=True, example="779693ba57dc43889d235fe3095553d2"),
    'status': fields.String(description='Appel à compter les mots', required=True, example="PENDING"),
    'message': fields.String(description='Specific message', required=True)
})

@api.route('/api/callback/<job_id>', doc={'description': 'Get status of call', 'params':{'job_id': {'example':'779693ba57dc43889d235fe3095553d2', 'description':'The ID of the job returned by /task endpoint'}}})
class GetTaskStatus(Resource):
    @staticmethod
    @api.doc(security='api_key')
    @api.response(200, 'Success', get_status_response_model)
    @api.response(400, 'Bad Request')
    @api.response(401, 'Unauthorized')
    @api.response(404, 'Not Found')
    @api.response(500, 'Internal Server Error')
    def get(job_id):
        info(tasks)
        task = tasks.get(job_id)
        if task is None:
            abort(404)

        return {
                   'id': job_id,
                   'status': task['status'],
                   'message': task['return_value']
               }, 200


post_tasks_response_model = api.model('Job', {
    'jobId': fields.String(description='Job ID to use for callback', example="779693ba57dc43889d235fe3095553d2"),
    'eta': fields.Integer(description='Estimated Time of Arrival', example=90),
    'retryInterval': fields.Integer(description='Delay between retries', required=True, example=30)
})

payload = api.model('Payload', {
    'text': fields.String(description='entre le texte', required=True, example="j'aime la data , et je suis des podcasts de hymaia pour me cultiver "),
})

@api.route('/api/count_cord', doc={'description': 'Launch job'})
class CatchAll(Resource):
    @staticmethod
    @api.doc(body=payload, security='api_key')
    @api.response(202, 'Success', post_tasks_response_model)
    @api.response(400, 'Bad Request')
    @api.response(401, 'Unauthorized')
    @api.response(404, 'Not Found')
    @api.response(500, 'Internal Server Error')
    def post():
        data = request.get_json()
        info(f'Request body: {data}')
        run(data)
        
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
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(environ.get('PORT', 8080))
    )
