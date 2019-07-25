# -*- encoding: utf-8 -*-
import os
import time
import operationConfig
from base.log import Log

config = operationConfig.CONFIG()
report_dir = os.path.join(operationConfig.RROJECT_DIR,'report\{0}'.format(time.strftime('%Y%m%d')))#报告地址report下的当前日期下
set_value = config.set_config_value('REPORT','path','{0}'.format(report_dir) )#将报告地址写入ini文件中，log记录日志的地址也是该目录下
if not os.path.exists(report_dir):
    os.mkdir(report_dir)
GetLog=Log('Run')
getlog = GetLog.log()


result=os.system('pytest RunCode --html={0}/report{1}.html'.format(report_dir,time.strftime('%H%M%S')))


getlog.info('报告执行结果查看执行报告')

