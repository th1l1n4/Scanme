#!/bin/python3

import sys
import socket
from datetime import datetime

#Define the Target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 scanme.py <ip>")
	
#Add a banner
print("- " * 20)
print("Scaning target "+target)
print("Time started: "+str(datetime.now()))
print("- " * 20)

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #return an error indicator
#		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
	

