# -*- encoding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object('app.configuration.Config')

db = SQLAlchemy  (app)

ma = Marshmallow(app)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
