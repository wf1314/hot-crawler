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


    def weibo(self) -> list:
        """
        微博热搜爬取
        :return:
        """
        
        url = 'https://s.weibo.com/top/summary?cate=realtimehot'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/75.0.3770.142 Safari/537.36',
        }
        output = []
        html = etree.HTML(requests.get(url, headers=headers).text)
        affair = html.xpath('//td[@class="td-02"]/a/text()')
        Url = html.xpath('//td[@class="td-02"]/a/@href')

        Url[0] = "https://s.weibo.com" + Url[0]

        view = html.xpath('//td[@class="td-02"]/span/text()')
        d = {
            'title': affair[0],
            'excerpt': "",
            'metrics': "",
            'link': Url[0],
            'image': "",
        }
        output.append(d)
        affair = affair[1:]
        Url = Url[1:]
        for o in range(0, len(affair)):
            Url[o] = "https://s.weibo.com" + Url[o]

            d = {
                'title': affair[o],
                'excerpt': "",
                'metrics': view[o],
                'link': Url[o],
                'image': "",
            }
            output.append(d)
        return output
        # print(output)


if __name__ == '__main__':
    # zhihu_hot()
    hot = HotSpider()
    hot.v2ex()
