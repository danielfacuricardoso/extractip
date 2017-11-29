#!/bin/usr/env  python
#!coding: utf-8
import paramiko
import os
import subprocess
import sys
import re
#Autenticação R1
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.3.2')
#Fim da Autenticação R1
#Iniciando criação da Topologia - Roteador 1
Topologia_Roteador_R1_Padrao = ['192.168.0.2','192.168.0.14','192.168.0.18','192.168.3.1']
def probe_ok(ip):
    stdin, stdout, stderr = ssh.exec_command('ping -c 1 ' + ip + ' -q')
    segmento= stdout.read()
    if (len(segmento)==0):
       segmento='100'
    else:
#    print segmento
        Segmento_Teste_Interface_Remota=int(re.findall(r'(\d+)%',segmento)[0])
#    print Segmento_Teste_Interface_Remota
    return Segmento_Teste_Interface_Remota != 100
#TOPOLOGIA R1
TopologiaUpR1 = [ip for ip in Topologia_Roteador_R1_Padrao if probe_ok(ip)]
#print TopologiaUpR1
#TOPOLOGIA R2

stdin, stdout, stderr = ssh.exec_command('python /root/comand7R2.py')
TOPOLOGIA_R2=stdout.read().rstrip('\n').replace('[','').replace('"','').replace(' ','').replace(']','').replace('\'','').split(",")
#print TOPOLOGIA_R2
#print type(TOPOLOGIA_R2)
#TOPOLOGIA R3
stdin, stdout, stderr = ssh.exec_command('python /root/comand7R3.py')
TOPOLOGIA_R3= stdout.read().rstrip('\n').replace('[','').replace('"','').replace(' ','').replace(']','').replace('\'','').split(",")
#TOPOLOGIA R4
stdin, stdout, stderr = ssh.exec_command('python /root/comand7R4.py')
TOPOLOGIA_R4= stdout.read().rstrip('\n').replace('[','').replace('"','').replace(' ','').replace(']','').replace('\'','').split(",")
## TOPOLOGIAGERAL ##
TOPOLOGIAGERAL=[TopologiaUpR1,TOPOLOGIA_R2,TOPOLOGIA_R3,TOPOLOGIA_R4]
print TOPOLOGIAGERAL
#print type(TOPOLOGIAGERAL[1])
#print TOPOLOGIAGERAL[1]



