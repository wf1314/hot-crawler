import os
import logging
from flask import Flask
from config import config_dict
from .api_1_0 import api
from .static_html import static_request
from .utils import RegexConverter

from logging.handlers import RotatingFileHandler


def init_log(app):
    """
    初始化日志
    :param app:
    :return:
    """
    config = app.config
    log_dir = config['LOGGER_DIR'] if config.get('LOGGER_DIR') else '/tmp/hot_crawler/'
    log_level = config['LOGGER_LEVEL'] if config.get('LOGGER_LEVEL') else 'INFO'
    app.logger.setLevel(getattr(logging, log_level))
    log_file = os.path.join(log_dir, 'log.log')
    file_log_handler = RotatingFileHandler(log_file, maxBytes=1024*1024*100, backupCount=10)
    formatter = logging.Formatter(
        '[%(levelname)1.1s %(asctime)s.%(msecs)03d %(module)s:%(lineno)d]%(' 'message)s ')
    file_log_handler.setFormatter(formatter)
    app.logger.addHandler(file_log_handler)


def create_app(mode='official'):
    """

    :param mode:
    :return:
    """
    global redis_con
    # 创建app对象
    app = Flask(__name__)
    # 加载配置项
    app.config.from_object(config_dict[mode])
    app.url_map.converters['re'] = RegexConverter
    app.register_blueprint(api, url_prefix='/api/v1_0')
    app.register_blueprint(static_request)
    init_log(app)
    return app

