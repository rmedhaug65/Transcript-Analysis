import scrapy
import requests

class QuoteSpider(scrapy.Spider):

    name = 'feed_exporter_test'
    # this is equivalent to what you would set in settings.py file
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'test.csv'
    }
    start_urls = ['https://seekingalpha.com/earnings/earnings-call-transcripts/1']

    def parse(self, response):
        
        for i, title in enumerate(titles):
            yield {'index': i, 'title': title}