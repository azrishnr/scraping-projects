# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy.selector import Selector

class YpagesSpider(scrapy.Spider):
    name = 'ypages'
    
    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            treat = require('treat')
            result = {}
            for i=1,3,1
            do
                assert(splash:runjs("document.querySelectorAll('a.next.ajax-page')[0].click()"))
                assert(splash:wait(5))
                    result[i] = splash:html()
            end
            return treat.as_array(result)
        end
    '''
    def start_requests(self):
        url = 'http://www.yellowpages.com'
        yield SplashRequest(url=url, callback=self.parse, endpoint='render.html', args={'wait':0.5})
        yield SplashRequest(url=url, callback=self.parse_other_pages, endpoint='execute', args={'wait':0.5, 'lua_source': self.script}, dont_filter=True)

    def parse(self, response):
        for res in response.xpath("//div[@class='result']"):
            yield {
                'name' : res.xpath("//a[@class='business-name']/span/text()").extract_first(),
                'phone_number' : res.xpath("//div[@class='phones phone primary']/text()").extract_first(),
                'address' : res.xpath("//p[@class='adr']/span[1]/text()").extract_first(),
                'city' : res.xpath("//p[@class='adr']/span[2]/text()").extract_first(),
                'state' : res.xpath("//p[@class='adr']/span[3]/text()").extract_first(),
                'zipcode' : res.xpath("//p[@class='adr']/span[4]/text()").extract_first()
            }
            
    def parse_other_pages(self, response):
        for page in response.data:
            sel = Selector(text=page)
            for res in sel.xpath("//div[@class='result']"):
                yield {
                    'name' : res.xpath("//a[@class='business-name']/span/text()").extract_first(),
                    'phone_number' : res.xpath("//div[@class='phones phone primary']/text()").extract_first(),
                    'address' : res.xpath("//p[@class='adr']/span[1]/text()").extract_first(),
                    'city' : res.xpath("//p[@class='adr']/span[2]/text()").extract_first(),
                    'state' : res.xpath("//p[@class='adr']/span[3]/text()").extract_first(),
                    'zipcode' : res.xpath("//p[@class='adr']/span[4]/text()").extract_first()
                }
