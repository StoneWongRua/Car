import json
import requests
import base64
import urllib.parse
from pprint import pprint
import time
import cv2


def detect(path):
    # 获取token
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    body = {'grant_type': 'client_credentials',
            'client_id': 'xXDugOa8S6GpMHfPK4OrXotZ',
            'client_secret': 'yzZps0FwcYVuigpB6SVz8mI6Q0DwZIhs'
            }

    req = requests.post(url=url, data=body)
    token = json.loads(req.content)['access_token']

    # 获取百度api识别结果
    ocr_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=%s' % token
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    # 读取图片并进行base64加密
    body = base64.b64encode(open(path, 'rb').read())
    # 进行urlencode
    data = urllib.parse.urlencode({'image': body})

    # post请求
    r = requests.post(url=ocr_url, headers=headers, data=data)

    # 输出请求结果
    # print('请求码为: %s' % r.status_code)
    res_words = json.loads(r.content)['words_result']
    result = json.loads(r.content)
    # print('识别结果为: %s' % res_words)
    # pprint(result)
    # pprint(len(result['words_result']))
    return result['words_result']



if __name__ == '__main__':
    path = r"C:\Users\15845\Pictures\Untitled Diagram (1).png"
    detect(path)