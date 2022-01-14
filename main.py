import asyncio
import requests
import json
from bilibili_api import live, sync
import db_process


class Asoul(object):
    def __init__(self, roomnum, uid):
        self.roomnum = roomnum
        self.uid = uid

    def get_livestatus(self, uid):
        url = 'https://api.live.bilibili.com/room/v1/Room/get_status_info_by_uids'
        header = {'Content-Type': 'application/json'}
        middle = {'uids': [uid]}
        payload = json.dumps(middle)
        r = requests.post(url, data=payload, headers=header)
        dict = r.json()
        statusvalue = dict["data"][str(uid)]['live_status']
        if statusvalue == 2:
            return True

    def get_bullet(self, roomnun):
        room = live.LiveDanmaku(roomnun)

        @room.on('DANMU_MSG')
        async def on_danmaku(event):
            # 收到弹幕
            # process the dic
            def recursive_get_value(data, key_to_find):
                if key_to_find in data:
                    return data[key_to_find]

                for v in data.values():
                    if isinstance(v, dict):
                        return recursive_get_value(v, key_to_find)
                return None

            username = recursive_get_value(event, 'info')[2][1]
            content = json.loads(recursive_get_value(event, 'info')[0][15]['extra'])["content"]
            uid = recursive_get_value(event, 'info')[2][0]
            try:
                plaque = f"{recursive_get_value(event, 'info')[3][1]}" \
                         f"{recursive_get_value(event, 'info')[3][0]}"
            except IndexError:
                plaque = None

            print(f"{uid} {plaque} {username}:  {content}")

        sync(room.connect())


Diana = Asoul(22637261, 672328094)
Ava = Asoul(22625025, 672346917)
Queen = Asoul(22625027, 672342685)
Kira = Asoul(22632424, 672353429)
Carol = Asoul(22634198, 351609538)


def main():
    Members = [Diana, Ava, Queen, Kira, Carol]
    for member in Members:
        judge = member.get_livestatus(member.uid)
        while judge is True:
            print("streaming")
            member.get_bullet(member.roomnum)


if __name__ == '__main__':
    main()
