from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.exceptions import CloseSpider
from mail.items import MailItem
from scrapy.http import Request


class MailSpider(Spider):
    name = "mail"
    allowed_domains = ["www.dailymail.co.uk", "dailymail.co.uk"]
    start_urls = ["http://www.dailymail.co.uk/news/headlines/index.html?previousday=%d" % d for d in range(3000)] + ["http://www.dailymail.co.uk/tvshowbiz/headlines/index.html?previousday=%d" % d for d in range(3000)]

    def parse(self, response):
        sel = Selector(response)
        headlines = sel.xpath('//ul[@class="link-box linkro-ccox ccox"]//a/text()').extract()

        for headline in headlines:
            item = MailItem()
            item['headline'] = headline
            yield item
