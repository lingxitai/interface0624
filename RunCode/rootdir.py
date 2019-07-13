
'''
将项目文件夹加到环境变量
'''
import os
import sys
sys.path.insert(0,(os.path.dirname(os.path.split(os.path.abspath(__file__))[0])))
# print(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]))
print(sys.path)
