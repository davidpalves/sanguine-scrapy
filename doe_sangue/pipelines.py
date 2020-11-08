from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
import pymongo


class NivelSangueHematoPipeline(object):
    def process_item(self, item, spider):
        if item["banco"] == "HEMATO":
            for tipo_sangue in item["sangue"]:
                if float(item["sangue"][tipo_sangue]) > 0.6:
                    item["sangue"][tipo_sangue] = "estavel"
                elif float(item["sangue"][tipo_sangue]) >= 0.4:
                    item["sangue"][tipo_sangue] = "alerta"
                else:
                    item["sangue"][tipo_sangue] = "critico"
        return item


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings["MONGODB_SERVER"], settings["MONGODB_PORT"]
        )
        db = connection[settings["MONGODB_DB"]]
        self.collection = db[settings["MONGODB_COLLECTION"]]

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data!")
        self.collection.update({"_id": item["_id"]}, dict(item), upsert=True)
        log.msg("Item added to MongoDB database!", level=log.DEBUG, spider=spider)
        return item
