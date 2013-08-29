#!/usr/bin/python

from socket import*
from cmd import*

##prompt = cmd.Cmd()

cnt = socket(AF_INET,SOCK_DGRAM)

status = 1 

while status == 1:

    open_ports = []
    closed_ports = []
    timed_out = []
    host = raw_input("enter host ip or hostname: ")
    ip = gethostbyname(host)
    t = int(raw_input("times out in : "))
    cnt.settimeout(t)
    first_port = int(raw_input("enter 1st port to scan: "))
    last_port = int(raw_input("enter last port to scan: "))

    for port in range(first_port,last_port):

                print("connecting to "+str(ip)+" on port "+str(port))
                result = cnt.connect_ex((ip,port))
                if result == 0:
                    open_ports.append(port)
##                    cnt.close()
##                elif result !=0:
##                    closed_ports.append(port)
##                    cnt.close()
                elif timeout :
                    timed_out.append(port)
                    cnt.close()

    print ("Closed ports are"+str(closed_ports))

    print ("open ports are"+str(open_ports))
	
	
	
	
		

