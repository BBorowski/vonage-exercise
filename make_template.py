#!/usr/bin/python3

import yaml
import os.path
from jinja2 import Environment, FileSystemLoader

def read_and_print_file(input_file):
    try:
        with open(input_file, mode="r") as f:
            content = yaml.safe_load(f)
    except (yaml.scanner.ScannerError, yaml.parser.ParserError) as e:
        print(f"Input file '{input_file}' is not structured correctly")
        raise e

    print(f"From file '{input_file}' loaded the following configuration:")
    for key, value in content.items():
        print(key + ": " + (value if value is not None else ''))

    return content

def read_template(template_file):
    environment = Environment(
                    loader=FileSystemLoader(
                    os.path.dirname(template_file)))
    return environment.get_template(os.path.basename(template_file))

def save_output_file(project_data, template, output_file):
    with open(output_file, mode="w") as df:
        df.write(template.render(project_data))

def main(input_file="project.yaml",
         output_file="Dockerfile",
         template_file="templates/Dockerfile.jinja"):
    project_data = read_and_print_file(input_file)
    template = read_template(template_file)
    save_output_file(project_data, template, output_file)

if __name__ == '__main__':
    main()
