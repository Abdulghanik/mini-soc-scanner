#!/usr/bin/python3

import os
import ipaddress
import socket




print ("Welcome to Mini-SOC Vulnerability Engine!")
print ("Author: Abdulghani ")
print ("*****************************************\n")
stars = "*****************************************\n"

#10.0.0.126

print ("Enter the IP/URL to Start Scan: ")
ip = input()

# declare result string var
fdesc = open("result.txt", "w")
fdesc.write(stars + "\n")

print("*****************************************\n")

print("Test if WAF is implemented on website or not.. using wafw00f tool")
fdesc.write("Test if WAF is implemented on website or not.. using wafw00f tool" + "\n")
fdesc.close()

result = os.system("wafw00f http://" +(ip) + ">> result.txt \n")
fdesc = open("result.txt", "a")
print ("WAF Scan is Fininshed")
fdesc.write("WAF Scan is Fininshed" + "\n")
print("*****************************************\n")
fdesc.write(stars + "\n")

#ssl scanning using sslscan tool for vulnerabilities of ssl
print("SSL Scan Vulnerabilities Check...")
fdesc.write("SSL Scan Vulnerabilities Check..." + "\n")
fdesc.close()
result+= os.system("sslscan " +(ip) + ">> result.txt \n")
fdesc = open("result.txt","a")


print ("SSL Scan is Fininshed")
print("*****************************************\n")
fdesc.write(stars + "\n")

try:

	#wordpress scanning framework
	print("Wordpress Scan Vulnerabilities and Plugin Check...")
	fdesc.write("Wordpress Scan Vulnerabilities and Plugin Check..." + "\n")
	fdesc.close()
	result+= os.system("wpscan --disable-tls-checks  -v -e --url " +(ip) + ">> result.txt \n")
	fdesc = open("result.txt","a")


	print ("Wordpress Scan is Fininshed")
	print("*****************************************\n")
	fdesc.write(stars + "\n")

except:
	print("The Given is not URL format, Please only insert URL format")
	fdesc.write("Wordpress Scan Vulnerabilities and Plugin Check..." + "\n")
	print("*****************************************\n")
	fdesc.write(stars + "\n")

#parsing ip from URL string to IP type
data = socket.gethostbyname(ip)

# parsing ip from string to IP type
ip = (ipaddress.ip_address(data))


print ("Scanning for FTP Port and Vulnerability")
#Scan port 21 is open first then if not skip bruteforce and scan this port to save time of process
try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((ip, 21))
	if result != 0:
		print ("Port 21 FTP : 	 Close")
		fdesk.write("Port 21 FTP : is Close" + "\n")
	sock.close()
except:

	fdesc.write("Scanning for FTP Port and Vulnerability" + "\n")
	fdesc.close()
	#FTP nmap command in terminal
	result= os.system("nmap -sV -p21  --script ftp-proftpd-backdoor %d" %(ip) + ">> result.txt \n")

	fdesc = open("result.txt","a")
	print ("Scanning FTP Completed !!!")
	fdesc.write("++ Scanning FTP Completed !!!" + "\n")

	print("***************************************** \n")
	fdesc.write(stars + "\n")

print ("Scanning for telnet Port and Vulnerability")
fdesc.write("Scanning for telnet Port and Vulnerability" + "\n")
fdesc.close()
#telnet nmap command in terminal
result+= os.system("nmap -sV -p23  %d" %(ip) + ">> result.txt \n")

# os.system("telnet %d" %(ip) +' \n')
fdesc = open("result.txt","a")
print ("Scanning Telnet Completed !!!")
fdesc.write("Scanning Telnet Completed !!!" + "\n")


print("*****************************************\n")
fdesc.write(stars + "\n")

print ("Scanning for SMB Port and Vulnerability (WannaCry Vulnerability) ")

fdesc.write("Scanning for SMB Port and Vulnerability (WannaCry Vulnerability) " + "\n")
fdesc.close()
#smb nmap command in terminal
result+= os.system("nmap --script=smb-os-discovery -p445  %d" %(ip) + " >> result.txt \n")

# os.system("telnet %d" %(ip) +' \n')
fdesc = open("result.txt","a")

print ("Scanning SMB Completed !!!")
fdesc.write("++ Scanning SMB Completed !!!" + "\n")

print("*****************************************\n")
fdesc.write(stars + "\n")


print("WannaCry Attack \n")
fdesc.write("WannaCry Attack " + "\n")
fdesc.close()
result+= os.system("nmap -p445 --script=smb-vuln-ms17-010  %d" %(ip) + ">> result.txt \n")
fdesc = open("result.txt","a")
print ("WannaCry Scan is Fininshed")
fdesc.write("WannaCry Scan is Fininshed" + "\n")

print("*****************************************\n")
fdesc.write(stars + "\n")

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((ip, 21))
	if result != 0:
		print ("Port 21 FTP : 	 Close")
	sock.close()
except:

	print ("Bruteforce FTP with Hydra..")
	fdesc.write("Bruteforce FTP with Hydra.." + "\n")
	fdesc.close()
	result+= os.system("hydra -L user.txt -P pass.txt -I -vV ftp://%d" %(ip) + ">> result.txt \n")

	fdesc = open("result.txt","a")
	print ("Bruteforce Attack of FTP Completed!")
	fdesc.write("++ Bruteforce Attack of FTP Completed!" + "\n")

print("*****************************************\n")
fdesc.write(stars + "\n")

print ("Bruteforce SSH with Hydra..")
fdesc.write("Bruteforce SSH with Hydra.." + "\n")
fdesc.close()
result+= os.system("hydra -L user.txt -P pass.txt -I -vV ssh://%d" %(ip) + ">> result.txt \n")
fdesc = open("result.txt","a")
print ("Bruteforce of SSH Completed!")
fdesc.write("++Bruteforce of SSH Completed!" + "\n")


print("*****************************************\n")
fdesc.write(stars + "\n")

#ssl scan for cipher lenghth check
print("SSL Scan Cipher Check...set IP only For Website in port 443")
fdesc.write("SSL Scan ...set IP only For Website at port 443" + "\n")
fdesc.close()
result+= os.system("nmap --script ssl-enum-ciphers -p443 %d" %(ip) + ">> result.txt \n")
fdesc = open("result.txt","a")



print ("SSL Scan is Fininshed")
fdesc.write("SSL Scan is Fininshed" + "\n")
print("*****************************************\n")
fdesc.write(stars + "\n")



print("End of Scan \n")
fdesc.write("End of Scan" + "\n")
fdesc.close()
