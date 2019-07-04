from flask import render_template, request, redirect, url_for
from app import app
from functions import get_lyrics


@app.route('/<username>/')
def lyrics_page(username):
    d = get_lyrics(username)
    if not d['page']:
        return render_template('error.html', error_msg='Username %s does not exist on last.fm' % username)
    if not d['lyrics']:
        return render_template('error.html', error_msg='No lyrics found for %s - %s' % (d['artist'], d['song']))
    return render_template('index.html',
                           artist=d['artist'],
                           song=d['song'],
                           lyrics=d['lyrics'].split('\n'))


@app.route('/', methods=['GET', 'POST'])
@app.route('/start/', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        username = str(request.form.get('username'))
        return redirect(url_for('lyrics_page', username=username))
    return render_template('start.html')
