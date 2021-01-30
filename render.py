#!/usr/bin/env python3

from os import path, listdir
from jinja2 import Environment, FileSystemLoader
import datetime as dt
import jsonpickle

from config import cfg



#
# methods
#

def render_file(filepath):
    print("INFO: reader from file %s" % filepath)

    # read the json file
    file = open(filepath, 'r') 
    json_string = file.read()
    file.close() 

    # transform json string to object
    jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=4)
    host = jsonpickle.decode(json_string)
    print(host)

    # render the output
    file_loader = FileSystemLoader(cfg.templates_path)
    env = Environment(loader=file_loader)
    template = env.get_template('index.html.j2')
    now = dt.datetime.now() 
    output = template.render(host=host, date=now)

    # write the output to file
    filepath = cfg.html_path + "/index.html"
    file = open(filepath, 'w') 
    file.write(output) 
    file.close() 



#
# the program
#

print("INFO: rendering html ...")

# iterate over all files in tmp dir
dir = cfg.tmp_path
for filename in listdir(dir):
    if filename.endswith(".data.json"):
        render_file( path.join(dir, filename) )
        print()
    else:
        continue

print()
