from scrapy.spiders import Spider
from scrapy import Request
from douban.items import DoubanItem

class DoubanMovieTop250Spider(Spider):
    name = 'douban_movie_top250'
    # start_urls = ['https://movie.douban.com/top250']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        print("Hello World")
        item = DoubanItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            # item['intro'] = movie.xpath(
            #     './/div[@class="bd"]/p[@class="quote"]/span/text()').extract()[0]
            yield item
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()[0]
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url
            yield Request(next_url, headers=self.headers)