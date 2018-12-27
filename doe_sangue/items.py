import scrapy
from scrapy import Field


class HemopeItem(scrapy.Item):
    _id = Field()
    url = Field()
    banco = Field()
    tipo_sangue = Field()
    nivel_sangue = Field()
    data_extracao = Field()


class HematoItem(scrapy.Item):
    _id = Field()  # IDs = Banco-TipoSangue
    url = Field()
    banco = Field()
    tipo_sangue = Field()
    nivel_sangue = Field()
    data_extracao = Field()
