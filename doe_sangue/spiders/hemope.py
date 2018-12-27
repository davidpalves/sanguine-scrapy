from doe_sangue.items import HemopeItem
from datetime import datetime
import scrapy
from .constants import (
    XPATH_ITEMS,
    XPATH_TIPO_SANGUE,
    XPATH_NIVEL_SANGUE
)


class HemopeSpider(scrapy.Spider):
    name = 'hemope'
    allowed_domains = ['www.hemope.pe.gov.br']
    start_urls = ['http://www.hemope.pe.gov.br/']

    def parse(self, response):
        for tipo_sangue in response.xpath(XPATH_ITEMS['hemope']):

            item = HemopeItem()

            item['url'] = response.url

            item['banco'] = "HEMOPE"

            item['tipo_sangue'] = tipo_sangue.xpath(
                XPATH_TIPO_SANGUE['hemope']).extract_first()

            item['nivel_sangue'] = tipo_sangue.xpath(
                XPATH_NIVEL_SANGUE['hemope']).re_first(r'sangue\s*(.*)')

            item['data_extracao'] = datetime.now()

            item['_id'] = item['banco'] + "-" + item['tipo_sangue']

            yield item
