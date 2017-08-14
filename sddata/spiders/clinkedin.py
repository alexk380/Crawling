# -*- coding: utf-8 -*-
import scrapy


class ClinkedinSpider(scrapy.Spider):
    name = "clinkedin"
    allowed_domains = ["www.linkedin.com"]
    start_urls = ['http://www.linkedin.com/']

    def parse(self, response):
        pass
