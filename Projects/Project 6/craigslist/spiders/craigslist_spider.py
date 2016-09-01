import scrapy
from craigslist.items import CraigslistItem

class CraigslistSpider(scrapy.Spider):
    name = "craigslist"
    allowed_domains = ["craigslist.org"]
    start_urls = [
        "http://dallas.craigslist.org/search/rva",
		"http://houston.craigslist.org/search/rva",
		"http://newyork.craigslist.org/search/rva",
		"http://phoenix.craigslist.org/search/rva",
		"http://losangeles.craigslist.org/search/rva",
		"http://chicago.craigslist.org/search/rva",
		"http://sfbay.craigslist.org/search/rva",
		"http://sandiego.craigslist.org/search/rva",
		"http://philadelphia.craigslist.org/search/rva",
		"http://sanantonio.craigslist.org/search/rva"
    ]

    def parse(self, response):
        for sel in response.xpath("//p[@class='row']"):
            item = CraigslistItem()
            item['url'] = response.url
            item['price'] = sel.xpath('//span[@class="l2"]/span[@class="price"]/text()').extract()[0]
            yield item