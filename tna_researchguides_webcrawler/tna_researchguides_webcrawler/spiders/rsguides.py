from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from tna_researchguides_webcrawler.helpers import *


class TnaResearchguidesWebcrawler(CrawlSpider):
    handle_httpstatus_list = [301]
    name = 'rsguides'
    allowed_domains = ['www.nationalarchives.gov.uk']
    start_urls = ['http://www.nationalarchives.gov.uk/help-with-your-research/']
    rules = [Rule(LinkExtractor(allow='/help-with-your-research/',
                                deny=['/atoz/', 'testlb', 'webarchive', 'letter=', '/research-guides-keywords/',
                                      '/cabinetpapers/', '/SearchUri/', 'research-category=', 'utm_campaign=']),
                  'parse_item', follow=True)]

    def parse_item(self, response):
        il = ItemLoader(item=TnaRSGuidesItem(), response=response)
        il.add_value('ID', response.url)
        il.add_xpath('TITLE', '//title/text()')
        il.add_value('SOURCE', '1200')
        il.add_xpath('START_DATE', '//meta[@name="DCTERMS.created"]/@content')
        il.add_xpath('END_DATE', '//meta[@name="CDTERMS.modified"]/@content')
        il.add_value('', parse_content(response))
        il.add_value('', parse_subjects(response))

        return il.load_item()