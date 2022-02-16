import os
import time


print("╔══╦═══╦════╦╗╔╦═══╦══╦════╗\n╚╗╔╣╔═╗╠═╗╔═╣║║║╔══╣╔═╩═╗╔═╝\n─║║║╚═╝║─║║─║╚╝║╚══╣╚═╗─║║\n─║║║╔══╝─║║─║╔╗║╔══╣╔═╝─║║\n╔╝╚╣║────║║─║║║║╚══╣║───║║\n╚══╩╝────╚╝─╚╝╚╩═══╩╝───╚╝")
vo = input("Variant?\n1. local\n> ")
def local():
    port = input("Port?\n> ")
    time.sleep(2)
    print("Succefully! 127.0.0.1:" + str(port))
    print("If you want to throw this link to the enemy - use ngrok TCP(ngrok.com)")
    os.system("php -S 127.0.0.1:" + str(port) + " -f code/index.php")
if vo == "local":
    local()
elif vo == "Local":
    local()
elif vo == "1":
    local()
else:
    print("Error!")


