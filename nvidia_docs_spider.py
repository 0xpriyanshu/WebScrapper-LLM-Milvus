import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging

class NvidiaDocsSpider(CrawlSpider):
    name = 'nvidia_docs'
    allowed_domains = ['docs.nvidia.com']
    start_urls = ['https://docs.nvidia.com/cuda/']

    rules = (
        Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(deny=r'\.(pdf|jpg|png|gif|bmp|svg|zip|exe|dmg|tar\.gz)$'), follow=False),
    )

    custom_settings = {
        'DEPTH_LIMIT': 5,
    }

    def parse_item(self, response):
        self.log(f'Scraping: {response.url}')
        if response.status != 200:
            self.log(f'Failed to scrape {response.url}', level=logging.ERROR)
            return
        page_title = response.css('title::text').get()
        page_content = response.css('body').get()
        yield {
            'url': response.url,
            'title': page_title,
            'content': page_content,
        }

