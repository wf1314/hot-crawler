"""
处理静态文件请求
"""
from flask import Blueprint

# 创建蓝图对象
static_request = Blueprint('static_request', __name__, './static')


@static_request.route('/<re(".*"):html>')
def index(html):
    """
    处理静态文件请求
    :param html:
    :return:
    """
    # 如果为空返回首页
    if not html:
        html = 'html/index.html'
    elif html != 'favicon.ico':
        html = 'html/' + html
    response = static_request.send_static_file(html)
    return response
