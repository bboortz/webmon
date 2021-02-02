#!/usr/bin/env python3

from os import path, listdir
from jinja2 import Environment, FileSystemLoader
import datetime as dt
import jsonpickle

from config import cfg
from model import Hosts



#
# methods
#

def render_output(hosts, output_filepath):
    print("INFO: writing output to file %s" % output_filepath)
    print(hosts)

    # render the output
    file_loader = FileSystemLoader(cfg.templates_path)
    env = Environment(loader=file_loader)
    template = env.get_template('index.html.j2')
    now = dt.datetime.now() 
    output = template.render(hosts=hosts)

    # write the output to file
    file = open(output_filepath, 'w') 
    file.write(output) 
    file.close() 


def render_file(filepath, output_filepath):
    print("INFO: reading from file %s" % filepath)

    # read the json file
    file = open(filepath, 'r') 
    json_string = file.read()
    file.close() 

    # transform json string to object
    jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=4)
    host = jsonpickle.decode(json_string)
    print(host)

    return host



#
# the program
#

print("INFO: rendering html ...")

# iterate over all files in tmp dir
host_list = []
dir = cfg.tmp_path
for filename in listdir(dir):
    if filename.endswith(".data.json"):
        host = render_file( path.join(dir, filename), cfg.output_filepath )
        host_list.append(host)
        print()
    else:
        continue

# render the output
now = dt.datetime.now() 
hosts = Hosts(host_list, now)
render_output(hosts, cfg.output_filepath)

print()
