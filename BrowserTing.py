import browserhistory as bh
import sqlite3
import pandas as pd
import csv


"""         Storing the browser history in a .csv file          """

# con = sqlite3.connect('C:\\Users\\chintu\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')
# c = con.cursor()
#
# columns = [["URL", "Title", "Visit Count", "Last Visit Time"]]
# c.execute("select url, title, visit_count, last_visit_time from urls") #urls,keyword_search_terms
# results = c.fetchall()
#
# c.close()
#
# file = open('C:\\My Schtuff\\SITE Stuff\\Gurgaon Police Internship\\Project\\history.csv', 'w+', encoding='utf-8', newline='')
# with file:
#     write = csv.writer(file)
#     write.writerows(columns)
#
# for r in results:
#     r = list(r)
#     for i in range(len(r)):
#         if isinstance(r[i], int):
#             r[i] = str(r[i])
#
# file = open('C:\\My Schtuff\\SITE Stuff\\Gurgaon Police Internship\\Project\\history.csv', 'a+', encoding='utf-8', newline='')
# with file:
#     write = csv.writer(file)
#     write.writerows(results)

"""         this code needs to be run just once to get the Browser History File          """

#########################################################################

"""         Blacklisting part           """

def clean_url(s):
    x = s.find("/")
    s = s[x+2:s.find("/", x+2)]
    return s

blacklisting = open('C:\\My Schtuff\\SITE Stuff\\Gurgaon Police Internship\\Project\\blacklist.csv', 'r', encoding='utf-8', newline='')
blacklist = []
data = pd.read_csv('C:\\My Schtuff\\SITE Stuff\\Gurgaon Police Internship\\Project\\history.csv',encoding='utf-8')
columns = ["URL", "Title"]
weird=[]
count = 0

for i in blacklisting:
    blacklist.append(i[:-2])

for i in data["Title"]:
    for b in blacklist:
        if isinstance(i,int)==False and isinstance(i,float)==False and  b in i:
            x=[b]
            data["URL"][count] = clean_url(data["URL"][count])
            for c in columns:
                x.append(data[c][count])
            weird.append(x)
    count+=1

columns.insert(0, "Keywords")
file = open('C:\\My Schtuff\\SITE Stuff\\Gurgaon Police Internship\\Project\\weird.csv', 'w+', encoding='utf-8', newline='')
with file:
    write = csv.writer(file)
    write.writerows([columns])
    write.writerows(weird)

print("Your results are stored in weird.csv")





