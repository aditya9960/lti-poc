from flask import request, json, Response
from . import main

@main.route('/')
def index():
	return 'Hello, World!'

def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )