# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, TakeFirst, Join, MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request

from crawler.items import ImagesCrawlerItem
from .utils import convert_datetime


class VozSpider(CrawlSpider):
    name = 'voz'
    allowed_domains = ['vozforums.com']
    start_urls = ['https://vozforums.com/showthread.php?t=2065093&page=1000']

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths='//*[@rel="next"][1]'),
            callback='parse_item',
            follow=True
        ),
    )

    def parse_item(self, response):
        l = ItemLoader(
            item=ImagesCrawlerItem(),
            response=response
        )

        l.add_xpath(
            'url',
            '//img/@src',
            MapCompose(
                lambda x: x if all(
                    [
                        x.startswith('http'),
                        'www.facebook.com' not in x,
                        'scorecardresearch.com' not in x,
                        'vozforums.com' not in x,
                    ]
                ) else ''
            ),
            Compose(lambda l: set([i for i in l if i]))
        )
        l.add_value('source', response.url)
        l.add_xpath(
            'posted_date',
            '//*[@class="thead"]/div[2]/text()',
            MapCompose(str.strip),
            TakeFirst(),
            Compose(convert_datetime)
        )

        return l.load_item()
