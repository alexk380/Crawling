# -*- coding: utf-8 -*-
import scrapy


class NypeopleSpider(scrapy.Spider):
    name = 'nypeople'
    allowed_domains = ['nycstartups.net', 
                       'startups-list.com', 
                       'startupsla.com',
                       'builtinmtl.com',
                       'startupschicago.net']
    start_urls = ['http://nycstartups.net/people', 
                  'http://atlanta.startups-list.com/people',
                  'http://austin.startups-list.com/people',
                  'http://bangalore.startups-list.com/',
                  'http://berlin.startups-list.com/people',
                  'http://bostonstartups.net/people',
                  'http://boulderstartups.net/people',
                  'http://startupschicago.net/people',
                  'http://hong-kong.startups-list.com/people',
                  'http://houston.startups-list.com/people',
                  'http://london.startups-list.com/people',
                  'http://startupsla.com/people',
                  'http://melbourne.startups-list.com/people',
                  'http://builtinmtl.com/people',
                  'http://moscow.startups-list.com/people',
                  'http://munich.startups-list.com/people',
                  'http://new-delhi.startups-list.com/people',
                  'http://paris.startups-list.com/people',
                  'http://sanfrancisco.startups-list.com/people',
                  'http://santiago.startups-list.com/people',
                  'http://sao-paulo.startups-list.com/people',
                  'http://seattle.startups-list.com/people',
                  'http://singapore.startups-list.com/people',
                  'http://stockholm.startups-list.com/people',
                  'http://sydney.startups-list.com/people',
                  'http://tel-aviv.startups-list.com/people',
                  'http://tokyo.startups-list.com/people',
                  'http://toronto.startups-list.com/people',
                  'http://vancouver.startups-list.com/people',
                  'http://washington.startups-list.com/people',
                  'http://amsterdam.startups-list.com/people',
                  'http://dallas.startups-list.com/people',
                  'http://denver.startups-list.com/people',
                  'http://detroit.startups-list.com/people',
                  'http://dublin.startups-list.com/people',
                  'http://frankfurt.startups-list.com/people',
                  'http://glasgow.startups-list.com/people',
                  'http://hamburg.startups-list.com/people',
                  'http://johannesburg.startups-list.com/people',
                  'http://kuala-lumpur.startups-list.com/people',
                  'http://kiev.startups-list.com/people',
                  'http://las-vegas.startups-list.com/people',
                  'http://leeds.startups-list.com/people'
                  'http://manchester.startups-list.com/people',
                  'http://miami.startups-list.com/people',
                  'http://mumbai.startups-list.com/people',
                  'http://new-orleans.startups-list.com/people',
                  'http://oakland.startups-list.com/people',
                  'http://oklahoma.startups-list.com/people',
                  'http://philadelphia.startups-list.com/people',
                  'http://phoenix.startups-list.com/people',
                  'http://portland.startups-list.com/people',
                  'http://prague.startups-list.com/people',
                  'http://providence.startups-list.com/people',
                  'http://sacramento.startups-list.com/people',
                  'http://salt-lake-city.startups-list.com/people',
                  'http://san-diego.startups-list.com/people',
                  'http://san-jose.startups-list.com/people',
                  'http://waterloo.startups-list.com/people'                    
                  ]

    def parse(self, response):
         for b in response.xpath('//*[@typeof="Person"]'):
            i = {
                'name' : b.xpath('@data-name').extract(),
                'title' : b.xpath('strong[2]/text()').extract(),
                'ref' : b.xpath('@href').extract(),
                'data-src' : b.xpath('img/@data-src').extract(),
                'comment' : b.xpath('comment()').extract_first().strip().replace('\n', '   '),
                'desc' : b.xpath('p/strong/text()').extract_first().strip().replace('\n', '   '),
                'url' : response.url
            }
            yield i