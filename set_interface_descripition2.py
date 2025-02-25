from netmiko import Netmiko
import logging

# Set up logging to capture output for debugging (optional)
logging.basicConfig(filename="netmiko_log.txt", level=logging.DEBUG)

# Define the device to connect to
devices = [{
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",  # Update with actual device IP
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}]

# Loop through the devices to apply the configuration
for device in devices:
    net_connect = Netmiko(**device)

    # Apply configuration from 'changes.txt' file
    output = net_connect.send_config_from_file('changes.txt')

    # Print the output of the configuration command
    print(output)

    # Disconnect from the device
    net_connect.disconnect()
