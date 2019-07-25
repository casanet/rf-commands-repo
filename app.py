from flask import Flask, jsonify
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
   return jsonify(get_device_commands(brand=brand,model=model))

if __name__ == '__main__':
   app.run()