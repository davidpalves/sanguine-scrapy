import scrapy


class HemopeItem(scrapy.Item):
    url = scrapy.Field()
    banco = scrapy.Field()
    tipo_sangue = scrapy.Field()
    nivel_sangue = scrapy.Field()


class HematoItem(scrapy.Item):
    url = scrapy.Field()
    banco = scrapy.Field()
    tipo_sangue = scrapy.Field()
    nivel_sangue = scrapy.Field()