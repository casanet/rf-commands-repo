from flask import Flask, jsonify, request, abort
from route.rest_common import app, admin_scope, commands_schema
from flask_expects_json import expects_json
from data.rf import set_device_commands, get_device_commands


@app.route('/rf/<brand>/<model>', methods=['GET'])
def model_rf_commands_route(brand: str, model: str):
    return jsonify(get_device_commands(brand=brand, model=model))


@app.route('/rf/<brand>/<model>', methods=['PUT'])
@admin_scope()
@expects_json(commands_schema)
def set_device_commans_route(brand: str, model: str):
    set_device_commands(brand=brand, model=model, data=request.json)
    resp = jsonify(success=True)
    return resp
