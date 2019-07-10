
from base.log import Log
import operationConfig
import requests



class BaseHttp():
    GetLog = Log('basehttp')
    getlog = GetLog.log()
    getconfig = operationConfig.CONFIG()
    scheme = getconfig.get_config_value('HTTP', 'scheme')
    baseurl = getconfig.get_config_value('HTTP', 'baseurl')
    port = getconfig.get_config_value('HTTP', 'port')
    timeout = getconfig.get_config_value('HTTP', 'timeout')
    if port:
        baseurl = scheme + '://' + baseurl + ':' + port
    else:
        baseurl = scheme + '://' + baseurl
    getlog.info('读取url成功：{0}'.format(baseurl))

    def get(self,uri,params):
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        url =self.baseurl + uri
        self.getlog.info('最终拼接地址为：{0}'.format(url))
        try:
            response = requests.get(url,headers=headers,params=params)
            self.getlog.info('get请求成功，内容为：%s' % response.content)
            return response

        except TimeoutError as e:
            self.getlog.error('get请求报错了，报错为：%s' % e)
    def post(self,uri,data):
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        url =self.baseurl + uri
        self.getlog.info('最终拼接地址为：{0}'.format(url))
        try:
            response = requests.post(url,headers=headers,data=data,timeout=int(self.timeout))
            self.getlog.info('post请求成功，内容为：%s' % response.text)
            if response.status_code == 200:
                self.getlog.info('post请求成功')
            else:
                response.status_code is not 200
                self.getlog.info('post请求返回失败')
            return response

        except TimeoutError as e:
            self.getlog.error('post请求报错了，报错为：%s' % e)

    def post_with_json(self,uri,data):
        headers = {'Content-type':'application/json'}
        url =self.baseurl + uri
        try:
            response = requests.post(url,headers=headers,json=data,timeout=int(self.timeout))
            self.getlog.info('post_with_json请求成功，内容为：%s' % response.text)
            return response

        except TimeoutError as e:
            self.getlog.error('post_with_json请求报错了，报错为：%s' % e)
if __name__=='__main__':
    basehttp = BaseHttp()
    data = {'number':'1012002'}
    gett=basehttp.post('/EmailSearch',data)