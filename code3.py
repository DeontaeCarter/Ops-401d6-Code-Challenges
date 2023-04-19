#!/usr/bin/env python3

# Deontae Carter 4/19/23
# Script: Uptime Sensor Tool Part 2
# https://www.w3schools.com/python/python_datetime.asp, https://github.com/codefellows/seattle-ops-401d6/blob/main/class-02/challenges/DEMO.md, ChatGPT


import os
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Function to send notification email
def send_email(admin_email, subject, message):
    burner_email = "dwrightshrute@gmail.com"
    burner_password = "codefellows1234"
    msg = MIMEText(message)
    msg['From'] = burner_email
    msg['To'] = admin_email
    msg['Subject'] = subject
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(burner_email, burner_password)
        smtp.send_message(msg)

# Get user input for IP address and email account details
ip_address = input("10.0.0.244 ")
admin_email = input("dwrightshrute@gmail.com: ")
burner_password = input("codefellows1234: ")

# Set initial ping status as "down"
ping_status = "down"

# Monitor the IP address for changes in ping status
while True:
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    response = os.system("ping -c 1 " + ip_address)
    if response == 0:
        if ping_status == "down":
            ping_status = "up"
            message = f"IP address {ip_address} changed status from down to up at {current_time}"
            subject = f"IP address {ip_address} status changed to up"
            send_email(admin_email, subject, message)
        print(current_time, ip_address, "is up!")
    else:
        if ping_status == "up":
            ping_status = "down"
            message = f"IP address {ip_address} changed status from up to down at {current_time}"
            subject = f"IP address {ip_address} status changed to down"
            send_email(admin_email, subject, message)
        print(current_time, ip_address, "is down!")
    print(current_time, "Ping Status:", ping_status)
    time.sleep(2)
