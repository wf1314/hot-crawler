import json
import time
from . import api
from flask import jsonify
from threading import Thread


def cache_hot(api, spider_fuc, key):
    """
    缓存热榜信息
    :param api:
    :return:
    """
    try:
        result = spider_fuc()
        output = {
            'code': 0,
            'msg': '成功',
            'data': result
        }
    except Exception as e:
        api.logger.error(e)
        output = {
            'code': 1111,
            'msg': '获取热榜失败',
            'data': [],
        }
    output = json.dumps(output)
    api.redis_con.set(key, output, ex='600')  # 缓存600s


@api.route('/<re(".*"):key>')
def get_hot_lists(key):
    """
    知乎热榜api
    http://127.0.0.1:5000/api/v1_0/zhihu
    :return:
    """
    if not hasattr(api.hot_spider, key):
        return '', 404
    spider_func = getattr(api.hot_spider, key)
    t1 = Thread(target=cache_hot, args=(api, spider_func, key))
    t1.start()
    # 不等待执行结束即向下执行, 为了加快显示速度先忽略掉内容是否更新
    while True:
        result = api.redis_con.get(key)
        if not result:
            time.sleep(0.1)
            continue
        output = json.loads(result)
        return jsonify(output)


