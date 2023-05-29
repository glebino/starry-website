from flask import (
    render_template,
    Flask,
    request,
    send_from_directory
)

import os

app = Flask(__name__)

@app.route("/")
def index():
    print(request.url)
    return render_template('index.html')

@app.route("/yes-endpoint", methods=['GET'])
def yes():
    return render_template('yes.html')

@app.route("/no-endpoint", methods=['GET'])
def no():
    return render_template('no.html')

@app.route('/favicon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.png', mimetype='image/vnd.microsoft.icon')
