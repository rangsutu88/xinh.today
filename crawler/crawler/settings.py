# -*- coding: utf-8 -*-

# Scrapy settings for crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import sys
import os

import django

# Django settings
sys.path.append('')  # Path to Django project
os.environ['DJANGO_SETTINGS_MODULE'] = 'vngirl.settings'

django.setup()

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

ITEM_PIPELINES = {'crawler.pipelines.ImagesCrawlerPipeline': 900, }

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"

ROBOTSTXT_OBEY = True

#  Enable and configure the AutoThrottle extension (disabled by default)
#  See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
#  The initial download delay
AUTOTHROTTLE_START_DELAY = 2
#  The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 30
#  The average number of requests Scrapy should be sending in parallel to
#  each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#  Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

LOG_LEVEL = 'INFO'
