#!bin/usr/env python
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.3.2', username='root', password='admin') # ssh router 1
stdin, stdout, stderr = ssh.exec_command('ping -c 1 192.168.0.14\n')  # pode ser redirecionado para um arquivo ou guardado em um lista
print stdout.readlines() #vê a saída do comando

#obs: pra usar a mesma função do ssh do paramiko de r1-r3 ou r1-r2 é nescessário instalar o paramiko de onde a biblioteca é invocada.
#caso for fazer ssh apartir de stdin,stdout é possível também.
