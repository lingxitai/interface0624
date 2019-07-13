import logging
import operationConfig
import os

# Log = logging.getLogger('dd')
# Log.setLevel(logging.DEBUG)
#
# filelog = logging.FileHandler('aa.log')
# screenlog=logging.StreamHandler()
#
# style = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
#
# filelog.setFormatter(style)
# screenlog.setFormatter(style)
#
# Log.addHandler(filelog)
# Log.addHandler(screenlog)
#
# Log.error('dsdsfd')
# Log.info('23456')
Config = operationConfig.CONFIG()#获得定义好的get_config_value方法
class Log():
    def __init__(self,servername='root'):
        self.servername=servername

        self.log1 = logging.getLogger(self.servername)
        self.log1.setLevel(logging.DEBUG)
        logaddress = os.path.join(Config.get_config_value('REPORT', 'path'), 'system.log')
        '''
        读取config.ini中的report-path，通过Run.py文件写入path，每天更新一个路径
        '''
        filelog = logging.FileHandler(logaddress)
        screenlog = logging.StreamHandler()

        style = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

        filelog.setFormatter(style)
        screenlog.setFormatter(style)

        self.log1.addHandler(filelog)
        self.log1.addHandler(screenlog)
    def log(self):
        return self.log1#引用类变量也需要self

if __name__ == '__main__':
    getlog = Log()
    getllog = getlog.log()
    getllog.error('3234')
    getllog.info('hjhj')
