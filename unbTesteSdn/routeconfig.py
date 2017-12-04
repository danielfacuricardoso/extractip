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
ssh.connect('192.168.3.2')
canal = ssh.invoke_shell()
canal.settimeout(2)
listaComandosSSH = open("arquivorouteconfig.txt",'r')
sshFalhou = False;
print '...INICIO EXECUCAO COMANDOS...'
for linha in listaComandosSSH:
    if(linha.startswith('#')):
        continue
    print 'comando: '+linha
    buff = ''
    try:
        timeout = time.time() + 2
        if(len(linha) == 1):
            param1 = str(linha[0])
            # EXECUTA COMANDO ping e AGUARDA ':~# ' OU TIMEOUT
            canal.send(param1)
            buff = ''
            while not buff.endswith(':~# '):
                resp = canal.recv(9999)
                if time.time() > timeout:
                    buff = '100'
                    break
                buff += resp
    except Exception as erro:
        print(erro)
    #print 'buff', buff
listaComandosSSH.close()
ssh.close()
print '...FINAL EXECUCAO COMANDOS...'
