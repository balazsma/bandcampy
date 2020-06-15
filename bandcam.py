import requests, re, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = False
driver = webdriver.Firefox(options=options, executable_path="./geckodriver")
albumurl = "https://romania.bandcamp.com"
artisturl = re.search('https://[0-1a-zA-Z]*.bandcamp.com', albumurl)
if artisturl:
    print("line 11")
    albumpage = requests.get(albumurl)
    soup = BeautifulSoup(albumpage.content, "html.parser")
    print(soup)
    tracks = soup.find_all("div", {"class" : "title"})

    for i in tracks:
        print("line 16")
        driver.get(artisturl.group(0) + str(i.find("a").get("href")))
        albumdata = driver.execute_script('return TralbumData')
        print(albumdata["album_url"])
driver.close()
