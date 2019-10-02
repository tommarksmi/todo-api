from flask_restful import Resource


class Todo(Resource):
    def get(self):
        return {'test': 'testing stuff'}
