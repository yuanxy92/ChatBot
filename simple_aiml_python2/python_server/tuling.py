#coding=utf-8
# -*- coding:utf-8 -*-
 
'''
Created by swh on 2017.09.18
'''
 
import requests
from json import loads

import urllib
import urllib2
import hashlib
import json
import random
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

class Baidu_Translation:
    def __init__(self):
        self._q = ''
        self._from = 'en'
        self._to = 'zh'
        self._appid = 20180710000184567
        self._key = 'sKzirYwRGODFFw0IRyJE'
        self._salt = 0
        self._sign = ''
        self._dst = ''
        self._enable = True
        
    def GetResult(self):
        self._q.encode('utf8')
        m = str(Trans._appid)+Trans._q+str(Trans._salt)+Trans._key
        m_MD5 = hashlib.md5(m)
        Trans._sign = m_MD5.hexdigest()        
        Url_1 = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'

        values = {'q' : self._q,
            'from' : self._from,
            'to' : self._to,
            'appid' : str(Trans._appid),
            'salt': str(Trans._salt),
            'sign' : self._sign}

        Url = Url_1 + urllib.urlencode(values)
        TransResponse = urllib2.urlopen(Url)
        TransResult = TransResponse.read()
        data = json.loads(TransResult)
        if 'error_code' in data:
            print 'Crash'
            print 'error:',data['error_code']
            return data['error_msg']
        else:
            self._dst = data['trans_result'][0]['dst']
            return self._dst
 
    def ShowResult(self,result):
        print result
        
    def tozh(self, text):
        self._q = text
        self._from = 'en'
        self._to = 'zh'
        self._appid = 20180710000184567
        self._key = 'sKzirYwRGODFFw0IRyJE'
        self._salt = random.randint(10001,99999)
        return self.GetResult()

    def toen(self, text):
        self._q = text
        self._from = 'zh'
        self._to = 'en'
        self._appid = 20180710000184567
        self._key = 'sKzirYwRGODFFw0IRyJE'
        self._salt = random.randint(10001,99999)
        return self.GetResult()

class LoginTic(object):
    def __init__(self):
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }
 
        self.key = '96a83ae75630444b990f5cab43370253'
        self.session = requests.session()
 
    def talkWithTuling(self,text):
        url = 'http://www.tuling123.com/openapi/api'
        data = {
            'key':self.key,       
            'info':text,         
            'userid':'test_id' 
        }
        response = requests.post(url=url, headers=self.headers, data=data)
        return response.text
 
 
if __name__ == '__main__':

    Trans = Baidu_Translation()

    ll = LoginTic()
    userName = raw_input('input:')
    userName = userName.decode('gb18030');
    userName = Trans.tozh(userName);

    while userName != 'q':
        print userName
        cont = ll.talkWithTuling(userName)
        dd = loads(cont)
        cont = Trans.toen((dd['text']));  
        print dd['text']
        print cont

        # if dd['code'] == 100000:
        #     print '-'*10
        #     print dd['text']
        # elif dd['code'] == 200000:
        #     print dd['text']
        #     print dd['url']
        # elif dd['code'] == 302000:
        #     print dd['text']
        #     print len(dd['list'])
 
        # elif dd['code'] == 308000:
        #     pass
 
        # elif dd['code'] == 313000:
        #     pass
 
        # elif dd['code'] == 314000:
        #     pass
        userName = raw_input('input:')
        userName = userName.decode('gb18030');
        userName = Trans.tozh(userName);
 
    print 'exit'
