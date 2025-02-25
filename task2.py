from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task2.j2")

class NetworkInterface:
    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

# First test with uplink=False
interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10, uplink=False)
print(template.render(interface=interface_obj))

# Now test with uplink=True
interface_obj.uplink = True
print("\nWith Uplink Enabled:")
print(template.render(interface=interface_obj))
