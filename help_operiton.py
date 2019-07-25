'''
输入模块名称后可以自动的生成说明书，尚未完成。
'''

import os
import operationConfig
method_list=dir(operationConfig.CONFIG)
print(method_list)

with open('method_help.txt','a+') as file:
    file.write('operationConfig  \n' )
    file.write(operationConfig.__doc__)

    for i in method_list:
        #print(i)
        if not i.startswith('_') and not i.endswith('_'):
            #print(i)
            if  hasattr(operationConfig.CONFIG,i):
                cc = getattr(operationConfig.CONFIG,i)
                #print(cc)
                if cc.__doc__ != None:
                    file.write('{0} 说明\n'.format(i))
                    file.write( cc.__doc__)
