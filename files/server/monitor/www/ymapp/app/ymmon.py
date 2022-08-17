import os
import time
import datetime
from pathlib import Path
import re
import shutil

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

app.config.update(
    DEBUG = True,
    TESTING = True,
    SECRET_KEY = 'development',
    UPLOAD_FOLDER = './uploads',
    MAX_CONTENT_PATH = 10485760, # 10MB                                                                          
)

@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/webcam1')
def webcam1():
    return render_template(
        'webcam1.html',
    )

