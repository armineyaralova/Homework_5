# -*- coding: utf-8 -*-
import scrapy


class QuestionsscraperSpider(scrapy.Spider):
    name = 'QuestionsScraper'
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["https://stackoverflow.com/questions/tagged/python?sort=newest&pageSize=15",
    "https://stackoverflow.com/questions/tagged/python?page=2&sort=newest&pagesize=15",
    "https://stackoverflow.com/questions/tagged/python?page=3&sort=newest&pagesize=15"]

    def parse(self, response):
         for question in response.css("div.summary"):
            yield {
                'question': question.css('h3 a::text').extract_first(),
                'url': question.css('h3 a::attr(href)').extract_first(),
                
            }