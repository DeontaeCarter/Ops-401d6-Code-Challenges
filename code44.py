#!/user/bin/python3
# Script: Ops 401 Class 44 Code Challenge
# Deontae Carter
# 6/12/2023
# Purpose: Create a Port Scanner

#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5  # TODO: Set a timeout value here, for example, 5 seconds.
sockmod.settimeout(timeout)

hostip = input("Enter the host IP: ")  # TODO: Collect a host IP from the user.
portno = int(input("Enter the port number: "))  # TODO: Collect a port number from the user, then convert it to an integer data type.

def portScanner(portno):
    if sockmod.connect_ex((hostip, portno)) == 0:  # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the socket docs.
        print("Port open")
    else:
        print("Port closed")

portScanner(portno)


