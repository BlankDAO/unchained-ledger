import os, json, gzip
from functools import wraps
from io import BytesIO as IO
from datetime import timedelta
from node.config.logging_config import logging
from node.server.database import database as db
from node.config.server_config import server_config as config
from flask import Flask, request, session, redirect, g, after_this_request

app = Flask(__name__)
app.secret_key = config.flask.secret_key


logger = logging.getLogger()
logging.info('******************* APPLICATION RUN *******************')


class ErrorToClient(Exception):
    pass


# compress HTTP content before it's served to client
def gzip_content(response):
    accept_encoding = request.headers.get('Accept-Encoding', '')
    if 'gzip' not in accept_encoding.lower():
        return response
    response.direct_passthrough = False
    if (response.status_code < 200 or
        response.status_code >= 300 or
        'Content-Encoding' in response.headers):
        return response
    gzip_buffer = IO()
    gzip_file = gzip.GzipFile(mode='wb',
                              fileobj=gzip_buffer)
    gzip_file.write(response.data)
    gzip_file.close()
    response.data = gzip_buffer.getvalue()
    response.headers['Content-Encoding'] = 'gzip'
    response.headers['Vary'] = 'Accept-Encoding'
    response.headers['Content-Length'] = len(response.data)
    return response


# pass the rasied error from errorhandler to clinet
@app.errorhandler(ErrorToClient)
def error_to_client(error):
    logger.debug('ErrorToClient: %s', error)
    return json.dumps({'msg': error.args[0], 'args': error.args[1:], 'status': False}), 400


@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=3)
    # g.db_session = db.Session()


@app.after_request
def after_request(response):
    return gzip_content(response)


@app.teardown_request
def teardown_request(exception):
    db_session = getattr(g, 'db_session', None)
    if db_session is not None:
        db_session.close()


@app.route('/')
def index():
    return "redirect('/static/index.html')"


def return_json(f):
    @wraps(f)
    def inner(*a, **k):
        r = f(*a, **k)
        return json.dumps(r)
    return inner


# register blue prints routes
import node.server.api as api
api.register_blueprints(app)
