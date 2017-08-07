import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture?mbid=social_retweet&src=longreads'
r = requests.get(url)
r_html = r.text

#soup = BeautifulSoup(r_html, "html5lib")
soup = BeautifulSoup(r_html, "html5lib")

fileName = input("Enter file name: ")
with open(fileName, 'w') as file:
    for part in soup.find_all(class_="content drop-cap"):
        file.write(part.text + "\n")
    file.close()



