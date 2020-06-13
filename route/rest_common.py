from flask import Flask, jsonify, request, abort
from functools import wraps
from settings import app_name
import os
import sys

app = Flask(app_name)

ADMIN_API_KEY = os.getenv("ADMIN_API_KEY")
if not ADMIN_API_KEY:
    msg = 'ADMIN_API_KEY not exists... exiting'
    print(msg)
    sys.exit(msg)

device_schema = {
    "type": "object",
    "properties": {
        "brand": {"type": "string"},
        "model": {"type": "string"},
        "category": {"type": "string"},
        "commands": {"type": "object"},
    },
    'required': ['brand', 'model', 'category', 'commands']
}

commands_schema = {
    "type": "object",
    "properties": {
        "commands": {"type": "object"},
    },
    'required': ['commands']
}

editDevice_schema = {
    "type": "object",
    "properties": {
        "brand": {"type": "string"},
        "model": {"type": "string"},
        "category": {"type": "string"},
    },
    'required': ['brand', 'model', 'category']
}


@app.after_request
def remove_header(response):
    # Hide server info from possilbe attakers.
    response.headers['Server'] = ''
    return response


def admin_scope():
    """Very simple admin scope authorazed"""
    def _admin_scope(f):
        @wraps(f)
        def __admin_scope(*args, **kwargs):
            try:
                if request.headers['api-key'] != ADMIN_API_KEY:
                    raise Exception('Invalid api-key')
            except:
                abort(403, 'Invalid api-key')
            return f(*args, **kwargs)
        return __admin_scope
    return _admin_scope


@app.route('/.well-known/security.txt')
def security_info_route():
    """ Get security help info """
    return app.send_static_file('.well-known/security.txt')
