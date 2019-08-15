import os
import requests
import cv2
import base64
import json
from pprint import pprint
import time
class CarRecognizer(object):
    def __init__(self, api_key, secret_key):
        self.access_token = self._get_access_token(api_key=api_key, secret_key=secret_key)
        self.API_URL = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car' + '?access_token=' \
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
        img_str = base64.b64encode(f.read())
        params = {'image': img_str, 'baike_num': 1}
        tic = time.clock()
        rp_json = self.get_result(params)
        toc = time.clock()
        print('=> Cost time: ', toc - tic)
        result = rp_json['result']
        print(result)
        if str(result[0]['name']) == "非车类":
            return "这并不是一台车\n" \
                   + "--------------------------------------------------"
        if str(result[0]['year']) == "无年份信息":
            # return "这是" + str ( result[0]['name'] ) + "吗？" + "听说" + str (
            #             #     result[0]['baike_info']['description'] ) + "\n"\
            return "年份信息：无" + \
                   "\n车型名称：" + str ( result[0]['name'] ) +\
                    "\n百度百科：" + str ( result[0]['baike_info']['description'] ) +\
                    "\n--------------------------------------------------"
        else:
            return"年份信息：" + str(result[0]['year']) +\
                   "\n车型名称：" + str ( result[0]['name'] ) +\
                    "\n百度百科：" + str ( result[0]['baike_info']['description'] ) + \
                    "\n--------------------------------------------------"


if __name__ == '__main__':
    print(CarRecognizer.detect(img_path="car.jpg"))
