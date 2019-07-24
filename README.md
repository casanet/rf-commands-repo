# rf-commands-repo
Simple, light-weight server for RF commands (such as: IR, 433 MHz etc.) for appliances.

# technologies
The Server is Build with Ptyhon, on flask framwork for the HTTP Routing, mongoDB for the data storing.

# purposes
If you have project that use RF commands for appliances (For exmple, see my great project [casanet](https://github.com/haimkastner/home-iot-server)), worry no more! this project will help with storing and fatching commands on demand.
With simple RESTfull API, you will be able the get all the avilable devices in the system, and their known commands.

# stages
in Stage A the DB will be close for uploading, and the we will upload them manually.
you will be able to get the list of all the devices and their known commands. the data will be mostly for Air-conditioning. 
in Stage B the DB will be open for everyone to upload their data, hopefully for other types of devices. also, the API will allow you to search the device you need with a single recording of your device-command.
another expension planned for stage B is receiving all devices commands by type of command (i.e. Turn-off, Turn-on), as a way to try to detecte the type of your device.
