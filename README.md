# rf-commands-repo
Simple, light-weight server for RF commands (such as: IR, 433 MHz etc.) for appliances.

# running server

* in project directory press `pip install -r requirements.txt`
* create mongodb database named `ir-commands`.
* create collection named `commands`.
* set `DATABASE_URL` env ver with mongo url for example `mongodb://<dbuser>:<dbpassword>@<ip>:<port>/ir-commands`.
* run it using `python app.py`.
* in production run is recomended using `gunicorn`.

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
