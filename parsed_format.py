from netmiko import Netmiko

# Define device
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}

# Connect to device
net_connect = Netmiko(**device)
output = net_connect.send_command("show ip interface brief", use_textfsm=True)
net_connect.disconnect()

# Check the output type
print(type(output))  # Should print: <class 'list'>

# Iterate through output and print interface names
for interface in output:
    print(interface['interface'])
