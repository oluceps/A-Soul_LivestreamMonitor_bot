import os
import posix
import asyncio
from bilibili_api import live, sync
from os import popen



class Asoul(object):
    def __init__(self,roomnum,uid):
        self.roomnum
        self.uid
    def  getbullet(roomnun):
        room = live.LiveDanmaku(roomnun)

        @room.on('DANMU_MSG')
        async def on_danmaku(event):
            # 收到弹幕
            print(event)

        sync(room.connect())


class Diana(Asoul):
    Asoul.roomnum = 22637261
    Asoul.uid  = 672328094
class Ava(Asoul):
    Asoul.roomnum = 22625025
    Asoul.uid = 672346917
class Queen(Asoul):
    Asoul.roomnum = 22625027
    Asoul.uid = 672342685

class Kira(Asoul):
    Asoul.roomnum = 22632424
    Asoul.uid = 672353429
class Carol(Asoul):
    Asoul.roomnum = 22634198
    Asoul.uid = 351609538


def main():
    # detect the liveroom pushstream statues
    for memberuid in UID:

        os.popen('curl -G \'http://api.live.bilibili.com/room/v1/Room/getRoomInfoOld\' \
--data-urlencode \'mid="+ memberuid +""\'')

        print(posix.read())
        # judge the status:
        # json analysis replace by T:
        if True:
            Diana.getbullet()


if __name__=='__main__':
    main()
