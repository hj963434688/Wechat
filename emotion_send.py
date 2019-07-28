import itchat
import os
from PIL import Image, ImageDraw, ImageFont
import threading
import time
import cv2

emo_path = './img/emo/'
result_path = './img/result/'


class target:
    def __init__(self, name, tag, type):
        self.name = name
        self.tag = tag
        self.type = type


def init():
    chatlist = []
    chatlist.append(target(name='Mirage。', tag='q1', type=1))
    chatlist.append(target(name='哈哈哈', tag='q2', type=2))
    chatlist.append(target(name='张狗狗逝去的青春', tag='q3', type=2))
    chatlist.append(target(name='filehelper', tag='q0', type=1))
    return chatlist


def get_emo():
    files = []
    exts = ['jpg', 'png', 'jpeg', 'JPG']
    for parent, dirnames, filenames in os.walk(emo_path):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    files.append(os.path.join(parent, filename))
                    break
    print('Find {} images'.format(len(files)))

    return files


# def test():
#     chatlist = init()
#     print(chatlist[0].name)

def auto_reply():
    # namelist = ['我是谁']
    namelist = ['唐钰婷', '我是谁']

    @itchat.msg_register(['Text', 'Picture'])
    def text_reply(msg):
        # print(msg['FromUserName'])
        # if msg['FromUserName'] == '我是谁':
        # se('你好鸭', friend)
        # print(friend)
        if not msg['FromUserName'] == myUserName:
            print(msg['User']['RemarkName'])
            name = msg['User']['RemarkName']
            # print(msg['MsgType'])5
            # print(msg['Text'])
            # test()
            if name in namelist:
                friend = itchat.search_friends(name)[0]
                send(msg['Text'], friend)
                return None

    itchat.run()


def manual_send():
    while True:
        print('1111')
        time.sleep(10)



def service():

    # namelist = ['唐钰婷', '我是谁']
    manual_thread = threading.Thread(target=manual_send())
    auto_reply_thread = threading.Thread(target=auto_reply())
    manual_thread.start()
    auto_reply_thread.start()
    # itchat.send('hellow', 'filehelper')



def send(word, friend):
    # print(friend)
    test(word)
    friend.send_image('target.jpg')


def test(word='hello world'):

    im1 = Image.open('cat.jpg')

    font = ImageFont.truetype('msyh.ttf', 30)
    draw = ImageDraw.Draw(im1)
    draw.text((70, 10), word, (40, 40, 40), font=font)
    draw = ImageDraw.Draw(im1)
    im1.show()
    im1.save('target.jpg')
    # friend = itchat.search_friends('我是谁')[0]
    # friend.send_image('hellow')


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    # service()
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    auto_reply()
    # se('ad')
    # test('阿萨德')
    # test()