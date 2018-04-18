BOT_NAME = 'es_rsguides'

SPIDER_MODULES = ['es_rsguides.spiders']
NEWSPIDER_MODULE = 'es_rsguides.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DEPTH_LIMIT = 100
DOWNLOAD_DELAY = .2

# LOG_LEVEL = 'INFO'
# LOG_FILE = 'cabpapers_dev.log'

COOKIES_ENABLED = False
RETRY_ENABLED = False
REDIRECT_ENABLED = False

ITEM_PIPELINES = {'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 100}

# ITEM_PIPELINES = {'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 100,
#                 'es_rsguides.pipelines.MongoDBPipeline': 200}

"MONGODB PIPELINE SETTINGS"
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = 'webcrawlers'
MONGODB_COLLECTION = 'es_rsguides'
MONGODB_UNIQ_KEY = 'ID'
MONGODB_ITEM_ID_FIELD = '_id'

"ELASTIC PIPELINE SETTINGS"
# ELASTICSEARCH_SERVERS = ['https://search-discoverydev-y6y7pkxqr64q5zmdsvf4ydgoca.eu-west-1.es.amazonaws.com/']
ELASTICSEARCH_SERVERS = ['localhost']
ELASTICSEARCH_INDEX = 'website_dev'
ELASTICSEARCH_TYPE = 'webpage'
ELASTICSEARCH_UNIQ_KEY = 'DOCUMENT_ID'
