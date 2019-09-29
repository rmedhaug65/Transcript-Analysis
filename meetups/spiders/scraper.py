# -*- coding: utf-8 -*-
import scrapy
import requests
from ..items import QuotetutorialItem
import re 
import csv

class QuoteSpider(scrapy.Spider):
	name = 'scrapingalpha'
	page_number = 12
	#start_urls = ['https://seekingalpha.com/article/4288008-osi-systems-inc-osis-ceo-deepak-chopra-q4-2019-results-earnings-call-transcript']
	start_urls = ['https://seekingalpha.com/earnings/earnings-call-transcripts/1']	#def start_requests(self):

	def parse(self, response):
		calls = response.xpath("//h3[@class='list-group-item-heading']/a/@href").extract()
		urls = ['https://seekingalpha.com' + i + '?part=single' for i in calls]
		for url in urls:
			yield scrapy.Request(url, callback=self.parse_company)
	
		next_page = 'https://seekingalpha.com/earnings/earnings-call-transcripts/' + str(QuoteSpider.page_number) + '/'
		if QuoteSpider.page_number < 20:
			QuoteSpider.page_number+=1
			yield response.follow(next_page, callback=self.parse)

	def parse_company(self, response):
		website = response.request.url
		time = response.xpath("//p[@class='p p1']/text()")[1].extract()
		name = response.xpath("//p[@class='p p1']/text()")[0].extract()
		symbol = response.xpath("//p[@class='p p1']/a/text()").extract()
		yield{'website':website,
			  'symbol':symbol,
			  'name':name,
			  'time':time}


		
