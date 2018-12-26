import scrapy
from scrapy import Field


class HemopeItem(scrapy.Item):
    url = Field()
    banco = Field()
    tipo_sangue = Field()
    nivel_sangue = Field()
    data_extracao = Field()


class HematoItem(scrapy.Item):
    url = Field()
    banco = Field()
    tipo_sangue = Field()
    nivel_sangue = Field()
    data_extracao = Field()
