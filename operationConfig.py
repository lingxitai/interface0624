'''
1.本页主要为获得config.ini的值，有sections区分不同的模块,下有items以键值的方式呈现
[ENV]#sections
env_name = kuaidi#items
用configparser.ConfigParser()类方法获得
可以get_config_value获得值和set_config_value修改值
2.定义环境变量地址RROJECT_DIR
'''
import os
from configparser import ConfigParser

# RROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
RROJECT_DIR = os.path.split(os.path.abspath(__file__))[0]
CONFIG_PATH = os.path.join(RROJECT_DIR, 'config', 'config.ini')


# CONFIG_PATH = os.path.abspath('%sconfig\config.ini'% RROJECT_DIR)

class CONFIG():
    configfile = ConfigParser()
    configfile.read(CONFIG_PATH, encoding='utf-8')

    def get_config_value(self, section, option):
        '''
        读取config.ini的值
        :param section:config中的模块名
        :param option:config中的元素键
        :return:
        '''
        value = self.configfile.get(section, option)
        return value

    def set_config_value(self, section, option, value):
        self.configfile.set(section, option, value)
        self.configfile.write(open(CONFIG_PATH, 'r+', encoding='UTF-8'))


if __name__ == '__main__':
    cc = CONFIG()
    print(cc.get_config_value('HTTP', 'scheme'))
    cc.set_config_value('HTTP', 'timeout', '5')
    #os.mkdir('report')
    print(os.path.abspath('%s/report' % os.path.dirname(__file__)))
