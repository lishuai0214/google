#!/usr/bin/python
import os

IPs=open('test','r')
able=open('able.txt','wb')
unable=open('diable.txt','wb')
for ip in IPs.readlines():
	ip=ip.replace('\n','')
	ret=os.system("ping -c 1 -W 1 " + ip + "> /dev/null")
	if not ret:
		print "ping "+ ip + "  OK" 
		able.write( ip + "\tOK\n")
	else:
		print "ping "+ ip + "  ERROR"
		unable.write(ip + "\tERROR\n")
	
IPs.close()
unable.close()
able.close()