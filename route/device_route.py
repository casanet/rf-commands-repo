from flask import Flask, jsonify, request, abort
from route.rest_common import admin_scope, commands_schema, device_schema, edit_device_schema, app
from flask_expects_json import expects_json
from data.devices import edit_device, create_device, delete_device, get_devices


@app.route('/devices', methods=['GET'])
def models_list_route():
    return jsonify(get_devices())


@app.route('/device', methods=['POST'])
@expects_json(device_schema)
@admin_scope()
def create_device_route():
    create_device(request.json)
    resp = jsonify(success=True)
    return resp


@app.route('/device/<brand>/<model>', methods=['PUT'])
@admin_scope()
@expects_json(edit_device_schema)
def set_device_route(brand: str, model: str):
    edit_device(brand=brand, model=model, device=request.json)
    resp = jsonify(success=True)
    return resp


@app.route('/device/<brand>/<model>', methods=['DELETE'])
@admin_scope()
def delete_device_route(brand: str, model: str):
    delete_device(brand=brand, model=model)
    resp = jsonify(success=True)
    return resp
