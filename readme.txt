$ scrapy startproject sddata .

$ scrapy genspider -t basic nypeople http://nycstartups.net/people

$ scrapy crawl nypeople

$ scrapy runspider  





 for b in response.xpath('//*[@typeof="Person"]'):
            i = {
                'name' : b.xpath('@data-name').extract(),
                'title' : b.xpath('strong[2]/text()').extract()
            }
            yield i
