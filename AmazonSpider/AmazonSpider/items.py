# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags

def remove_quotations(value):
    return value.replace(u"\u201d", '').replace(u"\u201c", '')

def strip_value(value):
    return value.strip()

class AmazonspiderItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    # product_name = scrapy.Field(
    #     input_processor = MapCompose(strip_value),
    #     out
    # )
    product_author = scrapy.Field()
    product_price = scrapy.Field()
    product_imagelink = scrapy.Field()
    
