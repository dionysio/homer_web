import os
from flask import Flask, current_app, send_file

import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('cmudict')
nltk.download('stopwords')

from .api import api_bp

app = Flask(__name__, static_folder='../dist/static')
app.register_blueprint(api_bp)

from .config import Config


@app.route('/<path:path>')
def index_client(path=None):
    return send_file(os.path.join(current_app.config['DIST_DIR'], 'index.html'))
