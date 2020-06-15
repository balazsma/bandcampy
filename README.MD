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

To download a single track, pass the -s or --song argument to bandcam.py and a link to a specific track, or an album.
**Note that if you pass an album's url after -s | --song, the showcased song on the page will be downloaded**  
**Example:**
python bandcam.py -s https://example.bandcamp.com/track/example-song

To download an album, pass the -a or --album argument to bandcam.py and a link to an album.

# Legal notice

I'm not very good with legal stuff, and frankly, I don't care enough to look into it. 
If something's wrong from a legal perspective, let me know.
