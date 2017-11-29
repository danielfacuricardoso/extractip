#!/bin/usr/env  python
#!coding: utf-8
import paramiko
import os
import subprocess
import sys
import re
#Autenticação R4
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.18')
#Nescessário configurar uma quebra como if no stdout no ssh caso a interface de R1 PRA R4 ESTEJA DOWN realizar ssh por outro caminho
#Fim da Autenticação R4
#Iniciando criação da Topologia - Roteador 4
Topologia_Roteador_R4_Padrao = ['192.168.0.17','192.168.0.10','192.168.0.6']
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
#TOPOLOGIA R4
TopologiaUpR4= [ip for ip in Topologia_Roteador_R4_Padrao if probe_ok(ip)]
print TopologiaUpR4
