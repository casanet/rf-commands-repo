# rf-commands-repo
Simple, light-weight server for RF commands (such as: IR, 433 MHz etc.) for appliances.

# running server

* Install the `poetry` dependency tool (if not installed yet) by `pip install --user poetry` for more info see [poetry docs](https://python-poetry.org/docs/)
* In project directory press `poetry install`
* Create MongoDB  database named `ir-commands`.
* Create collection named `commands`.
* Set `DATABASE_URL` environment variable the MongoDB URL,
* Run it using `poetry run python src/app.py`.
* In production run is recommended to use `gunicorn` see [gunicorn page](https://pypi.org/project/gunicorn/).

* In case of editing the dependencies list, after running the `poetry` command, please run `poetry export -f requirements.txt > requirements.txt` to update the `requirements.txt` for the production deploy.

# technologies
The Server is Build with Python, with the Flask framework for the HTTP Routing, MongoDB for the data storing.

# purposes
If you have a project that uses RF commands for appliances (For example, see my great project [casanet](https://github.com/casanet/casanet-server)), worry no more! this project will help with storing and fetching commands on demand.
With simple RESTfull API, you will be able the get all the available devices in the system, and their known commands.

# stages
## Stage A
The DB will be close for uploading, and we will upload them manually.
you will be able to get the list of all the devices and their known commands. the data will be mostly for Air-conditioning. 
## Stage B
The DB will be open for everyone to upload their data, hopefully for other types of devices. also, the API will allow you to search the device you need with a single recording of your device-command.
another expansion planned for stage B is receiving all devices commands by type of command (i.e. Turn-off, Turn-on), as a way to try to detect the type of your device.
