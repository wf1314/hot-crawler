import json
import requests
from pyquery import PyQuery as pq


def zhihu_hot() -> list:
    """
    知乎热榜爬取
    :return:
    """
    url = 'https://www.zhihu.com/billboard'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.142 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    doc = pq(r.text)
    content = doc('#js-initialData').text()
    result = json.loads(content)
    raw_output = result['initialState']['topstory']['hotList']
    output = []
    for o in raw_output:
        d = {
            'title': o['target']['titleArea']['text'],
            'excerpt': o['target']['excerptArea']['text'],
            'metrics': o['target']['metricsArea']['text'],
            'link': o['target']['link']['url'],
            'image': o['target']['imageArea']['url'],
        }
        output.append(d)
    return output


if __name__ == '__main__':
    zhihu_hot()
