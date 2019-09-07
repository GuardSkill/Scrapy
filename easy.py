# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule

from game import GameRecord


class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['web']
    start_urls = ['https://live.huanhuba.com/20190903/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        i = 0
        while (1):
            i += 1
            if len(response.xpath('(//*[@class="team-name"])[%d]/text()' % i)) < 1:
                break
            else:
                print("name: %s" % response.xpath('(//*[@class="team-name"])[%d]/text()' % i).extract())
                # print("web: %s" % response.xpath('//html').extract())
                l = ItemLoader(item=GameRecord(), response=response)
                l.add_xpath('name1', '(//*[@class="team-name"])[%d]/text()' % i)
                l.add_xpath('name2', '(//*[@class="team-name f-toe"])[%d]/text()' % i)
                l.add_xpath('time', '(//*[@class="td time"])[%d]/text()' % i)
                l.add_xpath('series', '(//*[@class="f-toe f-csp"])[%d]/text()' % i)
                l.add_xpath('score1', '(//*[@class="vs-data f-csp"])[%d]/@data-matchhomescore' % i, MapCompose(int))
                # l.add_xpath('score1', '(//*[@class="td vs"])[%d]/a/@data-matchhomescore' % i)
                l.add_xpath('score2', '(//*[@class="vs-data f-csp"])[%d]/@data-matchawayscore' % i, MapCompose(int))

                l.add_value('last_updated', 'today')  # you can also use literal values
                item.append(l.load_item())
                l.add_value('url', response.url)
                l.add_value('spider',self.name)
                l.add_value('server',socket.gethostname())
                l.add_value('date',datetime.datetime.now())
        return item

