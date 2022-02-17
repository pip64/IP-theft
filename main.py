import os
import time


print("╔══╦═══╦════╦╗╔╦═══╦══╦════╗\n╚╗╔╣╔═╗╠═╗╔═╣║║║╔══╣╔═╩═╗╔═╝\n─║║║╚═╝║─║║─║╚╝║╚══╣╚═╗─║║\n─║║║╔══╝─║║─║╔╗║╔══╣╔═╝─║║\n╔╝╚╣║────║║─║║║║╚══╣║───║║\n╚══╩╝────╚╝─╚╝╚╩═══╩╝───╚╝")
print("iptheft version 1.0.1")
time.sleep(0.3)
print("wait...")
time.sleep(0.7)
print("Welcome!")
wuse = input("Where are you launching from?\n1. local\n2. replit.com\n> ")
#start local
def startlocal():
    port = input("Port?\n> ")
    time.sleep(2)
    print("Succefully! 127.0.0.1:" + str(port))
    print("If you want to throw this link to the enemy - use ngrok TCP(ngrok.com)")
    os.system("php -S 127.0.0.1:" + str(port) + " -f index.php")
#start repl
def startrepl():
    print("Wait...")
    os.system("php -S 0.0.0.0:8000 -t .")
#if wuse = local or Local or replit or Replit or replit.com
if wuse == "local":
	startlocal()
elif wuse == "Local":
	startlocal()
elif wuse == "replit":
	startrepl()
elif wuse == "Replit":
	startrepl()
elif wuse == "replit.com":
	startrepl()
elif wuse == "Replit.com":
	startrepl()
elif wuse == "2":
	startrepl()
else:
	print("Error!")
