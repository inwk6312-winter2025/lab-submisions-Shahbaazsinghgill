from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task6.j2")

interfaces = [
    {"name": "GigabitEthernet0/1", "desc": "Uplink Port", "uplink": True},
    {"name": "GigabitEthernet0/2", "desc": "Server Port 1", "vlan": 10},
    {"name": "GigabitEthernet0/3", "desc": "Server Port 2", "vlan": 10}
]

print(template.render(interface_list=interfaces))
