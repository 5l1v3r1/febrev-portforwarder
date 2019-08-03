import os
os.system("rm /bin/frp")
metasploit=input("IS METASPLOIT-FRAMEWORK ALREADY INSTALLED IN YOUR SYSTEM ? [Y/n] : ")
if metasploit=="n" or metasploit=="N":
            os.sytem("sudo apt-get install metasploit")
else:
     print("NICE ......!")

apksign=input("IS APKSIGNER ALREADY INSTALLED IN YOUR SYSTEM? [Y/n]? : ")
if apksign=="n" or apksign=="N":
           os.system("sudo apt-get install apksigner")
else: 
     print("NICE .....")
     

ssh=input("IS openssh INSTALLED IN YOUR SYSTEM? [Y/n] : ")
if ssh=="n" or ssh=="N":
           os.system("apt-get install openssh")
print("[1] kali linux   [2] Termux ")
Os=int(input("CHOOSE THE OS : "))
if Os==1:
	path=os.getcwd()
	with open("frp.sh","w+") as fr:
		fr.write(f"python3 {path}/frportforward.py")
	os.system(f"cp {path}/frp.sh /bin/frp")
	os.system("chmod +x /bin/frp")
	print("")
	print("NOW YOU CAN RUN FEBREV-VENOM FROM ANYWERE BY TYPING COMMAND  >>  frp")
	exiting=input("ENTER ANY KEY TO CONTINUE.......!!!!! ")
	print(" ")
	print(" ")
	print(" ")
	print("STARTING FEBREV VENOM......#######################")
	os.system("chmod +x *")
	os.system("sudo python3 frportfwd.py")
elif Os==2:
	path=os.getcwd()
	with open("frp.sh","w+") as fr:
		fr.write(f"python3 {path}/frportforward.py")
	os.system(f"cp {path}/frp.sh //data/data/com.termux/files/usr/bin/frp")
	os.system("chmod +x //data/data/com.termux/files/usr/bin/frp")
	print("")
	print("NOW YOU CAN RUN FEBREV-VENOM FROM ANYWERE BY TYPING COMMAND  >>  frp")
	exiting=input("ENTER ANY KEY TO CONTINUE.......!!!!! ")
	print(" ")
	print(" ")
	print(" ")
	print("STARTING FEBREV VENOM......#######################")
	os.system("chmod +x *")
	os.system("sudo python3 frportfwd.py")
	
	
