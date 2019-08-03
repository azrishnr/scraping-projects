# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from AmazonSpider.items import AmazonspiderItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/books']

    def parse(self, response):
        for book in response.css('s-result-list s-search-results sg-row'):
            loader= ItemLoader(item=AmazonspiderItem(), selector=book, response=response)
            loader.add_css('product_name',".a-color-base.a-text-normal")
            loader.add_css('product_author',"span.a-size-base+ .a-size-base , .a-color-secondary .a-size-base.a-link-normal")
            loader.add_css('product_price',".a-spacing-top-small .a-price:nth-child(1) .a-price-fraction , .a-spacing-top-small .a-price:nth-child(1) .a-price-whole")
            loader.add_css('product_image',"s-image-fixed-height::attr(src)")
            yield loader.load_item()
        
        # /quotes?page=2
        # next_page= response.xpath("//a[@class='next_page']/@href").extract_first()
        next_page = response.css('a-last::attr(href)').extract()

        if next_page is not None:
            next_page_link= response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
