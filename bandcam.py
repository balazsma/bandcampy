import requests, re, time
import os, sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
options = Options()
options.headless = False
<<<<<<< HEAD

=======
driver = webdriver.Firefox(options=options, executable_path="./geckodriver")
>>>>>>> ca1703219b969e7f8e944782c1ce85980d513e11
albumurl = "https://romania.bandcamp.com"
artisturl = re.search('https://[0-1a-zA-Z]*.bandcamp.com', albumurl)
tracks = []
try:
    os.mkdir("./downloads")
except FileExistsError:
    pass
if artisturl:
    print("line 11")
    albumpage = requests.get(albumurl)
    soup = BeautifulSoup(albumpage.content, "html.parser")
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
            "tracknum" : albumdata["trackinfo"][0]["track_num"]
        }
        tracks.append(dict)
        path = "_".join(dict["album"].split()).replace("/", "_")
        print(path)


    driver.close()
    print(album)
    try:
        os.mkdir("./downloads/"+path)
    except FileExistsError:
        pass
    for track in tracks:
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
        audio.save()
# TASKS:
# - parameters
# - single track or album download
# - possibly grabbing all albums of an artist
# - executable