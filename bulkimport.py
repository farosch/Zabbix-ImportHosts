#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#v1.0 Made by Michael Kaplan
#v1.1 Made by Faryan Rezagholi

from zabbix_api import ZabbixAPI
import csv
from progressbar import ProgressBar, Percentage, ETA, ReverseBar, RotatingMarker, Timer

############################## Define Parameters ##############################
zapi = ZabbixAPI("https://zabbix/api_jsonrpc.php")
zapi.login(user="user", password="pass")
groupid = 25 #edit group id, you can find it using zabbix-cli
templateid = 11433 #edit templete id you can find it using zabbix-cli
############################ End Define Parameters ############################

zapi.session.verify = False
file = csv.reader(open(r"C:\Users\faryan.rezagholi\Downloads\zabbix-bulk-import-master\hosts.csv"))
lines = sum(1 for line in file)
bar = ProgressBar(maxval=lines,widgets=[Percentage(), ReverseBar(), ETA(), RotatingMarker(), Timer()]).start()
i = 0
f = csv.reader(open(r"C:\Users\faryan.rezagholi\Downloads\zabbix-bulk-import-master\hosts.csv"), delimiter=';') #Change the file name to that one you intend to use 

for [hostname,ip] in f: #edit colums to be readed and set variables for parameters
    zapi.host.create({
        "host": hostname ,
        "interfaces":[{
            "type": 2,
            "main": 1,
            "useip": 1,
            "ip": ip,
            "dns": hostname,
            "port": 161
        }],
        "groups":[{
            "groupid": groupid
        }],
        "templates":[{
            "templateid": templateid
        }]
        }
    )

    i += 1
    bar.update(i)

print ("\n Done")
        