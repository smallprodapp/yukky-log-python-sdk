import requests


class YukkyLog:
    appkey = ''
    appsecret = ''
    debug = False
    @classmethod
    def init(cls, appkey, appsecret, debug=False):
        cls.appkey = appkey
        cls.appsecret = appsecret
        cls.debug = debug

    @classmethod
    def request(cls, data):
        req = {
            'log': data,
            'appkey': cls.appkey,
            'appsecret': cls.appsecret
        }
        return requests.post(url="https://api.yukkyapp.com/log", json=req)

    @classmethod
    def error(cls, data):
        try:
            data['type'] = 'error'
            YukkyLog.request(data)
        except:
            if YukkyLog.debug:
                print("Yukky Log Error")

    @classmethod
    def warning(cls, data):
        try:
            data['type'] = 'warning'
            YukkyLog.request(data)
        except:
            if YukkyLog.debug:
                print("Yukky Log Error")

    @classmethod
    def info(cls, data):
        try:
            data['type'] = 'info'
            YukkyLog.request(data)
        except:
            if YukkyLog.debug:
                print("Yukky Log Error")

    @classmethod
    def custom(cls, data):
        try:
            YukkyLog.request(data)
        except:
            if YukkyLog.debug:
                print("Yukky Log Error")
