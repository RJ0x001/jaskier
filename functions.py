# from PyLyrics import *
from bs4 import BeautifulSoup
import lyricwikia
import requests


def get_lyrics(user):
    last = requests.get('https://www.last.fm/user/%s' % user)
    soup = BeautifulSoup(last.content, "html.parser")
    d = dict()
    try:
        d['song'] = soup.find('td', 'chartlist-name').findAll('a')[0].get('title')
        d['artist'] = soup.find('td', 'chartlist-artist').findAll('a')[0].get('title')
        d['page'] = 1
    except AttributeError:
        d['page'] = 0
        return d
    try:
        d['lyrics'] = lyricwikia.get_lyrics(d['artist'].strip(), d['song'].strip())
    except Exception as error:
        print(error)
        d['lyrics'] = None
    return d

