
#if estadosegr2 is not 0:
if estador2seg2 is not 100:
    TopologiaR2.append('192.168.0.5')
    del TopologiaR2down('192.168.0.5')
    print "Segmento 2 de R2 UP, inserindo IP abaixo na Topologia de R2:\n"
    print  TopologiaR2
#    RemoveIpSeg1=int(re.findall(r'(\d+)5',TopologiaR2)[0])
else:
   TopologiaR2down.append('192.168.0.5')
   remover = [TopologiaR2 = re.compile(".*192.168.0.5")filter(r.match, TopologiaR2)]
   elif remover = ('192.168.0.5'): TopologiaR2.remove('192.168.0.5')
   print "Segmento 2 de R2 Down,removido IP de R2\n"
   print TopologiaR2down
#   elif
----

