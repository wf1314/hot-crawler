from . import api
from flask import jsonify
from ..spider.zhihu_spider import zhihu_hot


@api.route('/zhihu')
def zhihu():
    """
    知乎热榜api
    http://127.0.0.1:5000/api/v1_0/zhihu
    :return:
    """
    output = zhihu_hot()
    return jsonify(output)
