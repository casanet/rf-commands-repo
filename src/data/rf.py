
from data.models import RfDevice


def get_device_commands(brand: str, model: str) -> dict:
    device = RfDevice.objects.get(brand=brand, model=model)
    return device.commands


def set_device_commands(brand: str, model: str, data: dict) -> None:
    device = RfDevice.objects.get(brand=brand, model=model)
    device.commands = data['commands']
    device.save()
