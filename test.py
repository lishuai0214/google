#!/usr/bin/python
import os

ips=open('google.txt','r')
for ip in ips.readlines():
    ip=ip.replace('\n','')
    print ip
