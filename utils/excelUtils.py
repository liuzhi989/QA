import xlrd,os

class excelUtils(object):

    # 初始化
    def __init__(self,excel_file,excel_sheet):
        # 判断文件
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.excel_sheet = excel_sheet
            self.case_list = list()
        else:
            raise FileNotFoundError('Excel Error：文件不存在！')

    # 读取文件
    def data(self):
        # 打开文件
        workbooks = xlrd.open_workbook(self.excel_file)
        # 打开sheet
        if type(self.excel_sheet) == str:
            self.sheet = workbooks.sheet_by_name(self.excel_sheet)
        elif type(self.excel_sheet) == int:
            self.sheet = workbooks.sheet_by_index(self.excel_sheet)

        # 获取用例头部信息
        title = self.sheet.row_values(0)
        for i in range(1,self.sheet.nrows):
            values = self.sheet.row_values(i)
            self.case_list.append(dict(zip(title,values)))
        return self.case_list

