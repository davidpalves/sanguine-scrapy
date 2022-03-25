import scrapy

from datetime import datetime

from doe_sangue.items import GenericItem
from .constants import (
    XPATH_ITEMS,
    XPATH_TIPO_SANGUE,
    XPATH_NIVEL_SANGUE,
    XPATH_ADDRESS,
    XPATH_PLACE_NAME,
)


class HemobaSpider(scrapy.Spider):
    name = "hemoba"
    allowed_domains = ["www.hemoba.ba.gov.br"]
    start_urls = ["http://www.hemoba.ba.gov.br/"]

    def parse(self, response):
        item = GenericItem()

        item["url"] = response.url

        item["banco"] = response.xpath(XPATH_PLACE_NAME["hemoba"]).get()

        item["data_extracao"] = datetime.now()

        addresses = response.xpath(XPATH_ADDRESS["hemoba"]).getall()

        item["endereco"] = ', '.join(addresses)

        item["cidade"] = "Salvador"

        item["estado"] = "BA"

        item["_id"] = item["banco"] + "-" + item["cidade"]

        sangue = {}
        for tipo_sangue in response.xpath(XPATH_ITEMS["hemoba"]):

            tipo_sanguineo = tipo_sangue.xpath(XPATH_TIPO_SANGUE["hemoba"]).get()

            nivel_sangue = tipo_sangue.xpath(XPATH_NIVEL_SANGUE["hemoba"]).getall()[-1].strip()

            sangue[tipo_sanguineo] = nivel_sangue

        item["sangue"] = sangue

        yield item
