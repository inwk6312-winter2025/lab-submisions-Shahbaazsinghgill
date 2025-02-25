from netmiko import Netmiko

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",  # Router 1
    "username": "student",
    "password": "Meilab123",
    "secret": "cisco",  # Required for enable mode
    "port": "22",
}

net_connect = Netmiko(**device)

# Print the initial prompt
print(f"Default prompt: {net_connect.find_prompt()}")

# Send the "disable" command and print the prompt
net_connect.send_command_timing("disable")
print(f"Disable command: {net_connect.find_prompt()}")

# Re-enter enable mode and print the prompt
net_connect.enable()
print(f"Enable command: {net_connect.find_prompt()}")

# Close the connection
net_connect.disconnect()
