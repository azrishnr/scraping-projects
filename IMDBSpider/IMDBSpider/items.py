# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # Main Fields
    main_headLine = scrapy.Field()
    headLine = scrapy.Field()

    # Seperate Fields
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    field = scrapy.Field()

class TestItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()

class MovieItem(scrapy.Item):
    title = scrapy.Field()
    directors = scrapy.Field()
    writers = scrapy.Field()
    stars = scrapy.Field()
    popularity = scrapy.Field()