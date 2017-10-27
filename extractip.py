#!/bin/usr/python
import shlex
import subprocess
import os
import netifaces
netifaces.interfaces()
for interface in netifaces.interfaces():
	for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
	 #try to ping ip on file #cmd=shlex.split("ping -c1 ['addr']")
     		    	print link['addr']
