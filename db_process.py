import pymongo


class liveinfo_db(object):
    def __init__(self,username,content,repeat_count):
        db_client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        temp_danmu_db = db_client["liveinfo"]
        if "liveinfo" in db_client.list_database_names():
            pass
        else:
            pass


