from netmiko import Netmiko

# Define the devices to connect to
devices = [{
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}]

# Set the description to be applied to the interface
description = 'Description set with Netmiko'
description_config = [
    "interface GigabitEthernet3",  # Interface to configure
    f"description {description}"   # Setting the description
]

# Loop through devices and apply configuration
for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set(description_config)
    print(output)  # Print the output from the device after configuration
    net_connect.disconnect()  # Disconnect from the device
