#! Python program that finds and counts how many links and new lines (due to the existence of <a></a>, <br> and <p></p> elements) are in an page's html code.
#! Created by Kostas Simiriotis, January 2019 for the Python test of the 1st semester.


from bs4 import BeautifulSoup
import requests

url = input("Please give url (ex.:http://www.cs.unipi.gr): ")
site = requests.get(url)
html = BeautifulSoup(site.text, 'lxml')

newLines = 0
links = 0

link = html.find_all('a')
links= len(link)

br = html.find_all('br')
par = html.find_all('p')
newLines = len(br) + len(par)

print(f"Yparxoun: {links} syndesmoi kai {newLines} allages grammis.")
