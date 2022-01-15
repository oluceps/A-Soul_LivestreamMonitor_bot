import toml
import pymongo

authinfo = toml.load("./db_auth.toml")["userme"]
db_client = pymongo.MongoClient("mongodb://127.0.0.1:27017/",
                                username=authinfo["username"],
                                password=authinfo["password"],
                                authSource=authinfo["authSource"],
                                authMechanism=authinfo["authMechanism"])


def check_database():
    print(f"Databases: {db_client.list_database_names()}")

    if "liveinfo" in db_client.list_database_names():
        print("Database has exist, check collection: ")
        print(db_client["liveinfo"].list_collection_names())
        if "danmu" in db_client["liveinfo"].list_collection_names():
            print("collection has exist")
            return True
        else:
            pass


def insert(username, content, plague, uid, repeat_count):
    formatodict = {"uid": f"{uid}",
                   "username": f"{username}",
                   "content": f"{content}",
                   "plague": f"{plague}",
                   "repeat_count": f"{repeat_count}"}
    db_client["liveinfo"]["danmu"].insert_one(formatodict)
    print("insert success")



