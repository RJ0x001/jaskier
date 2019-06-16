import requests

from PyLyrics import *
from bs4 import BeautifulSoup


def get_lyrics(user):
    last = requests.get('https://www.last.fm/user/%s' % user)
    soup = BeautifulSoup(last.content, "html.parser")
    chart = soup.find('td', 'chartlist-name').findAll('a')
    c, content = 0, ''
    for x in chart:
        if c == 1:
            content = x.get('title')
        x.get('title')
        c += 1
    artist, song = content.strip().split('—')
    print(artist.strip(), song.strip())
    try:
        lyrics = PyLyrics.getLyrics(artist.strip(), song.strip())
        return lyrics
    except ValueError as e:
        print(e)
        return 'No lyrics found'


print(get_lyrics('RedJin'))
