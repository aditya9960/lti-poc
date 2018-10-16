from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask import request, json
import os
from . import models

app = Flask(__name__)
config_name = os.getenv('FLASK_CONFIG')
app.config.from_object(app_config[config_name])

db = SQLAlchemy(app)

from .mod_student import mod_student as student_blueprint
from .main import main as main_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(student_blueprint, url_prefix='/api/v1/student')
