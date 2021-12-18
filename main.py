import os
import asyncio
import requests
import json
from bilibili_api import live, sync
from os import popen



class Asoul(object):
    def __init__(self,roomnum,uid):
        self.roomnum = roomnum
        self.uid = uid


    def get_livestatus(self,uid):
        url = 'https://api.live.bilibili.com/room/v1/Room/get_status_info_by_uids'
        header = {'Content-Type': 'application/json'}
        middle = {'uids': [uid]}
        payload = json.dumps(middle)
        r = requests.post(url, data=payload, headers=header)
        dict = r.json()
        statusvalue = dict["data"][str(uid)]['live_status']
        return statusvalue


    def  get_bullet(self,roomnun):
        room = live.LiveDanmaku(roomnun)

        @room.on('DANMU_MSG')


        async def on_danmaku(event):
            # 收到弹幕
            # process the dic
            key_list = []



            def recursive_get_value(data,KeyToFind):
                for compkey in data.keys():
                    print(key_list)
                    if isinstance(data[compkey],dict):
                        key_list.append(compkey)
                        if data[compkey] == KeyToFind:
                            return data[compkey]
                        else:
                            recursive_get_value(data[compkey], KeyToFind)


            print(recursive_get_value(event,"content"))





            #danmu_pure = event["data"]["info"]#["extra"]["content"]
            #print(type(event))
            #print(type(event))
            #print(event.values())
            #print(danmu_pure)
            #print(danmu_pure)

        sync(room.connect())



Diana = Asoul(22637261,672328094)
Ava   = Asoul(22625025,672346917)
Queen = Asoul(22625027,672342685)
Kira  = Asoul(22632424,672353429)
Carol = Asoul(22634198,351609538)

def main():
    judge = Diana.get_livestatus(672328094)
    if judge == 2:
       print("streaming")
       Diana.get_bullet(Diana.roomnum)


    else:
        print("pass")


if __name__=='__main__':
    main()
