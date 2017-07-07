# -*- coding: utf-8 -*-
import scrapy
import json

class DirectorscraperSpider(scrapy.Spider):
    name = 'directorScraper'
    allowed_domains = ['http://www.imdb.com/chart/top']
    start_urls = []


    with open ('C:\Armine\imdb\imdb.json') as f:
    	a=f.read()
    	b=json.loads(a)
    	for i in range(1,11):
    	   	start_urls.append(b[i]['link'])

    def parse(self, response):
        yield{
        "movie": response.css('div.title_wrapper h1::text').extract_first(),
        "director": response.css('div.credit_summary_item span.itemprop::text').extract_first(),
        }   
    
    	
