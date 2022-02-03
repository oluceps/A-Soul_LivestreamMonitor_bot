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
        midict = r.json()
        statusvalue = midict["data"][str(uid)]['live_status']
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

            feedback_value = recursive_get_value(event, 'info')
            username = feedback_value[2][1]
            content = json.loads(feedback_value[0][15]['extra'])["content"]
            uid = feedback_value[2][0]
            sendtime = feedback_value[0][5]
            try:
                plague = f"{feedback_value[3][1]}" \
                         f"{feedback_value[3][0]}"
            except IndexError:
                plague = None
            val = f"{username},{content},{plague},{uid},{sendtime}"
            print(val)

            #print(event)
            db_process.insert(username,content,plague,uid,sendtime)


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
        if db_process.check_database() is True:
            while judge is True:
                # print("streaming")

                #sync(room.connect())



                print(member.get_bullet(member.roomnum))
                # db_process.insert(member.get_bullet(member.roomnum)())


        else:
            print("error")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("exit.")
