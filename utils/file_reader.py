import yaml
import configparser
import os
from xlrd import open_workbook


class YamlReader():
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
            self.config = configparser.ConfigParser()
        else:
            raise FileNotFoundError('文件不存在')
        self._data = None

    @property
    def data(self):
        if not self._data:
            with open(self.yamlf,'rb') as f:
                self._data = list(yaml.safe_load_all(f))
            return self._data


class SheetTypeError(Exception):
    pass

class ExcelReader:
    def __init__(self,excel,sheet=0,title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('Excel文件不存在')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()


    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int,str]:
                raise SheetTypeError('Please pass in <type int> or <type str>,not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)  #通过索引顺序获取一个工作表
            else:
                s = workbook.sheet_by_name(self.sheet)  #通过名称获取一个工作表

            if self.title_line:
                title = s.row_values(0)  #获取表中第一行数据，返回的是一个数组
                for col in range(1,s.nrows):  #依次遍历其余行，与行首组成dict，拼到self._data中
                    self._data.append(dict(zip(title,s.row_values(col))))

            else:
                for col in range(0,s.nrows):
                    #遍历所有行，拼到self._data
                    self._data.append(s.row_values(col))

            return self._data

#测试用代码
if __name__ == '__main__':
    e =r'C:\Users\dell\PycharmProjects\Test_framework\data\baidu.xlsx'
    reader = ExcelReader(e,title_line=True)
    print(reader.data)









