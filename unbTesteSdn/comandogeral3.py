#!/bin/usr/env  python
#!coding: utf-8
import paramiko
import os
import subprocess
import sys
import re

def probe_ok(ip, posicao):
    stdin, stdout, stderr = ssh.exec_command('ping -c 1 ' + ip + ' -q')
    segmento= stdout.read()
    if (len(segmento)==0):
        return listaNetX[posicao+len(topologiaPadrao)]
    else:
        testSegmento=int(re.findall(r'(\d+)%',segmento)[0])
        return listaNetX[posicao + 0 if testSegmento != 100 else posicao + len(topologiaPadrao) ]

# Abra o arquivo (leitura)
arquivo = open('arquivoTopologia.txt', 'w')
arquivo.close()

arquivo = open('arquivoTopologia.txt', 'r') # Abra o arquivo (leitura)
conteudo = arquivo.readlines()

listaCompleta = []
######TOPOLOGIA_R1
topologiaPadrao = ['192.168.3.1','192.168.0.2','192.168.0.14','192.168.0.18']
listaNetX = ['CRT,R1,9', 'R1,R2,2', 'R1,R3,4','R1,R4,6', 'CRT,R1,900', 'R1,R2,200', 'R1,R3,400','R1,R4,600','teste']
posicao = 0
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.3.2')
for ip in topologiaPadrao:
    resultado = probe_ok(ip,posicao)
    listaCompleta.append(resultado)
    posicao+=1
    conteudo.append(resultado+'\n')
ssh.close()
######TOPOLOGIA_R2
topologiaPadrao = ['192.168.0.1','192.168.0.5','192.168.0.2']
listaNetX = ['R2,R1,2', 'R2,R4,2', 'R2,H_R2,9','R2,R1,200', 'R2,R4,200', 'R2,H_R2,900']
posicao = 0
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.2')
for ip in topologiaPadrao:
    resultado = probe_ok(ip,posicao)
    listaCompleta.append(resultado)
    posicao+=1
    conteudo.append(resultado+'\n')
ssh.close()

######TOPOLOGIA_R3
topologiaPadrao = ['192.168.0.13','192.168.0.9','192.168.2.2']
listaNetX = ['R3,R1,4', 'R3,R4,3', 'R3,H_R3,9','R3,R1,400', 'R3,R4,300', 'R3,H_R3,900']
posicao = 0
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.14')
for ip in topologiaPadrao:
    resultado = probe_ok(ip,posicao)
    listaCompleta.append(resultado)
    posicao+=1
    conteudo.append(resultado+'\n')
ssh.close()
######TOPOLOGIA_R4
topologiaPadrao = ['192.168.0.17','192.168.0.6','192.168.0.10']
listaNetX = ['R4,R1,6', 'R4,R2,2', 'R4,R3,3','R4,R1,600', 'R4,R2,200', 'R4,R3,300']
posicao = 0
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.18')
for ip in topologiaPadrao:
    resultado = probe_ok(ip,posicao)
    listaCompleta.append(resultado)
    posicao+=1
    conteudo.append(resultado+'\n')
ssh.close()
# Abre novamente o arquivo (escrita)
# e escreva o conteúdo criado anteriormente nele.
arquivo = open('arquivoTopologia.txt', 'w')
arquivo.writelines(conteudo)
arquivo.close()

path = "/root/arquivoTopologia.txt"
os.system("scp "+path+" root@192.168.3.1:"+path)
