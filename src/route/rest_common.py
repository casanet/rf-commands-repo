from flask import Flask, jsonify, request, abort
from functools import wraps
from settings import app_name, rf_repository_key_header, local_server_key_header, REMOTE_SERVER_URL, RF_REPOSITORY_API_KEY
import requests 

app = Flask(app_name)

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

edit_device_schema = {
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
    # Hide server info from possible attackers.
    response.headers['Server'] = ''
    return response

def local_server_scope():
    """Scope for valid local server request, used for editing devices authorization"""
    def _local_server_scope(f):
        @wraps(f)
        def __local_server_scope(*args, **kwargs):
            try:
                local_server_key: str = request.headers.get(local_server_key_header)
                if not local_server_key :
                    raise Exception('Please set local_server_key header')
                local_server_key = local_server_key.split(":", 1)
                headers={}
                headers[rf_repository_key_header] = RF_REPOSITORY_API_KEY
                data={}
                data['mac'] = local_server_key[0]
                data['key'] = local_server_key[1]
                result = requests.post(url=f'{REMOTE_SERVER_URL}/API/servers/verification', headers=headers, json=data)
                if not result.status_code == 200:
                    raise Exception('Authentication failed')
                local_server: dict = result.json()
                request.local_server = local_server
                print(local_server)
            except:
                abort(403, 'Invalid certificates')
            return f(*args, **kwargs)
        return __local_server_scope
    return _local_server_scope


@app.route('/.well-known/security.txt')
def security_info_route():
    """ Get security help info """
    return app.send_static_file('.well-known/security.txt')
