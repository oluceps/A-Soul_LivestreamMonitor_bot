import toml
import pymongo

authinfo = toml.load("./db_auth.toml")["userme"]
db_client: MongoClient = pymongo.MongoClient("mongodb://127.0.0.1:27017/",
                                             username=authinfo["username"],
                                             password=authinfo["password"],
                                             authSource=authinfo["authSource"],
                                             authMechanism=authinfo["authMechanism"])


class liveinfo_process(object):

    def __init__(self, username, content, plague, uid, repeat_count):
        pass

    #        dbuser = urllib.parse.quote_plus(str(input("username of local db: ")))
    #        dbpasswd = urllib.parse.quote_plus(str(input("password: ")))
    def check_database(self):

        if "liveinfo" in db_client.list_database_names():
            print("Database has exist, check collection: ")
            if "danmuinfo" in db_client.list_collection_names():
                print("collection has exist")

        else:
            temp_danmu_db = db_client["liveinfo"]
            temp_danmu_col = temp_danmu_db["danmuinfo"]

    def insert(self, username, content, plague, uid, repeat_count):
        formatodict = {"uid": f"{uid}",
                       "username": f"{username}",
                       "content": f"{content}",
                       "plague": f"{plague}",
                       "repeat_count": f"{repeat_count}"}
        db_client["liveinfo"]["danmuinfo"].insert_one(formatodict)
