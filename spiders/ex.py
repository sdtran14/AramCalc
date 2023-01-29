import scrapy


class ExSpider(scrapy.Spider):
    name = 'ex'
    allowed_domains = ['www.metasrc.com']
    start_urls = ['http://www.metasrc.com/']

    def parse(self, response):
        pass
