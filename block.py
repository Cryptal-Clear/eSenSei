import socket
import csv

# Initialization
i=0
iplist=[]
blacklist=[]

# Read the blacklist csv file and gets the IPs
with open('blacklistdeets.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        i = i + 1
        if i%14 == 1:
            iplist.append(row)

# Gets the url from the IP address using reverse DNS lookup
for ip in iplist:
#    print(ip)
    try:
        url = socket.gethostbyaddr(ip[0])
        blacklist.append(url[0])
    except:
        print("URL not found")

#    print(url[0])
#    blacklist.append(url[0])

#Path to the system blacklist file
filepath = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

#Adding the URLs obtained to the system blacklist
with open(filepath, 'a') as file:
    for url in blacklist:
        file.write(redirect+" "+url+"\n")

#The sites in the blacklist should be blocked now
