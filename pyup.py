import os, socket
from flask import Flask, request, send_from_directory

# Not meant to be long-term persisted
UPLOAD_FOLDER = '/tmp/uploads'
# Hope port is not used
PORT = 8080
# Try to figure out the IP
HOST = [(s.connect(('192.168.0.0', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]

app = Flask(__name__)
# Increase max file upload size just in case
app.config['MAX_CONTENT_LENGTH'] = 1000 * 1024 * 1024 # MB max size

# configure upload folder
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


UPLOAD_FORM = '''
        <h1>Insecure file upload</h1>
        <form method=post enctype=multipart/form-data>
            <input type=file name=file>
            <input type=submit value=Upload>
        </form>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    '''
        Super basic listing of files
    '''
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file present'
        f = request.files['file']
        if f.filename == '':
            return 'No file name'
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
    resp = '<img src="https://api.qrserver.com/v1/create-qr-code/?data=http://' + HOST + ':' + str(PORT) + '&amp;size=100x100" alt="" title="" />'
    resp += UPLOAD_FORM
    resp += '<div><h1>List of files in ' + UPLOAD_FOLDER + '</h1>'
    resp += '<ol>'
    for f in os.listdir(UPLOAD_FOLDER):
        resp += '<li>'
        resp += '<a href="' + os.path.join(UPLOAD_FOLDER, f) + '">' + f + '</a>'
        resp += '</li>'
    resp += '</div>'
    return resp

@app.route(UPLOAD_FOLDER + '/<path:filename>', methods=['GET'])
def serve_files(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# run the app
try:
    app.run(port=PORT, host=HOST, debug=False)
except:
    print("Warning starting on a random port")
    app.run(port=0, host=HOST, debug=False)

