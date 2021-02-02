#!/usr/bin/env python3

import os
import subprocess
import datetime as dt
import jsonpickle
import socket

from config import cfg
from model import Card, Host



#
# methods
#

def run_command(cmd):
	result = subprocess.run(cmd, stdout=subprocess.PIPE)
	str = result.stdout.decode()
	str.replace('\n', '<br>')
	return str



#
# the program
#

print("INFO: gathering data ...")

# set your cards here!
cards = [
    Card("Uptime", run_command(['uptime']) ),
    Card("Memory", run_command(['free', '-m']) ),
    Card("ZFS", run_command([cfg.scripts_path + '/zstatus.sh']) ),
    Card("Disk", run_command(['df', '-h']) ),
    Card("Internet", run_command(['ping', '-c2', 'google.com']) )
]

# host object
hostname = socket.getfqdn(socket.gethostname())
host = Host(hostname, cards, dt.datetime.now())
print(host)

# transform object to json string
jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=4)
json_string = jsonpickle.encode(host)
#print(json_string)

# write the output to file
filepath = cfg.tmp_path + "/" + hostname + ".data.json"
file = open(filepath, 'w') 
file.write(json_string) 
file.close() 

print()
