import os
import logging

Obj = lambda: lambda: None

log = Obj()
log.filename = None
log.format = '%(asctime)s %(levelname)s %(name)s:%(filename)s:%(lineno)d: %(message)s'
log.level = logging.INFO

server_config = Obj()
server_config.log = log

server_config.db = Obj()
server_config.db.url = 'sqlite:///data.sqlite?check_same_thread=False'
server_config.db.echo = False
server_config.flask = Obj()
server_config.flask.secret_key = os.urandom(24)
server_config.flask.port = 5000
server_config.flask.debug = True
server_config.flask.static_url_path = '/static'
server_config.flask.static_folder = '../ui'

server_config.url = 'http://127.0.0.1:5000'
