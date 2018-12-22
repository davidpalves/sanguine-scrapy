import scrapy


class HemopeItem(scrapy.Item):
    url = scrapy.Field()
    tipo_sangue = scrapy.Field()
    nivel_sangue = scrapy.Field()