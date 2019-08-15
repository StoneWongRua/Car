# 语音输入法


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
    return result['result'][0] + "\n--------------------------------------------------"

def weather(path):
    result = client.asr ( get_file_content ( path ), 'wav', 16000, {'dev_pid': 1536, } )
    if result['result'][0].find("科技") != -1:
        print("111no")
        return True
    else:
        print("111yes")
        return False


def fanyi(path):
   # 识别本地文件
    result = client.asr(get_file_content(path), 'wav', 16000, {'dev_pid': 1536, })
    return result['result'][0]



if __name__ == '__main__':
    path = r'C:\Users\15845\Pictures\intel\audio\music\sample-files\16k.wav'
    test(path)