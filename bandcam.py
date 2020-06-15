import requests, re, time, datetime
import os, sys, argparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
options = Options()
options.headless = True
short_options = "ha:"
long_options = ["help", "album="]

parser = argparse.ArgumentParser()
#parser.add_argument("url", help="the url of the album/song to be downloaded")
parser.add_argument("-a","--album", help="download whole album")
args = parser.parse_args()
albumurl = args.album
artisturl = re.search('https://[0-1a-zA-Z]*.bandcamp.com', albumurl)
tracks = []
try:
    os.mkdir("./downloads")
except FileExistsError:
    pass
print(albumurl)
if artisturl:

    albumpage = requests.get(albumurl)
    soup = BeautifulSoup(albumpage.content, "html.parser")
    # get cover: a.popupImage -> child: img(src)
    album = ""
    trackelements = soup.find_all("div", {"class" : "title"})
    driver = webdriver.Firefox(options=options, executable_path="./geckodriver")
    for title in trackelements:

        driver.get(artisturl.group(0) + str(title.find("a").get("href")))
        albumdata = driver.execute_script('return TralbumData')
        embeddata = driver.execute_script('return EmbedData')
        # stream's link
        dict = {
            "link" : albumdata["trackinfo"][0]["file"]["mp3-128"],
            "title" : albumdata["trackinfo"][0]["title"],
            "artist" : albumdata["artist"],
            "album" : embeddata["album_title"],
            "tracknum" : albumdata["trackinfo"][0]["track_num"],
            "year" : str(datetime.datetime.strptime(albumdata["album_release_date"], '%d %b %Y %S:%M:%H %Z').year), #album_release_date: "04 Mar 2012 00:00:00 GMT",
        }
        tracks.append(dict)
        path = "_".join(dict["album"].split()).replace("/", "_")

    driver.close()

    try:
        os.mkdir("./downloads/"+path)
    except FileExistsError:
        pass
    for track in tracks:
        print("Downloading " + track["title"])
        title = "./downloads/"+path+"/"+track["title"]+".mp3"
        file = open(title, "wb")
        file.write(requests.get(track["link"]).content)
        file.close()
        mp3 = MP3(title)
        if mp3.tags is None:
            mp3.add_tags()
        mp3.save()
        audio = EasyID3(title)
        audio["artist"] = u""+track["artist"]
        audio["title"]=u""+track["title"]
        audio["album"]=u""+track["album"]
        audio["tracknumber"]=u""+str(track["tracknum"])
        audio["date"] = u""+track["year"]
        audio.save()
else:
    print("Invalid bandcamp URL.")
# TASKS:
# - parameters
# - single track or album download
# - possibly grabbing all albums of an artist
# - executable