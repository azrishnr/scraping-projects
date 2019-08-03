#-*- coding: utf-8 -*-
"""
Created on Tues Jul 30 3:31:55 2019
@author: Ahil Srikrishnar
"""

import scrapy
from IMDBSpider.items import MovieItem


class ImdbspiderSpider(scrapy.Spider):
    name = 'imdbspider'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top?ref_=nv_mv_250']

    def parse(self, response):
        links = response.xpath("//td[@class='titleColumn']/a/@href").extract()
        i = 1
        for link in links:
            abs_url = response.urljoin(link)
            rating = response.xpath("//td[@class='ratingColumn imdbRating']/strong/text()[" + str(i) + "]").extract()
            if (i <= len(links)):
                i = i + 1
                yield scrapy.Request(abs_url, callback=self.parse_indetail, meta={'rating' : rating})
    
    def parse_indetail(self, response):
        item = MovieItem()
        item['title'] = response.xpath("//div[@class='title_wrapper']/h1/text()").extract()[0][:-1]
        item['directors'] = response.xpath("//div[@class='credit_summary_item']/a/text()").extract()[0]
        item['writers'] = response.xpath("//div[@class='credit_summary_item'][2]/a/text()").extract()
        item['stars'] = response.xpath("//div[@class='credit_summary_item'][3]/a[position()<=3]/text()").extract()
        item['popularity'] = response.xpath("//span[@class='subText']/text()").extract()[6][21:-8]
        
        return item