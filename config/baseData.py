import os
from utils.yamlUtils import yamlUtils
from utils.excelUtils import excelUtils
from common.caseMethod import caseMethod

class baseData(object):

    # 初始化，定义文件路径
    def __init__(self):
        self.config_path = os.path.dirname(__file__)
        self.project_path = os.path.dirname(self.config_path)
        self.data_path = self.project_path + os.sep + 'data'
        self.logs_path = self.project_path + os.sep + 'logs'
        self.report_path = self.project_path + os.sep + 'report'
        self.mysql_path = self.config_path + os.sep + 'mysql.yml'
        self.base_path = self.config_path + os.sep + 'testBase.yml'
        self.excel_path = self.data_path + os.sep + 'testData.xlsx'

        self.base = yamlUtils(self.base_path).data()
        self.mysql = yamlUtils(self.mysql_path).data()

    # 获取log级别
    def get_log_level(self):
        log_level = self.base['Base']['log_level']
        return log_level

    # 获取sheet信息
    def get_excel_sheet(self):
        excel_sheet = self.base['Base']['excel_sheet']
        return excel_sheet

    # 获取数据库连接信息
    def get_mysql_info(self,mysql_name):
        mysql_info = self.mysql[mysql_name]
        return mysql_info

    # 获取全部用例
    def get_case_all(self):
        excel = excelUtils(excel_file=self.excel_path,excel_sheet=self.get_excel_sheet()).data()
        case_list = [i for i in excel]
        return case_list

    # 获取允许执行用例
    def get_run_case(self):
        title = caseMethod().is_run
        case_all = self.get_case_all()
        case_list = list()
        for i in case_all:
            if str(i[title]).lower() == 'y' or i[title] == '是':
                case_list.append(i)
        return case_list

    # 获取前置条件用例
    def get_pre_case(self,pre_factor):
        case_all = self.get_case_all()
        for i in case_all:
            if pre_factor in dict(i).values():
                return i
        return None

    # 获取邮箱信息
    def get_email_info(self):
        email_info = self.base['email']
        return email_info
