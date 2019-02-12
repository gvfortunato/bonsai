# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BonsaiItem(scrapy.Item):
	replies = scrapy.Field()
	topic = scrapy.Field()
	text = scrapy.Field()
	poster = scrapy.Field()
	last_replier = scrapy.Field()
	views = scrapy.Field()
	category = scrapy.Field()
