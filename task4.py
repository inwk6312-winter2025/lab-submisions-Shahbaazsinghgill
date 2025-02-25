from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task4.j2")

interface_data = {
    "description": "Server Port",
    "vlan": 10
}

print(template.render(interface=interface_data))

