from flask import Blueprint

mod_student = Blueprint('mod_student', __name__)

from . import models, views