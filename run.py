from doe_sangue.spiders.hemato import HematoSpider
from doe_sangue.spiders.hemope import HemopeSpider
from doe_sangue.spiders.ihebe import IhebeSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

s = get_project_settings()

if __name__ == "__main__":
    process = CrawlerProcess(s)

    process.crawl(HematoSpider)
    process.crawl(HemopeSpider)
    process.crawl(IhebeSpider)
    process.start()
