import scrapy

from datetime import datetime

from doe_sangue.items import HemopeItem
from .constants import (
    XPATH_ITEMS,
    XPATH_TIPO_SANGUE,
    XPATH_NIVEL_SANGUE,
    XPATH_ADDRESS,
    XPATH_PLACE_NAME,
)


class HemopeSpider(scrapy.Spider):
    name = "hemope"
    allowed_domains = ["www.hemope.pe.gov.br"]
    start_urls = ["http://www.hemope.pe.gov.br/"]

    def parse(self, response):
        item = HemopeItem()

        item["url"] = response.url

        item["banco"] = response.xpath(XPATH_PLACE_NAME["hemope"]).extract_first()

        item["data_extracao"] = datetime.now()

        item["endereco"] = response.xpath(XPATH_ADDRESS["hemope"]).extract_first().strip()

        item["cidade"] = "Recife - PE"

        item["_id"] = item["banco"] + "-" + item["cidade"]

        sangue = {}
        for tipo_sangue in response.xpath(XPATH_ITEMS["hemope"]):

            tipo_sanguineo = tipo_sangue.xpath(
                XPATH_TIPO_SANGUE["hemope"]
            ).extract_first()

            nivel_sangue = tipo_sangue.xpath(XPATH_NIVEL_SANGUE["hemope"]).re_first(
                r"sangue\s*(.*)"
            )

            sangue[tipo_sanguineo] = nivel_sangue

        item["sangue"] = sangue

        yield item
