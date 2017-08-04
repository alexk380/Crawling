# -*- coding: utf-8 -*-
import scrapy


class StartupeopleSpider(scrapy.Spider):
    name = 'startupeople'
    allowed_domains = ['http://nycstartups.net/people']
    start_urls = ['http://http://nycstartups.net/people/']

    def parse(self, response):
        pass
