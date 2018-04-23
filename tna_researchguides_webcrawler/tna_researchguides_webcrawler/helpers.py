from tna_researchguides_webcrawler.items import TnaRSGuidesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def parse_content(response):
    il = ItemLoader(item=TnaRSGuidesItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('CONTENT', '//div[contains(@class, "breather")]/p//text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "breather")]/ul/li//text()')
    il.add_xpath('CONTENT', '//table[contains(@class, "table table-striped")]/tbody/tr/td//text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "accordion-content")]/p//text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "video-box")]/p//text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "entry-content clearfix")]/p//text()')
    return il.load_item()


def parse_subjects(response):
    il = ItemLoader(item=TnaRSGuidesItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('SUBJECTS', '//meta[@name="keywords"]/@content')
    return il.load_item()
