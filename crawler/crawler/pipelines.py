# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from .items import ImagesCrawlerItem
from beauty.models import Image
from .spiders.utils import get_file_size

logger = logging.getLogger(__name__)


class ImagesCrawlerPipeline(object):
    def process_item(self, item, spider):
        # print(item)
        images = item['url']
        for i in images:
            if Image.objects.filter(url=i):
                logger.info('Image existed.')
                pass
            elif i.endswith('.gif'):
                pass
            else:
                j = ImagesCrawlerItem()
                f = get_file_size(i)
                if f != 0:
                    j['source'] = item['source'][0]
                    j['url'] = i
                    j['posted_date'] = item['posted_date'][0]
                    j['file_size'] = f
                    j.save()
                    logger.info('Image added')
                else:
                    logger.info('Image have been deleted.')
                    pass
        return item
