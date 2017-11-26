#!/usr/bin/env python
#1) monstar topologia
#2) testar ping via ssh
#3) executar script melhor caminho
#4) gravar em todas a interfaces
#scp antonio@192.168.1.150:/home/antonio/desenvolvimento/clonadosTeste/extractip/unbTesteSdn/* /root/extractip/unbTesteSdn


import paramiko
### 1 - IMPORTAR ARQUIVO COM A TOPOLOGIA
listaTopologia = open("listaIPs.txt",'r')
listaAtivos = []

### 2 - DECLARA PARAMIKO
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

### 3 - TESTA AS MAQUINAS
for linha in listaTopologia:
    maquinaAtual = linha.split(',')
    if(len(maquinaAtual) is 3):
        try:
            ip = str(maquinaAtual[0])
            usuario = str(maquinaAtual[1])
            senha = str(maquinaAtual[2])
            senha = senha[0:len(senha)-1]
            ssh.connect(ip, username=usuario, password=senha)
            listaAtivos.append(maquinaAtual)
        except (IOError,TypeError) as erro:
            print(erro)
listaTopologia.close()
ssh.close()
### 4 - MOSTRA AS MAQUINAS ATIVAS
print('MAQUINAS ATIVAS')
for maquina in listaAtivos:
    print(maquina)

####TOPOLOGIA
#controlador 192.168.3.1  root admin123daniel
#roteador1 192.168.3.2  root admin
#roteador4 192.168.0.18  root admin
#roteador2 192.168.0.2  root admin -> host1 192.168.1.2 root admin
#roteador3 192.168.0.14  root admin -> host2 192.168.2.2 root admin
