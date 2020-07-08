import requests
from bs4 import BeautifulSoup
import csv
import urllib.request
import safebrowsing





key = 'YOUR_API_KEY'
URL = "https://sb-ssl.google.com/safebrowsing/api/lookup?client=api&apikey={key}&appver=1.0&pver=3.0&url={url}"


def is_safe(key, url):
    response = requests.get(URL.format(key=key, url=url))
    return response.text != 'malware'

print(is_safe(key, 'http://malware.io'))  # prints False
print(is_safe(key, 'http://google.com'))  # prints True


# apikey = 'YOUR_API_KEY'
# sb = safebrowsing.LookupAPI(apikey)
# resp = sb.threat_matches_find('www.youtube.com')
# print(resp)
#





# apikey = 'YOUR_API_KEY'
# parameters = {"client":apikey,"threatInfo": "www.google.com"}
# response = requests.post("https://safebrowsing.googleapis.com/v4/threatMatches:find?key="+apikey)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)






# from gglsbl import SafeBrowsingList
# sbl = SafeBrowsingList('YOUR_API_KEY')
# threat_list = sbl.lookup_url('http://github.com/')
# if threat_list == None:
#     print("no threat")
# else:
#     print('threats: ' + str(threat_list))