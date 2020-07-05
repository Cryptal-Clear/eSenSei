import requests
from bs4 import BeautifulSoup
import csv

with open('output.txt', 'w') as f:
    f.write("Details of sites visited is as follows: \n")
with open('weird.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        url = row[1]

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        titlesoup = soup.find('title')
        outtext = titlesoup.text

        with open('output.txt', 'a') as outfile:
            outfile.write(outtext)
            outfile.write("\n")

# Final output is written to output.txt
