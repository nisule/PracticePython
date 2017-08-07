import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture?mbid=social_retweet&src=longreads'
r = requests.get(url)
r_html = r.text

#soup = BeautifulSoup(r_html, "html5lib")
soup = BeautifulSoup(r_html, "html5lib")

# turns out this wasn't correct like i thought gg
for part in soup.find_all(class_="content drop-cap"):
    print(part.text + "\n")

'''
for title in soup.find_all(class_='story-heading'):
    if title.a:
        print(title.a.text.replace("\n", " ").strip())
    else:
        print(title.contents[0].strip())
'''