import logging
import requests
from requests.auth import HTTPBasicAuth
import json

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

HOST = '192.168.1.101'  # The IP of your device
USER = 'student'        # Username for authentication
PASS = 'Meilab123'      # Password for authentication
BASE_URL = 'http://{0}/restconf/api/running/'.format(HOST)  # The base URL for RESTCONF

def set_interfaces(append_url, interface_name):
    # Construct the full URL
    url = BASE_URL + append_url + interface_name
    auth = HTTPBasicAuth(USER, PASS)  # Authentication
    headers = {
        'Accept': 'application/vnd.yang.data+json',
        'Content-Type': 'application/vnd.yang.data+json'
    }
    # Data for the IP address change
    data = {
        "ietf-interfaces:interface": {
            "name": "GigabitEthernet3",  # The interface to change
            "description": "Changed through Restconf",  # Description to add
            "type": "iana-if-type:ethernetCsmacd",  # Type of interface
            "enabled": 'true',  # Enable the interface
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "10.0.10.3",  # New IP address
                        "netmask": "255.255.255.0"  # Subnet mask
                    }
                ]
            },
            "ietf-ip:ipv6": {}  # If no IPv6, leave this empty
        }
    }

    # Send PUT request to change the configuration
    response = requests.put(url, auth=auth, headers=headers, data=json.dumps(data))

    if response.status_code == 204:
        logging.info(f"Request was successful on {HOST}, Code: {response.status_code}")
        return "success!"
    else:
        logging.error(f"Error encountered during request on {HOST}, Code: {response.status_code}")
        return response.text

# Call the function
print(set_interfaces("interfaces/interface/", "GigabitEthernet3"))
