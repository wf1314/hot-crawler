from . import api


@api.route('/v2ex')
def v2ex():
    api.logger.debug('hello world')
    return 'hello world'
