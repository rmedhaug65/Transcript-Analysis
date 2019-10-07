# -*- coding: utf-8 -*-
import scrapy
import requests
import re 
import csv

class QuoteSpider(scrapy.Spider):
	name = 'scrapingalphas'
	#page_number = 1
	start_urls = ['https://seekingalpha.com/earnings/earnings-call-transcripts/15']

	def parse(self, response):
		next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
		if next_page:
			next_page_url = response.urljoin(next_page)
			calls = response.xpath("//h3[@class='list-group-item-heading']/a/@href").extract()
			urls = ['https://seekingalpha.com' + i + '?part=single' for i in calls]
			for url in urls:
				yield scrapy.Request(url, callback=self.parse_company)
			yield scrapy.Request(next_page_url, callback=self.parse)

	def parse_company(self, response):
		website = response.request.url
		time = response.xpath("//p[@class='p p1']/text()")[1].extract()
		name = response.xpath("//p[@class='p p1']/text()")[0].extract()
		symbol = response.xpath("//p[@class='p p1']/a/text()").extract()
		yield{'website':website,
			  'symbol':symbol,
			  'name':name,
			  'time':time}

