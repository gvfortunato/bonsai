from scrapy import Spider
from bonsai.items import BonsaiItem
from scrapy import Request
import re

class BonsaiSpider(Spider):
	name = 'bonsai_spider'
	allowed_urls = ['https://www.bonsaiempire.com/']
	start_urls = ['https://www.bonsaiempire.com/forum']
	
	def parse(self, response):
		subforums = response.xpath('.//div[@class="kthead-title kl"]/span/a/@href').extract()
		for subforum in subforums:
			print(subforum)
			url = 'https://www.bonsaiempire.com'+subforum
			yield Request(url=url, meta = {'subforum':subforum}, callback=self.parse_subforum)

	def parse_subforum(self, response):
		pages = response.xpath('.//ul[1][@class="kpagination"]/li/a/text()').extract()
		last_page = pages[-1]
		subforum = response.meta['subforum']
		for i in range(0,int(last_page)*20,20):
			url = 'https://www.bonsaiempire.com'+ subforum + '?start={}'.format(i)
			yield Request(url=url, callback=self.parse_post)

	def parse_post(self, response):
		posts = response.xpath('.//tr[@class="krow2 krow2"]')
		for post in posts:
			replies = post.xpath('.//td[@class="kcol-first kcol-ktopicreplies hidden-phone"]/strong/text()').extract()
			topic = post.xpath('.//td[@class="kcol-mid kcol-ktopictitle"]/div/a[@class="hasTooltip topictitle"]/text()').extract()
			text = post.xpath('.//td[@class="kcol-mid kcol-ktopictitle"]/div/a/@title').extract()
			poster = post.xpath('.//div[@class="hidden-phone"]/span[@class="kwho-user hasTooltip"]/text()').extract()
			last_replier = post.xpath('.//div[@class="visible-phone"]/span[@class="kwho-user hasTooltip"]/text()').extract()
			views = post.xpath('.//span[@class="ktopic-views-number"]/text()').extract()
			category = response.xpath('.//div[@class="kheader"]/h2/span/text()').extract()

			item = BonsaiItem()
			item['replies'] = replies
			item['topic'] = topic
			item['text'] = text
			item['poster'] = poster
			item['last_replier'] = last_replier
			item['views'] = views
			item['category'] = category
			yield item

		posts1 = response.xpath('.//tr[@class="krow1 krow1"]')
		for post in posts1:
			replies = post.xpath('.//td[@class="kcol-first kcol-ktopicreplies hidden-phone"]/strong/text()').extract()
			topic = post.xpath('.//td[@class="kcol-mid kcol-ktopictitle"]/div/a[@class="hasTooltip topictitle"]/text()').extract()
			text = post.xpath('.//td[@class="kcol-mid kcol-ktopictitle"]/div/a/@title').extract()
			poster = post.xpath('.//div[@class="hidden-phone"]/span[@class="kwho-user hasTooltip"]/text()').extract()
			last_replier = post.xpath('.//div[@class="visible-phone"]/span[@class="kwho-user hasTooltip"]/text()').extract()
			views = post.xpath('.//span[@class="ktopic-views-number"]/text()').extract()
			category = response.xpath('.//div[@class="kheader"]/h2/span/text()').extract()

			item = BonsaiItem()
			item['replies'] = replies
			item['topic'] = topic
			item['text'] = text
			item['poster'] = poster
			item['last_replier'] = last_replier
			item['views'] = views
			item['category'] = category
			yield item



