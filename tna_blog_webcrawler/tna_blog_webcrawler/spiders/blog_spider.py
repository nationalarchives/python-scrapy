from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BlogSpider(CrawlSpider):
    name = "blogs"

    allowed_domains = ['blog.nationalarchives.gov.uk']
    start_urls = [
        'http://blog.nationalarchives.gov.uk/blogposts/'
    ]

    rules = [Rule(LinkExtractor(allow='/blog/',
                                deny=['/blog/tag/', '/blog/author/', 'blog/category/']),
                  'parse_item', follow=True)]

    def parse_item(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.txt'

        with open(f'blog_output/{filename}', 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
