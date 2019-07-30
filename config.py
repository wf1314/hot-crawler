"""
以对象形式配置
"""


class Config(object):
    """
    配置基类
    """
    # 配置redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    LOGGER_DIR = '/tmp/hot_crawler/'


class DevelopConfig(Config):
    """开发模式"""
    DEBUG = True
    LOGGER_LEVEL = 'DEBUG'


class OfficialConfig(Config):
    """正式模式"""
    LOGGER_LEVEL = 'INFO'


config_dict = {
    'develop': DevelopConfig,
    'official': OfficialConfig,
}