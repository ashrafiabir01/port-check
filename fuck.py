# op = 1


# with open("ip.txt") as foo:
#     lines = len(foo.readlines())
#     print(lines)

# for i in range (lines) :


#     print ("biva ", op)

#     op = op+1

import pyfiglet 

import sys 

import socket 

from datetime import datetime 
port = 5678

bal = open('ip.txt').read().splitlines()

ascii_banner = pyfiglet.figlet_format("PORT SCANNER") 

print(ascii_banner) 
with open("ip.txt") as foo:

    lines = len(foo.readlines())
    to = 1
# Defining a target 

if len(sys.argv) == 2: 

      

    # translate hostname to IPv4 

    target = socket.gethostbyname(sys.argv[1])  

else: 

    print("Invalid ammount of Argument") 

  
# Add Banner  

print("-" * 50) 

#print("Scanning Target: " + target) 

print("Scanning started at:" + str(datetime.now())) 

print("-" * 50) 

   

try: 

      

    # will scan ports between 1 to 65,535 

    for target in bal : 
         
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

        socket.setdefaulttimeout(1) 

          

        # returns an error indicator 

        result = s.connect_ex((target,port))
 
        print ("fuck no ", to)
        to = to+1
        if result ==0: 

            print (target+ " hurry")
            open ("hurry.txt" , "a").write (target + "\n")
        s.close() 


except KeyboardInterrupt: 

        print("\n Exitting Program !!!!") 

        sys.exit() 

except socket.gaierror: 

        print("\n Hostname Could Not Be Resolved !!!!") 

        sys.exit() 

except socket.error: 

        print("\ Server not responding !!!!") 

        sys.exit()