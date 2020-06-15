from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import datetime, requests


def get_track_info(link, driver):

    driver.get(link)
    albumdata = driver.execute_script('return TralbumData')
    embeddata = driver.execute_script('return EmbedData')
    # stream's link
    dict = {
        "link": albumdata["trackinfo"][0]["file"]["mp3-128"],
        "title": albumdata["trackinfo"][0]["title"],
        "artist": albumdata["artist"],
        "album": embeddata["album_title"],
        "tracknum": albumdata["trackinfo"][0]["track_num"],
        "year": str(datetime.datetime.strptime(albumdata["album_release_date"], '%d %b %Y %S:%M:%H %Z').year),

    }
    return dict
def download_track(title, link, artist, album, tracknum, year, path):
    print("Downloading " + title)
    filename = "./downloads/"+path+"/"+title+".mp3"
    file = open(filename, "wb")
    file.write(requests.get(link).content)
    file.close()
    mp3 = MP3(filename)
    if mp3.tags is None:
        mp3.add_tags()
    mp3.save()
    audio = EasyID3(filename)
    audio["artist"] = u""+artist
    audio["title"]=u""+title
    audio["album"]=u""+album
    audio["tracknumber"]=u""+str(tracknum)
    audio["date"] = u""+year
    audio.save()

def append_to_tracks(dict, tracks):
    path = "_".join(dict["album"].split()).replace("/", "_")
    tracks.append(dict)
    return path