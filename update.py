#!/usr/bin/env python3

import os
import subprocess
from jinja2 import Environment, FileSystemLoader
from datetime import datetime 



#
# card definiton
#
class Card:

    def __init__(self, name, content):

        self.name = name
        self.content = age

    def getContent(self):
        return self.content

    def getName(self):
        return self.name   



#
# the command execution
#
def run_command(cmd):
	result = subprocess.run(cmd, stdout=subprocess.PIPE)
	str = result.stdout.decode()
	str.replace('\n', '<br>')
	return str



#
# the program
#

PATH = os.path.abspath(os.path.dirname(__file__))

# set your cards here!
cards = [
    { 'name': 'Uptime', 'content': run_command(['uptime']) },
    { 'name': 'Memory', 'content': run_command(['free', '-m']) },
    { 'name': 'Disk', 'content': run_command(['df', '-h']) },
    { 'name': 'Internet', 'content': run_command(['ping', '-c2', 'google.com']) }
]

# render the output
file_loader = FileSystemLoader(PATH + '/templates')
env = Environment(loader=file_loader)
template = env.get_template('index.html.j2')
now = datetime.now() 
output = template.render(cards=cards, date=now)

# write the output to file
filepath = PATH + "/html/index.html"
file = open(filepath, 'w') 
file.write(output) 
file.close() 
