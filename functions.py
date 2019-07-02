from PyLyrics import *
from bs4 import BeautifulSoup


def get_lyrics(user):
    last = requests.get('https://www.last.fm/user/%s' % user)
    soup = BeautifulSoup(last.content, "lxml")
    try:
        chart = soup.find('td', 'chartlist-name').findAll('a')
    except AttributeError:
        pass
    c, content = 0, ''
    for x in chart:
        if c == 1:
            content = x.get('title')
        x.get('title')
        c += 1
    artist, song = content.strip().split('—')
    try:
        lyrics = PyLyrics.getLyrics(artist.strip(), song.strip())
    except ValueError:
        lyrics = None
    return artist, song, lyrics

