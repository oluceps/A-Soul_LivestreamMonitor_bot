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


def insert(*args):
    formatodict = {"uid": args[3],
                   "username": args[0],
                   "content": args[1],
                   "plague": args[2],
                   "sendtime": args[4],
                   "repeat_count": None}
    db_client["liveinfo"]["danmu"].insert_one(formatodict)
    print("insert success")



