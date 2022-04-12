#!/usr/bin/python3
import nmap

print("[Info] Herramienta creada para escanear los puertos abiertos de una dirección IP")
print("   ||  Escrito en Python y utiliza Nmap")
print("   ||  Creada por Pingu Chan  >> https://github.com/pingu489")


ip= input("[+] Introduce la IP objetivo: ")
nm= nmap.PortScanner()
puertos_abiertos="-p "
count=0
results= nm.scan(hosts=ip, arguments="-sT -n -Pn -T4")
#print (results)


print("\nHost : %s" % ip)
print("State : %s" % nm[ip].state())
for proto in nm[ip].all_protocols():
    print('Protocol : %s' % proto)
    lport = nm[ip][proto].keys()
    sorted(lport)
    for port in lport:
        print ('port : %s\tstate : %s' % (port, nm[ip][proto][port]['state']))
        if count==0:
            puertos_abiertos= puertos_abiertos+" "+str(ip)
            count=1
        else:
            puertos_abiertos= puertos_abiertos+","+str(ip)

print("\npuertos abiertos: "+puertos_abiertos+" "+ str(ip))      