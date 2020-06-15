import requests, re
import os, sys, argparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import bandcampydl

options = Options()
options.headless = True
parser = argparse.ArgumentParser()

parser.add_argument("-a","--album", help="download whole album", action="store_true")

parser.add_argument("url", help="URL to be downloaded")
args = parser.parse_args()
albumurl = args.url
artisturl = re.search('https://[0-1a-zA-Z]*.bandcamp.com', albumurl)
tracks = []
try:
    os.mkdir("./downloads")
except FileExistsError:
    pass

if artisturl:
    try:
        driver = webdriver.Firefox(options=options, executable_path="./geckodriver")
    except WebDriverException:
        sys.exit("A webdriver exception has occurred. Check geckodriver's path.")
    if args.album:
        albumpage = requests.get(albumurl)
        soup = BeautifulSoup(albumpage.content, "html.parser")



        trackelements = soup.find_all("div", {"class" : "title"})

        for title in trackelements:

            link = artisturl.group(0) + str(title.find("a").get("href"))
            path = bandcampydl.append_to_tracks(bandcampydl.get_track_info(link, driver), tracks)

    else:
        path = bandcampydl.append_to_tracks(bandcampydl.get_track_info(albumurl, driver), tracks)


    driver.close()
    try:
        os.mkdir("./downloads/"+path)
    except FileExistsError:
        pass
    except NameError:
        sys.exit("Tracklist is empty. Possibly a single song's URL was passed of album.")
    for track in tracks:
        bandcampydl.download_track(track["title"], track["link"], track["artist"], track["album"], track["tracknum"], track["year"], path)

else:
    print("Invalid bandcamp URL.")
