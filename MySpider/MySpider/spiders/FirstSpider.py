import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'

    def __init__(self, category=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://sports.ifeng.com/listpage/31193/1/list.shtml']

    def parse(self, response):
        fw = open('./result.html','w')
        fw.write(response.body)