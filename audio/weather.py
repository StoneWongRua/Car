# -*- coding:utf-8 -*-
import sys
sys.path.append('..')
import requests
import json
import pprint
from urllib import parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}



from aip import AipSpeech

API_KEY = 'Mlkae0hWQ2QzBHsOWNuQY9yZ'
APP_ID = '17011900'
SECRET_KEY = 'zuykmIs4xwLxLGzXkWbmDOW6IMMaBZsu'


client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()




def test(path):
   # 识别本地文件
    result = client.asr(get_file_content(path), 'wav', 16000, {'dev_pid': 1536, })
    # print(result['result'][0])
    if result['result'][0].find("科技") == -1:
        # print("111no")
        return False
    else:
        # print("111yes")
        return result['result'][0][0:2]

def weather_analyse(location):
    url = 'https://free-api.heweather.com/s6/weather/now?lang=zh&key=34d0643935014b1db954d39c8651a70c' \
          '&location={}'.format(str(location))
    try:
        html = requests.get(url, headers=headers)
    except requests.ConnectionError as e:
        print(e)
    else:
        json_data = json.loads(html.text)
        status = json_data['HeWeather6'][0]['status']
        if status == 'no data for this location':
            print("该城市/地区没有你所请求的数据!")
            return "该城市/地区没有你所请求的数据!"
        elif status == 'permission denied':
            print("没访问权限, 氪金购买服务吧!")
            return "暂时没访问权限"
        elif status == 'ok':
            if location == "auto_ip":
                weather = json_data['HeWeather6'][0]['now']
                return  "天气：" + weather['cond_txt'] + "\n"+\
                        "气温：" + weather['tmp'] + "\n" + \
                        "体感温度：" + weather['fl']+ "\n" + \
                        "风向：" + weather['wind_dir'] + "\n" + \
                        "风速：" + weather['wind_spd']+ "公里/小时\n" + \
                        "相对湿度：" + weather['hum'] + \
                        "\n降水量：" + weather['pcpn'] + \
                        "\n--------------------------------------------------"
            else:
                weather = json_data['HeWeather6'][0]['air_now_city']
                return location + "天气：" + weather['cond_txt'] + "\n"+\
                        "气温：" + weather['tmp'] + "\n" + \
                        "体感温度：" + weather['fl']+ "\n" + \
                        "风向：" + weather['wind_dir'] + "\n" + \
                        "风速：" + weather['wind_spd']+ "公里/小时\n" + \
                        "相对湿度：" + weather['hum'] + \
                        "\n降水量：" + weather['pcpn'] + \
                        "\n--------------------------------------------------"
        else:
            print("出了点问题")
            return "出了点问题"




def lifestyle_analyse(location):
    url = 'https://free-api.heweather.net/s6/weather/lifestyle?lang=en&key=34d0643935014b1db954d39c8651a70c' \
          '&location={}'.format(str(location))
    try:
        html = requests.get(url, headers=headers)
    except requests.RequestException as e:
        print(e)
    else:
        json_data = json.loads(html.text)
        status = json_data['HeWeather6'][0]['status']
        if  status == 'no data for this location':
            print("该城市/地区没有你所请求的数据!")
        elif status == 'permission denied':
            print("没访问权限, 氪金购买服务吧!")
        elif status == 'ok':
            if location == "auto_ip":
                print("您所在地")
                style = []
                for item in json_data['HeWeather6'][0]['lifestyle']:
                    print(item['txt'])
                    style.append(item['txt'])
                    print("testtettkjsabcolsjbdsl" + style)

            else:
                print ( location + "当天的生活建议" )
                for item in json_data['HeWeather6'][0]['lifestyle']:
                    print(item['txt'])

            print("数据更新时间",json_data['HeWeather6'][0]['update']['loc'])
        else:
            print("出了点问题")

        return json_data['HeWeather6'][0]['lifestyle']




if __name__ == '__main__':
    path = r'C:\Users\15845\Pictures\intel\audio\music\sample-files\16k.wav'
    # 3: 获取当地,输入auto_ip
    location = "auto_ip"
    if test(path) != False:
        weather_analyse("auto_ip")
        print('-' * 10)
        lifestyle_analyse("auto_ip")
        print("testtesttest" + lifestyle_analyse(location)[0]['txt'])