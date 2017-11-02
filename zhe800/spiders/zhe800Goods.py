# -*- coding: utf-8 -*-
import scrapy
from zhe800.items import Zhe800Item

class Zhe800goodsSpider(scrapy.Spider):
    name = 'zhe800Goods'
    allowed_domains = ['zhe800.com']

    pageNum = 1
    url = "https://www.zhe800.com/ju_tag/taonanzhuang/page/"

    start_urls = [url + str(pageNum)]

    def parse(self, response):
        data = response.xpath('//div[@class="deal"]')
        for each in data:
            item = Zhe800Item()
            try:
                item['goodsName'] = each.xpath('./div/h3/a/text()').extract()[0]
            except IndexError:
                item['goodsName'] = ""


            try:
                item['originPrice'] = each.xpath('./div/h4/em/text()').extract()[0]
            except IndexError:
                item['originPrice'] = ""


            try:
                item['oldPrice'] = each.xpath('./div/h4/del/text()').extract()[0]
            except IndexError:
                item['oldPrice'] = "0"


            try:
                item['goodsPiclLink'] = each.xpath('./div/a[1]/img[1]/@src').extract()[0]
            except IndexError:
                item['goodsPiclLink'] = ""

            yield item

        self.pageNum += 1
        yield scrapy.Request(self.url+str(self.pageNum),callback=self.parse)

