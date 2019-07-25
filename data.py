from mongoengine import *
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# Connect mongoengine driver to the database
connect(host=DATABASE_URL)

# Device document model.
class RfDevice(Document):
    meta = {
        'collection': 'commands'
    }
    brand = StringField(required=True)
    model = StringField(required=True)
    category = StringField(required=True)
    commands = ObjectIdField(required=True)

def get_devices():
    devices = []
    for device in RfDevice.objects:
        record = {
            'brand': device.brand,
            'model': device.model,
            'category': device.category,
        }
        devices.append(record)
    return devices

def get_device_commands(brand, model):
    device= RfDevice.objects.get(brand=brand,model=model)
    return device.commands