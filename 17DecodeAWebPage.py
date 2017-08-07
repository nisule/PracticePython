import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)


for title in soup.find_all(class_='story-heading'):
    if title.a:
        print(title.a.text.replace("\n", " ").strip())
    else:
        print(title.contents[0].strip())