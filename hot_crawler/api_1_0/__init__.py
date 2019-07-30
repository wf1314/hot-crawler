from flask import Blueprint

api = Blueprint('api', __name__)

from . import zhihu


@api.record
def record_params(setup_state):
    # api.config = {}
    app = setup_state.app
    api.logger = app.logger
    # api.config = dict([(key, value) for (key, value) in dict(app.config).items()])


@api.after_request
def after_request(response):
    """设置默认的响应报文格式为application/json"""
    # 如果响应报文response的Content-Type是以text开头，则将其改为默认的json类型
    if response.headers.get("Content-Type").startswith("text"):
        response.headers["Content-Type"] = "application/json"
    return response
