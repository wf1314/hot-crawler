from . import api


@api.route('/zhihu')
def zhihu():
    api.logger.debug('hello world')
    return 'hello world'
