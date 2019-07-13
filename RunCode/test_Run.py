'''
通过baseCode获取案例数据，结果为列表，通过baseHttp获取response
将response.content转为字典，读取code与testcase中的HttpCode比较
'''
import pytest
#from . import rootdir
#import operationConfig
from base.baseCode import BaseCode
from base.baseHttp import BaseHttp
from base.log import Log
import json
basecode = BaseCode()
basehttp = BaseHttp()
case_data = basecode.get_rowcase_data('TestCase')#如果读取单行，后加行数
GetLog = Log('test_Run')
getlog = GetLog.log()
# def func(x):
#     return x+1
# def test_func():
#     assert func(4) == 5cd
# @pytest.mark.parametrize('a,b,excepted',[(1,2,3),(2,3,6)])
# def test_1(a,b,excepted):
#     assert a+b == excepted

@pytest.mark.parametrize('case_data',case_data)
def test_allcase(case_data):
    getlog.info('-----------{0}案例执行开始----------------------------'.format(case_data['测试用例']))
    if case_data['请求方法'] == 'post':
        res = basehttp.post(case_data['接口路径'],case_data['请求体'])
        getlog.info('post请求的response和response.content返回码为：{0} \n {1}'.format(res,res.content))
        load_res=json.loads(res.content)#将返回的response.content转为字典
        getlog.info('post请求的返回的response.content转为字典后为：{0} '.format(load_res))
        res_code =load_res['code']#读取字典的code
        getlog.info('post请求的response返回码为：{0}'.format(res_code))
    elif case_data['请求方法'] == 'get':
        res = basehttp.get(case_data['接口路径'], case_data['请求体'])
        getlog.info('get请求的response和response.content返回码为：{0} \n {1}'.format(res,res.content))
        load_res=json.loads(res.content)#将返回的response.content转为字典
        getlog.info('get请求的返回的response.content转为字典后为：{0} '.format(load_res))
        res_code =load_res['code']#读取字典的code
        getlog.info('get请求的response返回码为：{0}'.format(res_code))
    else:
        res = basehttp.post_with_json(case_data['接口路径'], case_data['请求体'])
        getlog.info('post_with_json请求的response和response.content返回码为：{0} \n {1}'.format(res,res.content))
        load_res=json.loads(res.content)#将返回的response.content转为字典
        getlog.info('post_with_json请求的返回的response.content转为字典后为：{0} '.format(load_res))
        res_code =load_res['code']#读取字典的code
        getlog.info('post_with_json请求的response返回码为：{0}'.format(res_code))
    assert res_code == case_data['HttpCode']
    getlog.info('------------------{0}案例执行结束---------------------'.format(case_data['测试用例']))

if __name__=='__main__':
    pytest.main(['test_Run.py'])