from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
import logging
import pymongo

logger = logging.getLogger()
SETTINGS = get_project_settings()


class NivelSangueHematoPipeline(object):
    def process_item(self, item, spider):
        if item["banco"] in ["HEMATO", "IHEBE"]:
            for tipo_sangue in item["sangue"]:
                if float(item["sangue"][tipo_sangue]) > 0.6:
                    item["sangue"][tipo_sangue] = "estavel"
                elif float(item["sangue"][tipo_sangue]) >= 0.4:
                    item["sangue"][tipo_sangue] = "alerta"
                else:
                    item["sangue"][tipo_sangue] = "critica"
        return item


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            SETTINGS["MONGODB_SERVER"], SETTINGS["MONGODB_PORT"]
        )
        db = connection[SETTINGS["MONGODB_DB"]]
        self.collection = db[SETTINGS["MONGODB_COLLECTION"]]

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data!")
        self.collection.update({"_id": item["_id"]}, dict(item), upsert=True)
        logger.info("Item added to MongoDB database!",)
        return item
