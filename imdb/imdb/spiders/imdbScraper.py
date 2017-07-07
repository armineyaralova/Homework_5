# -*- coding: utf-8 -*-
import scrapy


class ImdbscraperSpider(scrapy.Spider):
    name = 'imdbScraper'
    allowed_domains = ['http://www.imdb.com/chart/top']
    start_urls = ['http://www.imdb.com/chart/top/']

    def parse(self, response):
    	imdb=response.css("tr")[1:-2]
    	i=0
    	average=[]
        
        for a in imdb:
            yield {
                'rank': a.css('td.titleColumn::text').re('[0-9]+')[0],
                'title': a.css('td.titleColumn a::text').extract_first(),
                'link': 'http://imdb.com'+str(a.css('td.titleColumn a::attr(href)').extract_first()),
                'year': a.xpath('//td/span/text()').extract()[i],
                'rating': a.css('td strong::text').extract_first(),
                
            }
            i+=1

        for b in imdb:
        	Rating=b.css('td strong::text').extract_first()
        av=float(Rating)
        average.append(av)
        avg=sum(average)/len(average)
    	yield{
    	"Average":avg
    	}
