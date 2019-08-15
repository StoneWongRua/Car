import urllib, urllib.request

import json
import requests
import base64
import urllib.parse
from pprint import pprint
import time


class IDCardRecognizer(object):
    def __init__(self, api_key, secret_key):
        self.access_token = self._get_access_token(api_key=api_key, secret_key=secret_key)
        self.API_URL = 'https://aip.baidubce.com/rest/2.0/ocr/v1/idcard' + '?access_token=' \
                       + self.access_token
    @staticmethod
    def _get_access_token(api_key, secret_key):
        api = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
              '&client_id={}&client_secret={}'.format(api_key, secret_key)
        rp = requests.post(api)
        if rp.ok:
            rp_json = rp.json()
            print(rp_json['access_token'])
            return rp_json['access_token']
        else:
            print('=> Error in get access token!')
    def get_result(self, params):
        rp = requests.post(self.API_URL, data=params)
        if rp.ok:
            print('=> Success! got result: ')
            rp_json = rp.json()
            pprint(rp_json)
            return rp_json
        else:
            print('=> Error! token invalid or network error!')
            print(rp.content)
            return None


    def detect(self, img_path):
        f = open(img_path, 'rb')
        img_path = base64.b64encode(f.read())
        params = {"image": img_path, "id_card_side": "front"}
        tic = time.clock()
        rp_json = self.get_result(params)
        toc = time.clock()
        print('=> Cost time: ', toc - tic)
        result = rp_json['words_result']
        print(result)
        strover = '识别结果：\n'
        words_result = rp_json['words_result']

        while rp_json['words_result_num'] == 6:
            # 公民身份号码
            Citizenship_number = words_result['公民身份号码']['words']
            strover += '  公民身份号码：{} \n '.format ( Citizenship_number )
            # 民族
            Nation = words_result['民族']['words']
            strover += '  民族：{} \n '.format ( Nation )
            # 姓名
            Full_name = words_result['姓名']['words']
            strover += '  姓名：{} \n '.format ( Full_name )
            # 住址
            address = words_result['住址']['words']
            strover += '  住址：{} '.format ( address )
            strover += '\n---------------------------------------'
            return strover


        # return result

def get_idcard(path):
    # 获取token
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    body = {'grant_type': 'client_credentials',
            'client_id': 'xXDugOa8S6GpMHfPK4OrXotZ',
            'client_secret': 'yzZps0FwcYVuigpB6SVz8mI6Q0DwZIhs'
            }

    req = requests.post(url=url, data=body)
    access_token = json.loads(req.content)['access_token']
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    # 二进制方式打开图片文件
    img = base64.b64encode(open(path, 'rb').read())
    params = {"image": img, "id_card_side": "front"}
    params = urllib.parse.urlencode ( params ).encode ( 'utf-8' )
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request ( url=request_url, data=params )
    request.add_header ( 'Content-Type', 'application/x-www-form-urlencoded' )
    response = urllib.request.urlopen ( request )
    content = response.read ()
    result = json.loads ( content )





if __name__ == '__main__':
    print(get_idcard(r"C:\Users\15845\Pictures\Camera Roll\1.jpg"))



