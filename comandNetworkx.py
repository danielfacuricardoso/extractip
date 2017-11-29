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
###FIM DO PASSO 2
###ÍNICIO DO PASSO 3 - PESO E ROTAS
### 1 - INFORMAR A TOPOLOGIA ATIVA
listaTopologia = []
listaTopologia.append("CTR,R1, 9")
listaTopologia.append("R1, R2, 2")
listaTopologia.append("R1, R3, 4")
listaTopologia.append("R1, R4, 6")
#listaTopologia.append("R2, R4, 2")
listaTopologia.append("R2, H1, 9")
listaTopologia.append("R3, R4, 3")
listaTopologia.append("R3, H2, 9")
G = nx.DiGraph()
### 2 - CARREGAR O OBJETO DO NETWORKX
for linha in listaTopologia:
    maquinaAtual = linha.split(',')
    origem = str(maquinaAtual[0]).strip()
    destino = str(maquinaAtual[1]).strip()
    peso = int(str(maquinaAtual[2]).strip())
    G.add_edges_from([(origem,destino)], weight=peso)
    G.add_edges_from([(destino,origem)], weight=peso)
### 3 - EXIBE MENOR CAMINHO
print(nx.dijkstra_path(G, 'H1', 'H2', weight='weight')


