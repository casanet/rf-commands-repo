from mongoengine import *
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# Connect mongoengine driver to the database
connect(host=DATABASE_URL)


class RfDevice(Document):
    """Devices document objects model."""
    meta = {
        'collection': 'commands'
    }
    brand = StringField(required=True)
    model = StringField(required=True)
    category = StringField(required=True)
    commands = DynamicField(required=True)
