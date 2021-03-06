from data.models import RfDevice


def is_device_exists(brand: str, model: str) -> bool:
    try:
        RfDevice.objects.get(brand=brand, model=model)
        return True
    except:
        return False


def get_devices() -> list:
    devices = []
    for device in RfDevice.objects:
        record = {
            'brand': device.brand,
            'model': device.model,
            'category': device.category,
        }
        devices.append(record)
    return devices


def create_device(device) -> None:
    brand = device['brand']
    model = device['model']
    if is_device_exists(brand=brand, model=model):
        raise Exception("Sorry, the device already exists")

    newDevice = RfDevice(brand=brand, model=model,
                         category=device['category'], commands=device['commands'])
    newDevice.save()


def edit_device(brand: str, model: str, device: dict) -> None:
    if not is_device_exists(brand=brand, model=model) :
        raise Exception("Sorry, the device is not exists")
    if is_device_exists(brand=device['brand'], model=device['model']) :
        raise Exception("Sorry, the new device identity already exists")
    currentDevice = RfDevice.objects.get(brand=brand, model=model)
    currentDevice['brand'] = device['brand']
    currentDevice['model'] = device['model']
    currentDevice['category'] = device['category']
    currentDevice.save()


def delete_device(brand: str, model: str) -> None:
    device = RfDevice.objects.get(brand=brand, model=model)
    device.delete()
