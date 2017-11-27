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
    stdin, stdout, stderr = ssh.exec_command('ping -c 1 ' + ip + ' -q\n')
    segmento= stdout.read()
#    print segmento
    Segmento_Teste_Interface_Remota=int(re.findall(r'(\d+)%',segmento)[0])
#    print Segmento_Teste_Interface_Remota
    return Segmento_Teste_Interface_Remota != 100
#return Segmento_Teste_Interface_Local_Down !=
TopologiaUpR1 = [ip for ip in Topologia_Roteador_R1_Padrao if probe_ok(ip)]
#print "TOPOLOGIA R1:\n"
print TopologiaUpR1
