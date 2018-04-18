from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from es_rsguides.parsers import *


class EsRsguidesCrawl(CrawlSpider):
    handle_httpstatus_list = [301]
    name = 'rsguides'
    allowed_domains = ['www.nationalarchives.gov.uk']
    start_urls = ['http://www.nationalarchives.gov.uk/help-with-your-research/']
    rules = [Rule(LinkExtractor(allow='/help-with-your-research/',
                                deny=['/atoz/', 'testlb', 'webarchive', 'letter=', '/research-guides-keywords/',
                                      '/cabinetpapers/', '/SearchUri/',  'research-category=', 'utm_campaign=']),
                  'parse_item', follow=True)]

    def parse_item(self, response):
        l = ItemLoader(item=EsRsguidesItem(), response=response)

        l.add_value('DOCUMENT_ID', response.url)
        # l.add_xpath('TITLE', '//meta[@property="og:title"]/@content')
        l.add_xpath('TITLE', '//title/text()')
        l.add_value('SOURCE', '1200')
        l.add_xpath('START_DATE', '//meta[@name="DCTERMS.created"]/@content')
        l.add_xpath('END_DATE', '//meta[@name="CDTERMS.modified"]/@content')
        l.add_value('', parse_content(response))
        l.add_value('', parse_subjects(response))

        return l.load_item()
