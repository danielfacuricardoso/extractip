#!/bin/usr/python
import shlex
import subprocess
import os
import netifaces
netifaces.interfaces()
#netifaces.ifaddresses('choose some interface like eth1-2 1 per')
#for interface in netifaces.interfaces():
    #print netifaces.ifaddresses(interface)[netifaces.AF_INET]
for interface in netifaces.interfaces():
	for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
					#cmd=shlex.split("ping -c1 ['addr']")
     		    	print link['addr']
