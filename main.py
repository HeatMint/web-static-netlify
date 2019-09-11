from flask import Flask
from flask import send_file
from flask import make_response
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/',endpoint='index')
def index():
    return send_file("static/index.html")


@app.route('/<path:path>',endpoint='stat')
def stat(path):
    print path
    try:
        file = send_file("static/" + path)
    except IOError:
        try:
            file=send_file("static/" + path + ".html")
        except IOError:
            file=send_file("static/404.html")

    response = make_response(file)
    response.headers['X-Frame-Options'] = 'ALLOW-FROM http://gomoku.kcibald.com'
    return response

http_server = WSGIServer(('', 80), app)
http_server.serve_forever()