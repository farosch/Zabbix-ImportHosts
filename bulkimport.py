#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#v1.0 Michael Kaplan
#v1.1 Faryan Rezagholi

from zabbix_api import ZabbixAPI
import csv
from progressbar import ProgressBar, Percentage, ETA, ReverseBar, RotatingMarker, Timer


############################## Define Parameters ##############################
url = "https://zabbix/api_jsonrpc.php"
username = "user"
secret = "pass"
groupid = 2 # set group id (you can find it using zabbix-cli)
char = ";" # delimiting character in csv
path = "C:\\hosts.csv" # change the file name to that one you intend to use 
port = 161
############################ End Define Parameters ############################


zapi = ZabbixAPI(url)
zapi.session.verify = False
zapi.login(user=username, password=secret)
file = csv.reader(open(path))
lines = sum(1 for line in file)
bar = ProgressBar(maxval=lines,widgets=[Percentage(), ReverseBar(), ETA(), RotatingMarker(), Timer()]).start()
i = 0
f = csv.reader(open(path), delimiter=char)

for [hostname,ip] in f:
    zapi.host.create({
        "host": hostname ,
        "interfaces":[{
            "type": 1,
            "main": 1,
            "useip": 1,
            "ip": ip,
            "dns": hostname,
            "port": port
        }],
        "groups":[{
            "groupid": groupid
        }]
        }
    )

    i += 1
    bar.update(i)

print ("\n Done")
        