import os
import posix
import asyncio
from bilibili_api import live, sync
from os import popen


def room(roomnum):
    return live.LiveDanmaku(roomnum)

class Asoul(object):
    def __init__(self,room,uid):
        self.room = room
class Diana(Asoul):
    self.Diana.room = room(22637261)
    self.Ava.room = room(22625025)
    self.Queen.room = room(22625027)
    self.Kira.room = room(22632424)
    self.Carol.room = room(22634198)


UID = {

       'Diana':672328094,

       'Ava':672346917,

       'Queen':672342685,

       'Kira':672353429,

       'Carol':351609538

}

roomlist = [Asoul.Diana.room,Avaroom,Queenroom,Kiraroom,Carolroom]

def main():
    # detect the liveroom pushstream statues
    for memberuid in UID:

        os.popen('curl -G \'http://api.live.bilibili.com/room/v1/Room/getRoomInfoOld\' \
--data-urlencode \'mid="+ memberuid +""\'')

        print(posix.read())
        # judge the status:
        # json analysis replace by T:
        if True:
            room =

            @room.on('DANMU_MSG')
            async def on_danmaku(event):
                # 收到弹幕
                print(event)

            sync(room.connect())
            # ing


if __name__=='__main__':
    main()
