#!/bin/usr/env  python
#!coding: utf-8
import paramiko
import os
import subprocess
import sys
import re
import networkx as nx

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.3.2')
stdin, stdout, stderr = ssh.exec_command('python /root/comandgeral3.py')

listaTopologia = open("arquivoTopologia.txt",'r')

G = nx.DiGraph()

### 2 - CARREGAR O OBJETO DO NETWORKX
for linha in listaTopologia:
    maquinaAtual = linha.split(',')
    origem = str(maquinaAtual[0]).strip()
    destino = str(maquinaAtual[1]).strip()
    peso = int(str(maquinaAtual[2]).strip())
    G.add_edges_from([(origem,destino)], weight=peso)
    G.add_edges_from([(destino,origem)], weight=peso)

### 4 - EXIBE MENOR CAMINHO
print(nx.dijkstra_path(G, 'H_R2', 'H_R3'))
