# -*- coding: utf-8 -*-
import datetime
import socket

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

from game import GameRecord


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['https://live.huanhuba.com/20190903/']
    # start_urls = ('https://live.huanhuba.com/20190903/',
    #               'https://live.huanhuba.com/20190902/',
    #               'https://live.huanhuba.com/20190901/')

    def parse(self, response):
        """
        :param response:
        :return:
         @url https://live.huanhuba.com/20190903/
         @returns items 1
         @scrapes name1 name2 time series
         @scrapes url spider server date
        """
        i=0
        while(1):
            i+=1
            if len(response.xpath('(//*[@class="team-name"])[%d]/text()'%i))<1:
                break
            else:
                print("name: %s"% response.xpath('(//*[@class="team-name"])[%d]/text()'%i).extract())
                # print("web: %s" % response.xpath('//html').extract())
                l = ItemLoader(item=GameRecord(), response=response)
                l.add_xpath('name1', '(//*[@class="team-name"])[%d]/text()'%i)
                l.add_xpath('name2', '(//*[@class="team-name f-toe"])[%d]/text()'%i)
                l.add_xpath('time', '(//*[@class="td time"])[%d]/text()'%i)
                l.add_xpath('series', '(//*[@class="f-toe f-csp"])[%d]/text()'%i)
                l.add_xpath('score1', '(//*[@class="vs-data f-csp"])[%d]/@data-matchhomescore' % i,MapCompose(int))
                # l.add_xpath('score1', '(//*[@class="td vs"])[%d]/a/@data-matchhomescore' % i)
                l.add_xpath('score2', '(//*[@class="vs-data f-csp"])[%d]/@data-matchawayscore' % i,MapCompose(int))

                l.add_value('last_updated', 'today')  # you can also use literal values

                # l.add_value('url', response.url)
                # l.add_value('spider',self.name)
                # l.add_value('server',socket.gethostname())
                # l.add_value('date',datetime.datetime.now())

                yield l.load_item()
        return

