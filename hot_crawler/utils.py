import redis
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    """
    正则匹配路由
    """
    def __init__(self, url_map, *args):
        super().__init__(url_map)
        self.regex = args[0]


def get_redis(host='localhost', port=6379):
    """
    获取redis操作对象
    :param host:
    :param port:
    :return:
    """
    pool = redis.ConnectionPool(host=host, port=port, decode_responses=True)
    redis_con = redis.Redis(connection_pool=pool)
    return redis_con
