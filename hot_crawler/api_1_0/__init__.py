from flask import Blueprint
from ..utils import get_redis
from hot_crawler.hot_spider import HotSpider

api = Blueprint('api', __name__)

from . import hot


@api.record_once
def record_params(setup_state):
    # api.config = {}
    app = setup_state.app
    api.logger = app.logger
    api.redis_con = get_redis(app.config.get('REDIS_HOST'), app.config.get('REDIS_PORT'))
    api.hot_spider = HotSpider()
    # api.config = dict([(key, value) for (key, value) in dict(app.config).items()])


@api.after_request
def after_request(response):
    """设置默认的响应报文格式为application/json"""
    # 如果响应报文response的Content-Type是以text开头，则将其改为默认的json类型
    if response.headers.get("Content-Type").startswith("text"):
        response.headers["Content-Type"] = "application/json"
    return response

