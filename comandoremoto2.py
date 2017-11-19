#!/usr/bin/env python
#coding: utf-8
import paramiko
import os
import subprocess
import sys
import re
TopologiaR1=['192.168.0.2','192.168.0.14','192.168.0.18','192.168.3.1']
TopologiaR2=[]
TopologiaR2down=[]
TopologiaR3=[]
TopologiaR3down=[]
#TopologiaR4   Router1        Router3        Router2
TopologiaR4=['192.168.0.17','192.168.0.10','192.168.0.6']
l=[['r1','r2',0],['r2','r4',1]]
#Topologia
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#stdin, stdout, stderr = ssh.exec_command('ssh 192.168.3.2')
#ssh.connect('192.168.3.2', username='root', password='admin')
ssh.connect('192.168.3.2')
stdin, stdout, stderr = ssh.exec_command('ping -c 1 192.168.0.2 -q\n')  # pode ser redirecionado ou$
a1= stdout.read()
print a1
stdin, stdout, stderr = ssh.exec_command('ping -c 1 192.168.0.14 -q\n')
a2= stdout.read()
print a2
stdin, stdout, stderr = ssh.exec_command('ping -c 1 192.168.0.18 -q\n')
a3= stdout.read()
print a3
estadoseg1=int(re.findall(r'(\d+)%',a1)[0])
estadoseg4=int(re.findall(r'(\d+)%',a2)[0])
estadosegrouter4=int(re.findall(r'(\d+)%',a3)[0])
#estadoseg1=int(a.split('\n')[3].split(',')[2].split(" ")[1][:-1])
#estadoseg1=int(a.split('\n')[3].split(',')[2].split(" ")[1][:-1])
#seg1ip = "192.168.0.2"
#estadoseg1 = os.system("ping %s -c 2" % seg1ip)
if estadoseg1 is not 0:
    TopologiaR1=['192.168.0.14','192.168.0.18','192.168.3.1']
    print "Segmento 1 Down:192.168.0.1-192.168.0.2"
    print TopologiaR1
else:
    TopologiaR1=['192.168.0.2','192.168.0.14','192.168.0.18','192.168.3.1']
    print "Segmento 1 Up:192.168.0.1-192.168.0.2, Topologia Atual:\n"
    print TopologiaR1

#    l[0][2]=1
#else:
#    l[0][2]=0
#if l[0][2]  is not 0:
#    print "segmento1,down"
#else:
#    print "segmento1,up"
if estadoseg4 is not 0:
#    l[0][2]=1
#else:
#    l[0][2]=0
#if l[0][2]  is not 0:
    print "segmento4,down"
else:
    print "segmento4,up"
if estadosegrouter4 is not 0:
#    l[0][2]=1
#else:
#    l[0][2]=0
#if l[0][2]  is not 0:
    print "segmentorouter4,down"
else:
    print "segmentorouter4,up"

# print("segmento 1 down")
#else:
#   print("segmento 1 up")
#print stdout.readlines() #vê a saída do comando
# validando router 2
#ssh.connect('192.168.0.2', username='root', password='admin')
stdin, stdout, stderr = ssh.exec_command('ssh 192.168.0.2 ')
#segmento1
stdin, stdout, stderr = ssh.exec_command('ping -c 1 192.168.0.1 -q\n')  # pode ser red$
ar2seg1= stdout.read()
print ar2seg1
#segmento6
stdin, stdout, stderr = ssh.exec_command('ping -c 1 192.168.0.2 -q\n')
ar2seg6= stdout.read()
print ar2seg6
#segmento 2
stdin, stdout, stderr = ssh.exec_command('ping -c 1 192.168.0.5 -q\n')
ar2seg2= stdout.read()
print ar2seg2
#estadoseg router 2
estador2seg1=int(re.findall(r'(\d+)%',ar2seg1)[0])
estador2seg6=int(re.findall(r'(\d+)%',ar2seg6)[0])
estador2seg2=int(re.findall(r'(\d+)%',ar2seg2)[0])
#RemoveIpSeg1=int(re.findall(r'(\d+).',TopologiaR2)[0])
if estador2seg1 is not 0:
   TopologiaR2.remove('192.168.0.1')
   print "Segmento 1 de R2 Down\n"
   print TopologiaR2
else:
    TopologiaR2.append('192.168.0.1')
    print "Segmento 1 de R2 UP, inserindo IP abaixo na Topologia de R2:\n"
    print  TopologiaR2
#if estadosegr2 is not 0:
if estador2seg2 is not 100:
    TopologiaR2.append('192.168.0.5')
    del TopologiaR2down('192.168.0.5')
    print "Segmento 2 de R2 UP, inserindo IP abaixo na Topologia de R2:\n"
    print  TopologiaR2
#    RemoveIpSeg1=int(re.findall(r'(\d+)5',TopologiaR2)[0])
else:
   TopologiaR2down.append('192.168.0.5')
   remover = [TopologiaR2 = re.compile(".*192.168.0.5")filter(r.match, TopologiaR2)]
   elif remover = ('192.168.0.5'): TopologiaR2.remove('192.168.0.5')
   print "Segmento 2 de R2 Down,removido IP de R2\n"
   print TopologiaR2down
#   elif
