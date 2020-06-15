# Introduction

Bandcampy is a script for grabbing albums or individual songs from Bandcamp.

# Requirements

_Python 3_

_mutagen_
pip install mutagen

_requests_
pip install requests

_bs4_
pip install bs4

_selenium_
pip install selenium



# Usage

To download a single track, simply pass the link to a spefic track or album to bandcam.py.
**Note that if you pass an album's url after -s | --song, the showcased song on the page will be downloaded**  
**Example:**
python bandcam.py https://example.bandcamp.com/track/example-song

To download an album, pass the -a or --album argument to bandcam.py and a link to the album.

python bandcam.py https://example.bandcamp.com/album/example-album
# Note

**Certain content on _bandcamp.com_ may be protected by copyright law. I do not take responsibility for the illicit use of this script.**
