# rf-commands-repo
Simple, light-weight server for RF commands (such as: IR, 433 MHz etc.) for appliances.

# running server

* Install the `poetry` dependency tool (if not installed yet) by `pip install --user poetry` for more info see [poetry docs](https://python-poetry.org/docs/)
* In project directory press `poetry install`
* Create MongoDB  database named `ir-commands`.
* Create collection named `commands`.
* Set the `DATABASE_URL` environment variable the MongoDB URL,
* Run it using `poetry run python src/app.py`.
* In production run is recommended to use `gunicorn` see [gunicorn page](https://pypi.org/project/gunicorn/).

* In case of editing the dependencies list, after running the `poetry` command, please run `poetry export -f requirements.txt > requirements.txt` to update the `requirements.txt` for the production deploy.

# technologies
The Server is Build with Python, with the Flask framework for the HTTP Routing, MongoDB for the data storing.

# purposes
If you have a project that uses RF commands for appliances (For example, see my great project [casanet](https://github.com/casanet/casanet-server)), worry no more! this project will help with storing and fetching commands on demand.
With simple RESTfull API, you will be able the get all the available devices in the system, and their known commands.

# data access & manipulation
Anyone can access the API, but to manipulate the data the request need to authorized by the [remote server](https://github.com/casanet/remote-server) as a valid local user
by adding an `local_server_key_header` header contains the local server certificate `mac_address:local_server_api_secret_key`.

To allow it, set `REMOTE_SERVER_URL` environment variable contained the remote server URL and `RF_REPOSITORY_API_KEY` with same key in the remote server to validate Rf commands validations requests, see [.env.example](./.env.example) for example.

# API (quick review)
 - GET /devices
 - POST /devices json=`{ brand : string, model: string, category: string, commands: object }`
 - PUT /devices/{brand}/{model} json=`{ brand : string, model: string, category: string }`
 - DELETE /devices/{brand}/{model}
 - GET /rf/{brand}/{model} 
 - PUT /rf/{brand}/{model} json=`{ commands: object }`



