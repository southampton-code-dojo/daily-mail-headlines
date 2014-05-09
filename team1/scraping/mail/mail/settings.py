# Scrapy settings for mail project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mail'

SPIDER_MODULES = ['mail.spiders']
NEWSPIDER_MODULE = 'mail.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mail (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 1,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
    'mail.comm.rotate_useragent.RotateUserAgentMiddleware' :400
}

DOWNLOAD_DELAY = 1

COOKIES_ENABLED = False

JOBDIR="jobs/mail"