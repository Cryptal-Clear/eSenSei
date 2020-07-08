import requests
from bs4 import BeautifulSoup
import csv
import urllib.request

# getting IP address
def getIP(domain):
    url = "https://domainbigdata.com/"
    page = urllib.request.Request(url+domain, headers={'User-Agent': 'Mozilla/5.0'})
    infile = urllib.request.urlopen(page).read()
    soup = BeautifulSoup(infile, features="html.parser")
    try:
        section = soup.find("tr", {"id":"trIP"})
        anchor = section.find("a")
        ip = anchor.get("href")[1:]
        getGeo(ip)
    except:
        try:
            getGeo(domain)
        except:
            print("This didn't work for",domain)

# getting geographic details
def getGeo(ip):
    parameters = {"ip": ip}
    response = requests.post("https://www.ipaddress.my/", data = parameters)
    soup = BeautifulSoup(response.text, 'html.parser')

    res = {"Hostname:":"","Domain Name:":"","ISP:":"","City:":"","Country:":"","Latitude:":"","Longitude:":"","ZIP Code:":"","Area Code:":""}

    for i in res:
        res[i] = soup.find("td", text=i).find_next_sibling("td",text=True)
        if res[i]!=None:
            res[i] = res[i].get_text()

    res["Domain Name:"] = soup.find("td", text="Domain Name:").find_next().findChild("a")
    if res["Domain Name:"]!=None:
        res["Domain Name:"] = res["Domain Name:"].get_text()

    r = []
    for i in res:
        r.append([i,res[i]])
    r.append(["IP Address:",ip])
    write_to_file(r,ip)

def write_to_file(r,ip):
    file = open('C:\\My Schtuff\\SITE Stuff\\Gurgaon Police Internship\\Project\\results.csv', 'a+', encoding='utf-8', newline='')
    with file:
        write = csv.writer(file)
        write.writerows([[ip],[""]])
        write.writerows(r)
        write.writerows([[""], [""]])

store = open('C:\\My Schtuff\\SITE Stuff\\Gurgaon Police Internship\\Project\\results.csv', 'w+', encoding='utf-8', newline='')
domains = set()

with open('C:\\My Schtuff\\SITE Stuff\\Gurgaon Police Internship\\Project\\weird.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        if i[1]=="URL":
            continue
        domains.add(i[1])

url = list(domains)

for i in url:
    getIP(i)
print("\n\nResults saved in results.csv")












