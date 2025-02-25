from jinja2 import Environment, FileSystemLoader
import yaml

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("router-template.j2")

with open("router-config.yml") as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)

print(template.render(config))
