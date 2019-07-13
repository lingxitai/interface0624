'''
通过baseExcel模块和operationConfig获取excel表案例数据，已字典方式呈现，最终结果为列表
'''
from base.log import Log
from  base.baseExcel import BaseExcel
import operationConfig
import os
class BaseCode():

    def __init__(self):
        GetLog = Log('basecode')
        self.getlog = GetLog.log()
        LOCALCONFIG=operationConfig.CONFIG()
        pro_dir = operationConfig.RROJECT_DIR
        excel_dir = os.path.join(pro_dir, LOCALCONFIG.get_config_value('EXCEL', 'excel_file'))
        self.baseexcel=BaseExcel(excel_dir)
        self.dict_key_value = eval(LOCALCONFIG.get_config_value('EXCEL','excel_case_name'))
        self.getlog.info('案例key值读取成功为：{0}'.format(self.dict_key_value))

    # def __str__(self):
    #     return self.get_rowcase_data.__doc__#用于返回一个对象的描述信息
    def get_rowcase_data(self,sheetname,rowNumber=None):
        '''
        sheetname必填，如果填写错误日志会报错，rowNumber,默认不填时读取全表案例数据，指定某行只会读取某行数据，超出行数会有日志报错
        :param sheetname:
        :param rowNumber:
        :return: 返回字典格式的case_data
        '''
        case_data = []
        try:
            if rowNumber == None:
                rowNumber = self.baseexcel.get_rows(sheetname)
                for i in range(1,rowNumber):
                    caserow_data = self.baseexcel.get_rowvalue(sheetname,i)
                    dict_data = dict(zip(self.dict_key_value,caserow_data))
                    case_data.append(dict_data)
                    self.getlog.info('{0}页全部案例读取成功，为：{1}'.format(sheetname, case_data))
            elif rowNumber != None :
                try:
                    caserow_data = self.baseexcel.get_rowvalue(sheetname, rowNumber)
                    dict_data = dict(zip(self.dict_key_value, caserow_data))
                    case_data.append(dict_data)
                    self.getlog.info('第{0}行案例读取成功，为：{1}'.format(rowNumber, case_data))
                except Exception as e:
                    self.getlog.error('读取数据失败：%s' % e)
        except Exception as e:
            self.getlog.error('读取数据失败：%s' % e)
        return case_data


if __name__ == '__main__':
    basecode = BaseCode()

    print(basecode.get_rowcase_data('TestCase'))
    print(basecode.get_rowcase_data('TestCase',2))






# LOCALCONFIG=operationConfig.CONFIG()
# pro_dir=operationConfig.RROJECT_DIR
# excel_dir=os.path.join(pro_dir,LOCALCONFIG.get_config_value('EXCEL','excel_file'))
#
# baseexcel=BaseExcel(excel_dir)
# getexceldata=baseexcel.get_rowvalue('TestCase_bak',1)
# config = operationConfig.CONFIG()
# # excel_case_name = ['测试编号','测试用例','FrontSQL前置数据命令','请求体','接口路径','请求方法','HttpCode','结果校验']
# excel_case_name = config.get_config_value('EXCEL','excel_case_name')
# print(excel_case_name)
# print(eval(excel_case_name))
# caseindex=eval(excel_case_name)
# dict1 = zip(caseindex,getexceldata)
# print(dict(dict1))
