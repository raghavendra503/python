import requests
from bs4 import BeautifulSoup
import bs4

url = "https://www.wikipedia.org/"

response = requests.get(url)
content = response.text
print(response.status_code)
if response.status_code ==200:
    #print(BeautifulSoup.prettify())
    soup =BeautifulSoup(content,"html.parser")
    for link in soup.find_all('a'):
        print(link.get("href"))
else:
    print("url unaccessible")
