from flask import Flask, jsonify, request, abort
import os
import settings
import route.rf_route
import route.device_route
from route.rest_common import app

# Get PORT from env.
PORT = os.getenv("PORT")
if not PORT:
    PORT = 5000
else:
    PORT = int(PORT)

if __name__ == '__main__':
    app.run(port=PORT)
