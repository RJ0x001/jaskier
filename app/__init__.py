from flask import Flask, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from app import views
