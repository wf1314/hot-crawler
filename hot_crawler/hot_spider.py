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
        r = requests.get(url, headers=self.headers)
        doc = etree.HTML(r.text)
        output = []
        for div in doc.xpath('//div[@class="cell item"]'):
            title = div.xpath('.//span[@class="item_title"]/a/text()')[0]
            link = div.xpath('.//span[@class="item_title"]/a/@href')[0]
            metrics = div.xpath('.//a[@class="count_livid"]/text()')
            metrics = metrics[0] if metrics else '0'
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
        r = requests.get(url, headers=self.headers)
        doc = etree.HTML(r.text)
        output = []
        for div in doc.xpath('//div[@id="pl_top_realtimehot"]//table/tbody/tr'):
            title = div.xpath('./td[@class="td-02"]/a/text()')[0]
            url = 'https://s.weibo.com' + div.xpath('./td[@class="td-02"]/a/@href')[0]
            metrics = div.xpath('./td[@class="td-02"]/span/text()')
            metrics = metrics[0] if metrics else ''
            d = {
                'title': title,
                'excerpt': "",
                'metrics': metrics,
                'link': url,
                'image': "",
            }
            output.append(d)
        return output

    def tianya(self) -> list:
        """
        天涯论坛
        :return:
        """
        url = 'https://bbs.tianya.cn/m/hotArticle.jsp'
        r = requests.get(url,  headers=self.headers)
        doc = etree.HTML(r.text)
        output = []
        for div in doc.xpath('//div[@class="m-box"]//ul/li'):
            title = div.xpath('./a/p/text()')[0]
            url = 'https://bbs.tianya.cn/m/' + div.xpath('./a/@href')[0]
            metrics = div.xpath('./a/span/text()')
            metrics = metrics[0] if metrics else ''
            d = {
                'title': title,
                'excerpt': "",
                'metrics': metrics,
                'link': url,
                'image': "",
            }
            output.append(d)
        return output

    def baidu(self) -> list:
        """
        百度热搜
        :return:
        """
        url = 'http://top.baidu.com/buzz?b=1&c=513&fr=topcategory_c513'
        r = requests.get(url, headers=self.headers)
        doc = etree.HTML(r.content.decode('gb18030'))
        output = []

        for div in doc.xpath('//table[@class="list-table"]//td[@class="keyword"]'):
            title = div.xpath('./a/text()')[0]
            url = div.xpath('./a/@href')[0]
            metrics = div.xpath('..//td[@class="first"]/span/text()')
            metrics = metrics[0] if metrics else ''
            d = {
                'title': title,
                'excerpt': "",
                'metrics': metrics,
                'link': url,
                'image': "",
            }
            output.append(d)
        return output

    def zhihuribao(self) -> list:
        """
        知乎日报
        :return:
        """
        url = 'http://daily.zhihu.com'
        r = requests.get(url, headers=self.headers)
        doc = etree.HTML(r.text)
        output = []
        for div in doc.xpath('//div[@class="main-content-wrap"]//div[@class="wrap"]//a'):
            title = div.xpath('span/text()')[0]
            url = "https://daily.zhihu.com" + div.xpath('@href')[0]
            image = div.xpath('img/@src')[0]
            d = {
                'title': title,
                'excerpt': "",
                'metrics': '',
                'link': url,
                'image': image,
            }
            output.append(d)
        return output

    def ithome(self) -> list:
        """
        IT之家
        :return:
        """
        url = 'https://www.ithome.com/'
        r = requests.get(url, headers=self.headers)
        doc = etree.HTML(r.content)
        output = []
        for div in doc.xpath('//div[@class="bx"]/ul/li'):
            title = div.xpath('./a/text()')[0]
            url = div.xpath('./a/@href')[0]
            metrics = div.xpath('./span/text()')
            metrics = metrics[0] if metrics else ''
            d = {
                'title': title,
                'excerpt': "",
                'metrics': metrics,
                'link': url,
                'image': '',
            }
            output.append(d)
        return output

    def jiandan(self) -> list:
        """
        煎蛋
        :return:
        """
        url = 'https://jandan.net'
        r = requests.get(url, headers=self.headers)
        # doc = etree.HTML(r.content.decode('gb18030'))
        doc = etree.HTML(r.content)
        output = []
        for div in doc.xpath('//div[@class="post f list-post"]'):
            title = div.xpath('.//div[@class="indexs"]/h2/a/text()')[0]
            url = div.xpath('.//div[@class="indexs"]/h2/a/@href')[0]
            d = {
                'title': title,
                'excerpt': "",
                'metrics': '',
                'link': url,
                'image': '',
            }
            output.append(d)
        return output

    def baidutieba(self) -> list:
        """
        百度贴吧
        :return:
        """
        url = 'https://tieba.baidu.com'
        r = requests.get(url, headers=self.headers)
        doc = etree.HTML(r.text)
        output = []
        for div in doc.xpath('//div[@class="thread-name-wraper"]'):
            title = div.xpath('./a/text()')[0]
            url = 'https://tieba.baidu.com' + div.xpath('./a/@href')[0]
            d = {
                'title': title,
                'excerpt': "",
                'metrics': '',
                'link': url,
                'image': '',
            }
            output.append(d)
        return output

    def heikepai(self) -> list:
        """
        黑客派
        :return:
        """
        url = 'https://hacpai.com/recent/hot'
        r = requests.get(url, headers=self.headers)
        doc = etree.HTML(r.text)
        output = []
        for div in doc.xpath('//h2[@class="article-list__title article-list__title--view fn__flex-1"]'):
            title = div.xpath('./a/text()')[0]
            url = div.xpath('./a/@href')[0]
            d = {
                'title': title,
                'excerpt': "",
                'metrics': '',
                'link': url,
                'image': '',
            }
            output.append(d)
        return output

    def SegmentFault(self) -> list:
        """
        SegmentFault
        :return:
        """
        url = 'https://segmentfault.com/hottest'
        r = requests.get(url, headers=self.headers)
        doc = etree.HTML(r.text)
        output = []
        for div in doc.xpath('//div[@class="news__item-info clearfix"]'):
            title = div.xpath('.//div[@class="mb5 mt5"]/h4/text()')[0]
            url = 'https://segmentfault.com/hottest' + div.xpath('./a/@href')[0]
            d = {
                'title': title,
                'excerpt': "",
                'metrics': '',
                'link': url,
                'image': '',
            }
            output.append(d)
        return output

    def douban(self) -> list:
        """
        豆瓣
        :return:
        """
        url = 'https://www.douban.com/gallery/'
        r = requests.get(url, headers=self.headers)
        doc = etree.HTML(r.text)
        output = []
        for div in doc.xpath('//ul[@class="trend"]/li'):
            title = div.xpath('./a/text()')[0]
            url = div.xpath('./a/@href')[0]
            d = {
                'title': title,
                'excerpt': "",
                'metrics': '',
                'link': url,
                'image': '',
            }
            output.append(d)
        return output

    def wangyinews(self) -> list:
        """
        网易新闻
        :return:
        """
        url = 'http://news.163.com/special/0001386F/rank_whole.html'
        r = requests.get(url, headers=self.headers)
        doc = etree.HTML(r.text)
        output = []
        for div in doc.xpath('//div[@class="tabContents active"]/table//td[@class="cBlue"]'):
            title = div.xpath('../td/a/text()')[0]
            url = div.xpath('../td/a/@href')[0]
            d = {
                'title': title,
                'excerpt': "",
                'metrics': '',
                'link': url,
                'image': '',
            }
            output.append(d)
        return output


if __name__ == '__main__':
    # zhihu_hot()
    hot = HotSpider()
    hot.weibo()
