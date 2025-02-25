from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template.j2")

class NetworkInterface:
    def __init__(self, name, description, vlan):
        self.name = name
        self.description = description
        self.vlan = vlan

interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10)
print(template.render(interface=interface_obj))
