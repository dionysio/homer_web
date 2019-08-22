import os
from flask import Flask, current_app, send_file

from .api import api_bp

app = Flask(__name__, static_folder='../dist/static')
app.register_blueprint(api_bp)

from .config import Config


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index_client(path=None):
    return send_file(os.path.join(current_app.config['DIST_DIR'], 'index.html'))
