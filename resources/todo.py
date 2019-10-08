from flask_restful import Resource, reqparse
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import database.config as db_conf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/tom/temp/todo.db'
db = SQLAlchemy(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=False)

Session = sessionmaker(bind=engine)
session = Session()

parser = reqparse.RequestParser()


class Todo(Resource):
    def get(self, todo_id):
        query_result = session.query(db_conf.Todo).filter_by(id=todo_id).first()
        return {query_result.id: query_result.text}

    def post(self, todo_id):
        request_data = request.form['data']
        user_todo = db_conf.Todo(id=todo_id, text=request_data)
        session.add(user_todo)
        session.commit()
        return request_data
