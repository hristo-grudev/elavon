BOT_NAME = 'elavon'

SPIDER_MODULES = ['elavon.spiders']
NEWSPIDER_MODULE = 'elavon.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'elavon.pipelines.ElavonPipeline': 100,

}