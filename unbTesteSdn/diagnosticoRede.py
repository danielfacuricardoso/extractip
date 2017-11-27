#!/usr/bin/env python
#coding: utf-8
import paramiko
import os
import subprocess
import sys
import re
import time

#CONECTANDO VIA SSH COM O CONTROLADOR
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.24', username='root', password='123')
canal = ssh.invoke_shell()
canal.settimeout(3)
listaComandosSSH = open("listaComandosSSH.txt",'r')
for linha in listaComandosSSH:
    if(linha.startswith('#')):
        continue
    print 'comando: '+linha
    comandoAtual = linha.split(',')
    buff = ''
    try:
        if(len(comandoAtual) == 1):
            param1 = str(comandoAtual[0])
            # EXECUTA COMANDO ping e AGUARDA ':~# ' OU TIMEOUT
            canal.send(param1)
            buff = ''
            while not buff.endswith(':~# '):
                resp = canal.recv(9999)
                buff += resp
            # EXIBE O CONTEUDO DA VARIAVEL 'buff'
            if(linha.startswith('ping')):
                buff=int(re.findall(r'(\d+)%',buff)[0])
        if(len(comandoAtual) == 2):
            param1 = str(comandoAtual[0])
            param2 = str(comandoAtual[1])
            #SSH E HOST E AGUARDA A SENHA COM MSG 's password:'  OU TIMEOUT
            canal.send(param1+'\n')
            buff = ''
            while not buff.endswith('\'s password: '):
                resp = canal.recv(9999)
                buff += resp
            #ENVIA A SENHA E AGUARDA  OU TIMEOUT
            canal.send(param2)
            buff = ''
            while not buff.endswith(':~# '):
                resp = canal.recv(9999)
                buff += resp
    except (IOError,TypeError) as erro:
        print(erro)
    if(not linha.startswith('ssh')):
        print 'buff', buff
listaComandosSSH.close()
ssh.close()
