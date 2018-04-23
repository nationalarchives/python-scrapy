# -*- coding: utf-8 -*-

# Scrapy settings for tna_researchguides_webcrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tna_researchguides_webcrawler'

SPIDER_MODULES = ['tna_researchguides_webcrawler.spiders']
NEWSPIDER_MODULE = 'tna_researchguides_webcrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'tna_researchguides_webcrawler (+http://www.nationalarchives.gov.uk)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DEPTH_LIMIT = 100
DOWNLOAD_DELAY = .2

# LOG_LEVEL = 'INFO'
# LOG_FILE = 'tna_researchsguides_webcrawler.log'

COOKIES_ENABLED = False
RETRY_ENABLED = False
REDIRECT_ENABLED = False

ITEM_PIPELINES = {'tna_researchguides_webcrawler.pipelines.MongoDBPipeline': 100}

# ITEM_PIPELINES = {'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 100,
#                 'tna_researchguides_webcrawler.pipelines.MongoDBPipeline': 200}

"MONGODB PIPELINE SETTINGS"
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = 'tna_webcrawlers'
MONGODB_COLLECTION = 'tna_researchguides'
MONGODB_UNIQ_KEY = 'ID'
MONGODB_ITEM_ID_FIELD = '_id'

"ELASTIC PIPELINE SETTINGS"
# ELASTICSEARCH_SERVERS = ['https://search-discoverydev-y6y7pkxqr64q5zmdsvf4ydgoca.eu-west-1.es.amazonaws.com/']
ELASTICSEARCH_SERVERS = ['localhost']
ELASTICSEARCH_INDEX = 'tna_website_dev'
ELASTICSEARCH_TYPE = 'tna_webpage'
ELASTICSEARCH_UNIQ_KEY = 'ID'
