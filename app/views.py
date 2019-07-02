from flask import render_template, request
from app import app
from functions import get_lyrics


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'RedJin'}
    artist, song, lyrics = get_lyrics(user['nickname'])
    if not lyrics:
        return render_template('error.html', artist=artist, song=song)
    return render_template('index.html',
                           artist=artist,
                           song=song,
                           lyrics=lyrics.split('\n'))


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        username = str(request.form.get('username'))
        artist, song, lyrics, page_check = get_lyrics(username)
        if not lyrics:
            return render_template('error.html', artist=artist, song=song)
        return render_template('index.html',
                               artist=artist,
                               song=song,
                               lyrics=lyrics.split('\n'))
    return render_template('auth.html')
