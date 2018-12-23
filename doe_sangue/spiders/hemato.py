from doe_sangue.items import HematoItem
import scrapy


class HematoSpider(scrapy.Spider):
    name = 'hemato'
    allowed_domains = ['www.doesanguedoevida.com.br/doar-sangue-recife']
    start_urls = ['http://www.doesanguedoevida.com.br/doar-sangue-recife/']

    def parse(self, response):
        for tipo_sangue in response.xpath(' //div[contains\
         (@class,"item-estoque")]'):

            item = HematoItem()

            item['url'] = response.url

            item['banco'] = "HEMATO"

            item['tipo_sangue'] = tipo_sangue.xpath('.//div[contains\
             (@class, tipo-sangue)][2]/text()').extract_first()

            item['nivel_sangue'] = tipo_sangue.xpath('.//div[contains\
             (@class, "knob")]/@data-val[1]').extract_first()

            yield item
