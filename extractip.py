#!/bin/usr/python
import shlex
import subprocess
import os
import netifaces
netifaces.interfaces()
for interface in netifaces.interfaces():
	for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
	 #try to ping ip on file #cmd=shlex.split("ping -c1 ['addr']")
     		     with open('test1','w') as f:
                       sys.stdout=f
                        print link['addr']
   # problem:need to write 4 lines but it just write last, its mean that it's overwrite all lines before last.
		
