#!/bin/usr/python
#coding: utf-8
import netifaces as redesegmento1 #biblioteca extrai informações de interfaces
import sys   #usa metodos como stdout,stdin
import os
redesegmento1.ifaddresses('eth0') # target interface eth0
ip1 = redesegmento1.ifaddresses('eth0')[redesegmento1.AF_INET][0]['addr'] #filtrando informação de ip - eth0
#with open('test1','w') as f:
# sys.stdout=f
redesegmento1.ifaddresses('eth1') # target interface eth1
ip2 = redesegmento1.ifaddresses('eth1')[redesegmento1.AF_INET][0]['addr'] #filtrando informações de ip - eth1
redesegmento1.ifaddresses('eth2') #target interface eth2
ip3 = redesegmento1.ifaddresses('eth2')[redesegmento1.AF_INET][0]['addr'] #filtrando informações de ip - eth2
with open('tabelacontroladora','w') as f1: #abrindo arquivo a ser populado com ips
 sys.stdout=f1 # metodo stdout invocado da biblioteca sys
 print ip1,"\n",ip2,"\n",ip3  #  popular arquivo para ping

#PARA FAZER SPLIT EM IP ---
#mudando ip para pingar--nessario separar octeto e alterar o ultimo
#segmento1
#for ip1 in tabe
#transIp = ip1.split('.')
#if(len(transIp) is 4):
#  print ip1
#---------------
#Metodos de print antigos
# print "Eth0:",ip1,"\nEth1:",ip2,"\nEth2:",ip3  # ip 1 da interface populado em test1
# print ip2  # ip 2 da interface populado em test1
# print ip3  # ip 3 da interface populado em test1



#Author:By Daniel Facuri Cardoso  - gplv2 licence.
