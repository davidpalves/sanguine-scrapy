import scrapy

from datetime import datetime

from doe_sangue.items import IhebeItem
from .constants import (
    XPATH_ITEMS,
    XPATH_TIPO_SANGUE,
    XPATH_NIVEL_SANGUE,
    XPATH_ADDRESS,
    XPATH_PLACE_NAME,
)


class IhebeSpider(scrapy.Spider):
    name = "ihebe"
    allowed_domains = ["www.ihebe.com.br/"]
    start_urls = ["https://www.ihebe.com.br/"]

    def parse(self, response):
        item = IhebeItem()

        item["url"] = response.url

        item["banco"] = response.xpath(XPATH_PLACE_NAME["ihebe"]).get()

        item["data_extracao"] = datetime.now()

        item["endereco"] = response.xpath(XPATH_ADDRESS["ihebe"])[1].get().strip()

        item["cidade"] = "Belem - PA"

        item["_id"] = item["banco"] + "-" + item["cidade"]

        sangue = {}
        for tipo_sangue in response.xpath(XPATH_ITEMS["ihebe"]):

            tipo_sanguineo = tipo_sangue.xpath(XPATH_TIPO_SANGUE["ihebe"]).get()

            nivel_sangue = tipo_sangue.xpath(XPATH_NIVEL_SANGUE["ihebe"]).get()

            nivel_sangue = int(nivel_sangue) * 0.01

            sangue[tipo_sanguineo] = nivel_sangue

        item["sangue"] = sangue

        yield item
