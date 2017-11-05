#!/usr/bin/env python
#coding: utf-8
import paramiko
import os
import subprocess
import sys
l=[['r1','r2',0],['r2','r4',1]]
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.3.2', username='root', password='admin')
stdin, stdout, stderr = ssh.exec_command('ping -c 1 192.168.0.2 -q\n')  # pode ser redirecionado ou guardado em um lista
a= stdout.read()
estadoseg1=int(a.split('\n')[3].split(',')[2].split(" ")[1][:-1])

#seg1ip = "192.168.0.2"
#estadoseg1 = os.system("ping %s -c 2" % seg1ip)
#estadoseg1 = os.system("ip addr show")
#l=[['r1','r2',0],['r1','r2',1]]
if estadoseg1 is not 0:
    l[0][2]=1
else:
    l[0][2]=0
if l[0][2]  is not 0:
    print "segmento1,down"
else:
    print "segmento1,up"

 # print("segmento 1 down")
#else:
 #   print("segmento 1 up")
#print stdout.readlines() #vê a saída do comando
