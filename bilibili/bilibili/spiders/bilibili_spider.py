import re
import json

from scrapy import Request
from scrapy.spiders import Spider
from bilibili.items import BilibiliItem


class BilibiliSpider(Spider):
    name = 'bilibili_hot_anime'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://s.search.bilibili.com/cate/search?callback=jQuery17209575859979599228_1519735661575&main_ver=v3&search_type=video&view_type=hot_rank&order=click&copy_right=-1&cate_id=33&page=1&pagesize=20&jsonp=jsonp&time_from=20180201&time_to=20180228&_=1519735662126'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        temp = response.body
        temp = re.search('({.+})', temp).group(1)
        datas = json.loads(temp)['result']
        item = BilibiliItem()
        if datas:
            for data in datas:
                item['title'] = data['title']
                item['author'] = data['author']
                item['play_count'] = data['play']
                item['danmu_count'] = data['video_review']
                item['arcurl'] = data['arcurl']
                yield item
            page_num = re.search(r'page=(\d+)', response.url).group(1)
            page_num = 'page=' + str(int(page_num)+1)
            next_url = re.sub(r'page=\d+', page_num, response.url)
            yield Request(next_url, headers=self.headers)
