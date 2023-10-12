import requests

from .utils.AuthV3Util import addAuthParams

# 您的应用ID
APP_KEY = '****************'
# 您的应用密钥
APP_SECRET = '********************************'

def doCall(url, header, params, method):
    if 'get' == method:
        return requests.get(url, params)
    elif 'post' == method:
        return requests.post(url, params, header)

def createRequest(qs):
    '''
    note: 将下列变量替换为需要请求的参数
    '''
    q = qs
    lang_from = 'auto'
    lang_to = 'auto'
    vocab_id = '您的用户词表ID'

    data = {'q': q, 'from': lang_from, 'to': lang_to, 'vocabId': vocab_id}

    addAuthParams(APP_KEY, APP_SECRET, data)

    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = doCall('https://openapi.youdao.com/api', header, data, 'post')
    return str(res.content, 'utf-8')
