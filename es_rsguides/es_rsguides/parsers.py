from es_rsguides.items import EsRsguidesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def parse_content(response):
    l = ItemLoader(item=EsRsguidesItem(), response=response)
    l.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    l.default_output_processor = Join()
    l.add_xpath('CONTENT', '//div[contains(@class, "breather")]/p//text()')
    l.add_xpath('CONTENT', '//div[contains(@class, "breather")]/ul/li//text()')
    l.add_xpath('CONTENT', '//table[contains(@class, "table table-striped")]/tbody/tr/td//text()')
    l.add_xpath('CONTENT', '//div[contains(@class, "accordion-content")]/p//text()')
    l.add_xpath('CONTENT', '//div[contains(@class, "video-box")]/p//text()')
    l.add_xpath('CONTENT', '//div[contains(@class, "entry-content clearfix")]/p//text()')
    return l.load_item()


def parse_subjects(response):
    l = ItemLoader(item=EsRsguidesItem(), response=response)
    l.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    l.default_output_processor = Join()
    l.add_xpath('SUBJECTS', '//meta[@name="keywords"]/@content')
    return l.load_item()
