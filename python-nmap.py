import nmap 

print("--*30")
print("""PYthon-nmap, by  Kurrupt68
twitter : @ayokunle_al\n """ )
print("--"*30)
scanner = nmap.PortScanner()

print("Starting Port Scanner......" )
print("-"*40)
ip_add = input("Enter the Target ip address :" )
print("Target ip address : " + ip_add)

inp = input(""" Enter The Type of scan you would like to perform
        1.) SYN ACK scan 
        2.) UDP scan 
        3.) Comprehnsive Scanning\n""")
if  inp == "1":
    print("StARting SYN ACK SCAN ")
    print("Using nmap version : ", scanner.nmap_version())
    scanner.scan(ip_add,'1-1024','-v -sV')
    print(scanner.scaninfo())
    print("ip status : ",scanner[ip_add].state())
    print(scanner[ip_add].all_protocols() )
    print("open ports : ",scanner[ip_add]['tcp'].keys())

elif inp == "2":
    print("STaRtiNG UDP scan ")
    print("\nUsing Nmap Version: ",scanner.nmap_version())
    scanner.scan(ip_add,'1-1024','-sU')
    print("IP status : ",scanner[ip_add].state())
    print(scanner.scaninfo())
    print(scanner[ip_add].all_protocols())
    print("open ports : " ,scanner[ip_add]['udp'].keys())


elif inp == "3":
    print("sTarting COmprehensive scan")
    print("\nUsing nmap version :",scanner.nmap_version())
    scanner.scan(ip_add,'1-1024','-v -sS -sV -sC -O')
    print(scanner.scaninfo())
    print("IP Status : " ,scanner[ip_add].state()) 
    print(scanner[ip_add].all_protocols())
    print("open ports : ", scanner[ip_add]['tcp'].keys())
    
else :
    print("error wrong input")
