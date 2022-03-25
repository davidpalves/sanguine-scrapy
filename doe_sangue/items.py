import scrapy
from scrapy import Field


class GenericItem(scrapy.Item):
    _id = Field()
    url = Field()
    banco = Field()
    sangue = Field()
    data_extracao = Field()
    endereco = Field()
    cidade = Field()
    estado = Field()


class HematoItem(GenericItem):
    unidade = Field()

