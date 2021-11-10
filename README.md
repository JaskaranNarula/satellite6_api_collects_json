# Red Hat Satellite 6 APIs collects json

This is a single python module which can be excuted on any system from where we need to pull API request response in a JSON format. 

## How to use this script. 

1. Download the python scripts to any desired directory or on your Red Hat Satellite 6.7 or later.

2. Add the admin creds of the satellite admin user to the script under the variables:
~~~
USER = "admin"
PASSWORD = "changme"
SATILLITE_FQDN = "satellite.example.com"
~~~

3. Run the scripts as below.

#### Usage
~~~
# python3 satellite_api_output.py 
~~~

