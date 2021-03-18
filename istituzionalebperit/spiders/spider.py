import re

import scrapy

from scrapy.loader import ItemLoader

from ..items import IstituzionalebperitItem
from itemloaders.processors import TakeFirst

import requests

base_url = "https://istituzionale.bper.it/media-relations/comunicati-stampa?p_r_p_categoryId=override_{}"

payload = {}
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
  'X-Requested-With': 'XMLHttpRequest',
  'X-PJAX': 'true',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
  'Accept': '*/*',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Accept-Language': 'en-US,en;q=0.9,bg;q=0.8',
}


class IstituzionalebperitSpider(scrapy.Spider):
	name = 'istituzionalebperit'
	start_urls = [base_url.format('1063089080')]
	url = base_url.format('1063089080')

	def parse(self, response):
		data = requests.request("GET", self.url, headers=headers, data=payload)
		raw_data = scrapy.Selector(text=data.text)
		years = raw_data.xpath('//div[@class="horizontal-link-menu year-container"]/a/@href').getall()

		years_links = []
		for year in years:
			year = re.findall(r'\d+', year)[0]
			self.url = base_url.format(year)
			years_links.append(self.url)
		yield from response.follow_all(years_links, self.parse_year)

	def parse_year(self, response):
		data = requests.request("GET", response.url, headers=headers, data=payload)
		raw_data = scrapy.Selector(text=data.text)
		post_links = raw_data.xpath('//a[h2]/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = raw_data.xpath('//a[@class="page"]/@href').getall()
		yield from response.follow_all(next_page, self.parse_year)


	def parse_post(self, response):
		title = response.xpath('//div[@class="title"]/h1/text()').get()
		description = response.xpath('//div[@class="press-text"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//span[@class="date"]/text()').get()

		item = ItemLoader(item=IstituzionalebperitItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
