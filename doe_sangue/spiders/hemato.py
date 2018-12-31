from doe_sangue.items import HematoItem
from datetime import datetime
import scrapy
from .constants import (
    XPATH_ITEMS,
    XPATH_TIPO_SANGUE,
    XPATH_NIVEL_SANGUE
)


class HematoSpider(scrapy.Spider):
    name = 'hemato'
    allowed_domains = ['www.doesanguedoevida.com.br/doar-sangue-recife']
    start_urls = ['http://www.doesanguedoevida.com.br/doar-sangue-recife/']

    def parse(self, response):
        for tipo_sangue in response.xpath(XPATH_ITEMS['hemato']):

            item = HematoItem()

            item['url'] = response.url

            item['banco'] = "HEMATO"

            item['tipo_sangue'] = tipo_sangue.xpath(
                XPATH_TIPO_SANGUE['hemato']).extract_first()

            item['nivel_sangue'] = tipo_sangue.xpath(
                XPATH_NIVEL_SANGUE['hemato']).extract_first()

            item['data_extracao'] = datetime.now()

            item['cidade'] = "Recife"

            item['_id'] = item['banco'] + "-" + item['tipo_sangue']

            yield item
