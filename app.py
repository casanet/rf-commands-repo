from flask import Flask, jsonify
import os
import settings
from data import get_devices, get_device_commands

app = Flask(__name__)

@app.after_request
def remove_header(response):
    # Hide server info from possilbe attakers.
    response.headers['Server'] = ''
    return response

# Get all supported devices in system
@app.route('/devices')
def models_list():
    return jsonify(get_devices())

# Get RF commands of a devices.
@app.route('/rf/<brand>/<model>')
def model_rf_commands(brand, model):
    return jsonify(get_device_commands(brand=brand, model=model))


# Get security help info
@app.route('/.well-known/security.txt')
def security_info():
    return app.send_static_file('.well-known/security.txt')
        
    
# Get PORT from env.
PORT = os.getenv("PORT")
if not PORT:
    PORT = 5000
else:
    PORT = int(PORT)

if __name__ == '__main__':
    app.run(port=PORT)
