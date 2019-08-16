import requests


class youdao_fanyi(object):
    def __init__(self, appkey):
        if isinstance(appkey, dict):
            self.version = 1.1  # 版本号
            self.errorCode = None  # 状态码
            self.keyfrom = appkey['keyfrom']
            self.key = appkey['key']
            self.doctype = ['xml', 'json', 'jsonp']  # 返回数据格式
            self.url = 'http://fanyi.youdao.com/openapi.do'  # 接口
            self.type = 'data'
            self.q = ''  # 翻译的文本
        else:
            print ('error')


    def _pargmas_data(self, i=1):
        '''
        :param i: 返回数据格式，默认为json格式
        :return:pargmas 返回构建数据
        '''
        pargmas = {}
        pargmas['version'] = self.version
        pargmas['keyfrom'] = self.keyfrom
        pargmas['key'] = self.key
        pargmas['doctype'] = self.doctype[i]  # 获取什么格式的数据，0：xml，1:json 2:jsonp
        pargmas['type'] = self.type
        return pargmas

    def _get_fanyi_json(self):
        '''
        执行get请求
        :return:
        '''
        dict_data = self._pargmas_data()
        from audio import SpeechRecognition
        path = r'C:\Users\15845\Pictures\intel\output.wav'
        text = SpeechRecognition.fanyi(path)
        dict_data['q'] = text
        result = requests.get(self.url, params=dict_data)
        self.errorCode = result.status_code
        if self.errorCode==200:
            result = result.text
            return result

    def analysis_json(self):
        result_json_data = self._get_fanyi_json ()
        import json
        result = json.loads ( result_json_data )
        status_code = result['errorCode']
        if status_code == 0:
            print ( result['translation'][0] )
            return "翻译结果为：\n" + result['translation'][0] + "\n--------------------------------------------------"
        elif status_code == 20:
            print ( '要翻译的文本过长' )
            return '要翻译的文本过长'
        elif status_code == 30:
            print ( '无法进行有效的翻译' )
            return '无法进行有效的翻译'
        elif status_code == 40:
            print ( '不支持的语言类型' )
            return '不支持的语言类型'
        elif status_code == 50:
            print ( '无效的key' )
            return '无效的key'
        elif status_code == 60:
            print ( '无词典结果，仅在获取词典结果生效' )
            return '无词典结果，仅在获取词典结果生效'




