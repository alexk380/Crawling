# -*- coding: utf-8 -*-
import scrapy


class YclistSpider(scrapy.Spider):
    name = 'yclist'
    allowed_domains = ['yclist.com']
    start_urls = ['http://yclist.com/']

    def parse(self, response):
        i = {}

        for b in response.xpath('//*[@id="companies"]/table/tbody/tr'):
            i = {
                'name' : b.xpath('td[2]/text()').extract_first(),
                'link' : b.xpath('td[3]/a/text()').extract_first(),
                'status' : b.xpath('td[4]/text()').extract_first(),
                'desc' : b.xpath('td[6]/text()').extract_first()
            }

            yield i