from netmiko import ConnectHandler

r1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}

r2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102",  # Fixed IP for R2 (was mistakenly same as R1)
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}

# Iterate over both devices
for device in (r1, r2):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show interface description")
    net_connect.disconnect()

    # Print results
    print("-" * 100)
    print(f"Device: {device['ip']}")
    print(output)
    print("-" * 100)
