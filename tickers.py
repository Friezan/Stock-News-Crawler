#-----=====Scraper | Yahoo Based Feed=====-----#
#Version 4.0 | Martin Ortega Jr. | ortegamartin547@gmail.com | 5/1/2017
import scrapy
import collections

from collections import OrderedDict
from scrapy.spiders import XMLFeedSpider
from tickers.items import tickersItem
class Spider(XMLFeedSpider):
    name = "NewsScraper"
    allowed_domains = ["yahoo.com"]
    start_urls = (
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=ABIO,ACFN,AEMD,AEZS,AITB,AJX,AU,AKER',
                  )
    itertag = 'item'
    def parse_node(self, response, node):
        item = collections.OrderedDict()
        item['Title'] = node.xpath(
            'title/text()').extract_first()
        item['PublishDate'] = node.xpath(
            'pubDate/text()').extract_first()
        item['Description'] = node.xpath(
            'description/text()').extract_first()      
        item['Link'] = node.xpath(
            'link/text()').extract_first()
        return item
