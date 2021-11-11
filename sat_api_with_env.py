"""
Module to pull json output for satellite APIs
Author: Jaskaran Singh Narula
Email: narula.jaskaran@gmail.com
"""

import requests
import json
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


## Variables
USER = "admin"
PASSWORD = "changme"
SATILLITE_FQDN = "satellite.example.com"

def main():
    """
    Funtion to make the API resquest as per the API metioned in URL variable below.
    APIs can be:
    1) /api/hosts (default)
    2) /api/hosts?thin=1
    3) /api/hosts?thin=1\&per_page=10000
    """
    URL = "http://" + SATILLITE_FQDN + "/api/hosts"
    response = requests.get(URL, auth = HTTPBasicAuth(USER, PASSWORD), verify = False)
    data = json.loads(response.text)
    json_output = {
        "results":[]
    }
    for i in data['results']:
        value = {}
        try:
            value['name'] = i['name']
        except:
            value['name_error'] = "No Name for this server"
        try:
            value['last_checkin'] = i['subscription_facet_attributes']['last_checkin']
        except:
            value['last_checkin_error'] = "No last_checkin for this server"
        try:
            value['registered_through'] = i['subscription_facet_attributes']['registered_through']
        except:
            value['registered_through_error'] = "No registered_through for this server"

        json_output['results'].append(value)

    print(json.dumps(json_output, indent=4))

if __name__ == "__main__":
    main()
