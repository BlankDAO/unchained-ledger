import logging
import logging.handlers
import node.config.server_config as server_config


log = server_config.log
if log.filename is not None:
    log_handler = logging.handlers.WatchedFileHandler(log.filename)
else:
    log_handler = logging.StreamHandler()
log_handler.setFormatter(logging.Formatter(log.format))
root_logger = logging.getLogger()
root_logger.setLevel(log.level)
root_logger.addHandler(log_handler)

logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('werkzeug').setLevel(logging.INFO)
