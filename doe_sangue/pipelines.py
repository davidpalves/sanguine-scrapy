from scrapy.exceptions import DropItem
from scrapy.conf import settings
from datetime import datetime
from scrapy import log
import psycopg2
import pymongo


class NivelSangueHematoPipeline(object):
    def process_item(self, item, spider):
        if item['banco'] == "HEMATO":
            if float(item['nivel_sangue']) > 0.6:
                item['nivel_sangue'] = 'estavel'
            elif float(item['nivel_sangue']) >= 0.4:
                item['nivel_sangue'] = 'alerta'
            else:
                item['nivel_sangue'] = 'critico'

        return item


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data!")
        self.collection.update({'_id': item['_id']}, dict(item), upsert=True)
        log.msg("Item added to MongoDB database!",
                level=log.DEBUG, spider=spider)
        return item


class PostgreSQLPipeline(object):
    def __init__(self):
        self.connection = psycopg2.connect(
            host=settings['POSTGRES_HOST'],
            database=settings['POSTGRES_DB'],
            user=settings['POSTGRES_USER'],
            password=settings['POSTGRES_PASSWORD'])
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.cursor.execute("INSERT INTO nivel_sangue\
         (banco, tipo_sangue, nivel_sangue, url, scrapedAt, cidade) \
         VALUES (%s, %s, %s, %s, %s, %s);", [
                item['banco'],
                item['tipo_sangue'],
                item['nivel_sangue'],
                item['url'],
                datetime.now(),
                item['cidade']
                ])

        self.connection.commit()

        return item

    def close_spider(self, spider):
        self.cursor.execute("DELETE FROM nivel_sangue a\
         USING nivel_sangue b WHERE ((a.banco = b.banco AND\
         a.tipo_sangue = b.tipo_sangue) AND (a.id < b.id));")
        self.connection.commit()
