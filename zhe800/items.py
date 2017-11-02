# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Zhe800Item(scrapy.Item):
    # name = scrapy.Field()
    goodsName = scrapy.Field()
    originPrice = scrapy.Field()
    oldPrice = scrapy.Field()
    goodsPiclLink = scrapy.Field()

    
