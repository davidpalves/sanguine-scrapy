import scrapy

from datetime import datetime

from doe_sangue.items import HematoItem
from .constants import (
    XPATH_ITEMS,
    XPATH_TIPO_SANGUE,
    XPATH_NIVEL_SANGUE,
    XPATH_PAGES,
    XPATH_ADDRESS,
    XPATH_CITY,
    XPATH_CITY_WITHOUT_COMPLEMENT,
)


class HematoSpider(scrapy.Spider):
    name = "hemato"
    allowed_domains = ["www.doesanguedoevida.com.br"]
    start_urls = ["https://www.doesanguedoevida.com.br/banco-de-sangue-hemato"]

    def parse(self, response):
        pages = response.xpath(XPATH_PAGES["hemato"])

        for page in pages:
            yield response.follow(page, callback=self.parse_item)

    def parse_item(self, response):
        item = HematoItem()

        item["url"] = response.url

        item["banco"] = "HEMATO"

        item["data_extracao"] = datetime.now()

        item["endereco"] = response.xpath(XPATH_ADDRESS["hemato"]).get()

        cidade = response.xpath(XPATH_CITY["hemato"]).get()

        if len(cidade.strip()) > 0:
            localidade = cidade
        else:
            localidade = response.xpath(
                XPATH_CITY_WITHOUT_COMPLEMENT["hemato"]
            ).get()

        item["_id"] = item["banco"] + "-" + localidade

        localidade = localidade.split(" - ")

        item["cidade"] = localidade[0]

        item["estado"] = localidade[-1]

        if len(localidade) > 2:
            item["unidade"] = localidade[1].strip()

        sangue = {}
        for tipo_sangue in response.xpath(XPATH_ITEMS["hemato"]):
            tipo_sanguineo = tipo_sangue.xpath(
                XPATH_TIPO_SANGUE["hemato"]
            ).get()

            nivel_sangue = tipo_sangue.xpath(
                XPATH_NIVEL_SANGUE["hemato"]
            ).get()

            sangue[tipo_sanguineo] = nivel_sangue

        item["sangue"] = sangue

        yield item
