import json

class caseMethod(object):

    # 初始化
    def __init__(self):
        # 用例头部信息
        self.case_id = '用例ID'
        self.case_module = '模块'
        self.case_name = '用例名称'
        self.url = 'URL'
        self.pre_factor = '前置条件'
        self.mode = '请求方式'
        self.datas = '请求参数'
        self.except_body = '预期结果'
        self.is_run = '是否执行'
        self.headers = 'headers'
        self.cookies = 'cookies'
        self.except_code = 'status_code'
        self.mysql_name = '数据库名称'
        self.sql = '数据库验证'

    # 格式转化
    def json_api(self,data):
        json_data = json.loads(data) if data else data
        return json_data