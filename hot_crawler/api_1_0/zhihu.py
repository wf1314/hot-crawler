import json
import time
from . import api
from flask import jsonify
from hot_crawler.hot_spider import zhihu_hot
from threading import Thread


def cache_zhihu_hot(api):
    """
    缓存知乎热榜信息
    :param api:
    :return:
    """
    try:
        result = zhihu_hot()
        output = {
            'code': 0,
            'msg': '成功',
            'data': result
        }
    except Exception as e:
        api.logger.error(e)
        output = {
            'code': 1111,
            'msg': '获取知乎热榜失败',
            'data': [],
        }
    output = json.dumps(output)
    api.redis_con.set('zhihu', output, ex='600')  # 缓存600s


@api.route('/zhihu')
def zhihu():
    """
    知乎热榜api
    http://127.0.0.1:5000/api/v1_0/zhihu
    :return:
    """
    t1 = Thread(target=cache_zhihu_hot, args=(api, ))
    t1.start()
    # 不等待执行结束即向下执行, 为了加快显示速度先忽略掉内容是否更新
    while True:
        result = api.redis_con.get('zhihu')
        if not result:
            time.sleep(0.1)
            continue
        output = json.loads(result)
        return jsonify(output)
