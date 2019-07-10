
import xlwt
import xlrd
from xlutils3.copy import copy
from base.log import Log
class BaseExcel():
    def __init__(self,path):
        '''
        找到要打开的excel表格，并打开
        :param path:
        '''
        self.path=path
        GetLog = Log('baseExcel')
        self.getlog = GetLog.log()
        try:
            self.workbook=xlrd.open_workbook(self.path)
            self.getlog.info('打开Excel成功')
        except BaseException as e:
            self.getlog.error('打开Excel报错了： %s' % e)
    def __get_sheet(self,sheetname):
        '''
        要读取内容，需要指定是哪个sheet页，此函数用来指定
        有两种方式可以获得
        1.sheet=self.workbook.sheet_by_index(0)
        2.sheet=self.workbook.sheet_by_name('sheetname')
        此方法采用第二种
        :return:
        '''
        try:
            sheet = self.workbook.sheet_by_name(sheetname)
            self.getlog.info('打开sheet页--{0}成功'.format(sheetname))
        except BaseException as e:
            self.getlog.error('打开sheet报错了： %s' % e)
        return sheet

    def get_sheetnames(self):
        '''
        用来获取excel所有sheet的名称为get_sheet方法使用
        :return:
        '''
        sheetnames=self.workbook.sheet_names()
        self.getlog.info('获取sheetnames--{0}成功'.format(sheetnames))
        return sheetnames

    def get_rows(self,sheetname):
        '''
        用来获取指定sheet页有多少行
        :param sheetname:
        :return:
        '''
        numrows=self.__get_sheet(sheetname).nrows
        self.getlog.info('获取{0}总计{1}行;'.format(sheetname,numrows))
        return numrows
    def get_cols(self,sheetname):
        numcols=self.__get_sheet(sheetname).ncols
        self.getlog.info('获取{0}总计{1}列;'.format(sheetname,numcols))
        return numcols
    def get_single_value(self,sheetname,row,col):
        '''
        获取指定sheet表的某行某列的值
        :param sheetname:
        :param row:
        :param col:
        :return:
        '''
        sheet = self.__get_sheet(sheetname)
        value=sheet.cell_value(row,col)
        self.getlog.info('获取{0}第{1}行{2}列值为{3};'.format(sheetname,row,col,value))
        return value
    def get_rowcolvalue(self,sheetname,row,col1,col2):
        '''
        获取整行第col1列到第col2的值
        :param sheetname:
        :param row:
        :return:
        '''
        sheet = self.__get_sheet(sheetname)
        value=sheet.row_values(row,col1,col2)#默认为从该行的第一列到最后一列的值
        self.getlog.info('获取{0}第{1}行{2}--{3}列的值为{4};'.format(sheetname, row,col1,col2, value))
        return value
    def get_rowvalue(self,sheetname,row):
        '''
        获取整行的值
        :param sheetname:
        :param row:
        :return:
        '''
        sheet = self.__get_sheet(sheetname)
        value=sheet.row_values(row,start_colx=0,end_colx=None)#默认为从该行的第一列到最后一列的值
        value1=[]
        for i in value:
            if type(i) == float:
                value1.append(int(i))
            else:
                value1.append(i)
        self.getlog.info('获取{0}第{1}行值为{2};'.format(sheetname, row, value1))
        return value1
    def get_sheetindex(self,sheetname):
        '''
        通过sheetname获取序列
        :param sheetname:
        :return:
        '''
        sheetnames=self.get_sheetnames()
        for index,value in enumerate(sheetnames):
            if value==sheetname:
                return(index)
    def set_value(self,sheetindex,row,col,value):
        '''
        通过copy修改Excel表某sheet页某行某列值
        :param sheetindex:指定要修改的index
        :param row:指定行
        :param col:列
        :param value:修改为
        :return:
        '''
        try:
            workbook2=copy(self.workbook)
            sheet2=workbook2.get_sheet(sheetindex)
            sheet2.write(row,col,value)
            #self.workbook.release_resources()
            workbook2.save(self.path)#保存为原文件，覆盖掉
            self.getlog.info('修改excel数值成功')
        except BaseException as e:
            self.getlog.error('修改excel数值失败：s%' % e)


if __name__=='__main__':
    excel = BaseExcel('777.xls')
    # print(excel.get_sheetnames())
    # print(excel.get_cols('345_sheetname'))
    # print(excel.get_rows('345_sheetname'))
    # print(excel.get_single_value('345_sheetname',1,1))
    # print(excel.get_rowvalue('345_sheetname', 1))
    # print(excel.get_rowcolvalue('345_sheetname', 1, 1, 2))
    #print(excel.get_sheetindex('123_sheetname'))
    excel.set_value(1,4,5,'dsfs')
    print(BaseExcel.__init__.__doc__)

