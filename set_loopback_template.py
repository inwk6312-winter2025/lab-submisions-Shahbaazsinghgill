import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

# Load the host and interface information from YAML files
hosts = yaml.load(open('hosts.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('interfaces.yml'), Loader=yaml.SafeLoader)

# Set up Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, autoescape=True)
template = env.get_template('interfaces_config_template.j2')

# Render the template with the interface information
loopback_config = template.render(data=interfaces)

# Loop through the hosts and apply the configuration
for host in hosts["hosts"]:
    # Connect to the device via Netmiko
    net_connect = Netmiko(host=host["name"],
                          username=host["username"],
                          password=host["password"],
                          port=host["port"],
                          device_type=host["type"])
    print(f"Logged into {host['name']} successfully")
    
    # Send the loopback configuration commands
    output = net_connect.send_config_set(loopback_config.split("\n"))
    print(f"Pushed config into {host['name']} successfully")

    # Disconnect from the device
    net_connect.disconnect()

print("Done!")
