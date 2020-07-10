print("--"*30)
print("\nCHANGING MAC ADDRESS WITH PYTHON\n")
print("--"*30)
print("by Kurrupt68\n twitter: @ayokunle_al \n github:" )

#run with python3 ; python3 machange.py

import re #import regular expression
import subprocess #imoport subrocess
from random import choice , randint

interface = input("Enter the interface you would like to change: ").strip()

def main():
    inp = input("Enter 1 for Manual Changing of mac address , Enter 2 for Random Mac Address : ")
    if inp == "1":
        new_macaddress = input("Enter New Mac Address : ").strip()
        changemac(interface,new_macaddress)
    elif inp == "2":
        random = mac_random()
        print(random)
        changemac(interface,random)
    else :
        print("\n\t\t\tWRONG INPUT")


def mac_random():
    cisco = ["00","40","96"]
    dell = ["00",14,"22"]

    mac_address = choice([cisco,dell])
    for i in range(3):
        one = choice(str(randint(0,9)))
        two = choice(str(randint(0,9)))
        three = one+two
        mac_address.append(three) 
    return ":".join(mac_address)

def changemac(interface,new_macaddress):
    subprocess.call(["ifconfig "+str(interface)+" down"],shell=True)
    subprocess.call(["ifconfig "+str(interface)+" hw ether "+ str(new_macaddress)],shell=True)
    subprocess.call(["ifconfig "+str(interface)+" up"],shell=True)

def currentmac():

#using sub_prorocess to check output 
    output = subprocess.check_output(["ifconfig "+"eth0"],shell=True)
    current_mac= re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(output))
#using regular expression to search
    print(current_mac)

if __name__ == "__main__":
    main()

