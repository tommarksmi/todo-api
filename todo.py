from flask_restful import Resource, reqparse
from flask import Flask, request

parser = reqparse.RequestParser()


class Todo(Resource):
    def get(self, todo_id):
        return {todo_id: 'testing stuff'}

    def post(self, todo_id):
        request_data = request.form['data']
        # args = parser.parse_args()
        return request_data
