import json
import requests
from lxml import etree


class HotSpider(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/75.0.3770.142 Safari/537.36',
        }

    def zhihu(self) -> list:
        """
        知乎热榜爬取
        :return:
        """
        url = 'https://www.zhihu.com/billboard'

        r = requests.get(url, headers=self.headers)
        doc = etree.HTML(r.text)
        content = doc.xpath('//*[@id="js-initialData"]/text()')[0]
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

    def v2ex(self) -> list:
        """
        v2ex最热话题爬取
        :return:
        """
        url = 'https://v2ex.com/?tab=hot'
        r = requests.get(url)
        doc = etree.HTML(r.text)
        output = []
        for div in doc.xpath('.//div[@class="cell item"]'):
            title = div.xpath('.//span[@class="item_title"]/a/text()')[0]
            link = div.xpath('.//span[@class="item_title"]/a/@href')[0]
            metrics = div.xpath('.//a[@class="count_livid"]/text()')[0]
            d = {
                'title': title,
                'excerpt': '',
                'metrics': metrics,
                'link': 'https://v2ex.com' + link,
                'image': '',
            }
            output.append(d)
        return output


if __name__ == '__main__':
    # zhihu_hot()
    hot = HotSpider()
    hot.v2ex()
