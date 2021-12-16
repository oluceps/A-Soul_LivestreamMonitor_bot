import os
import posix
import asyncio
from bilibili_api import live, sync
from os import popen



class Asoul(object):
    def __init__(self,roomnum,uid):
        self.roomnum = roomnum
        self.uid = uid
    def  get_bullet(self,roomnun):
        room = live.LiveDanmaku(roomnun)

        @room.on('DANMU_MSG')
        async def on_danmaku(event):
            # 收到弹幕
            print(event)

        sync(room.connect())

Diana = Asoul(22637261,672328094)
Ava   = Asoul(22625025,672346917)
Queen = Asoul(22625027,672342685)
Kira  = Asoul(22632424,672353429)
Carol = Asoul(22634198,351609538)

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
