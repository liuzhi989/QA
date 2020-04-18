import pytest,allure
from config.baseData import baseData
from utils.requestsUtils import requestsUtils
from common.caseMethod import caseMethod
from utils.reUtils import reUtils
from utils.assertUtils import assertUtils

class testCase(object):

    data = baseData()
    case_list = data.get_run_case()
    sheet_name = data.get_excel_sheet()

    base = caseMethod()

    # 执行
    def run_api(self,url,mode,datas=None,headers=None,cookies=None):
        data = self.base.json_api(datas)
        header = self.base.json_api(headers)
        cookie = self.base.json_api(cookies)

        res = requestsUtils().res_api(
            url = url,
            mode = mode,
            data = data,
            headers = header,
            cookies = cookie
        )
        return res

    # 前置条件
    def pre_case(self,pre_case):
        url = pre_case[self.base.url]
        mode = pre_case[self.base.mode]
        datas = pre_case[self.base.datas]
        headers = pre_case[self.base.headers]
        cookies = pre_case[self.base.cookies]

        pre_res = self.run_api(
                url=url,
                mode=mode,
                datas=datas,
                headers=headers,
                cookies=cookies
            )
        return pre_res

    # 执行用例
    @pytest.mark.parametrize('case',case_list)
    def test_case(self,case):
        # 用例信息
        case_id = case[self.base.case_id]
        case_module = case[self.base.case_module]
        case_name = case[self.base.case_name]
        url = case[self.base.url]
        pre_factor = case[self.base.pre_factor]
        mode = case[self.base.mode]
        datas = case[self.base.datas]
        except_body = case[self.base.except_body]
        headers = case[self.base.headers]
        cookies = case[self.base.cookies]
        except_code = case[self.base.except_code]
        mysql_name = case[self.base.mysql_name]
        sql = case[self.base.sql]

        # 判断是否有前置条件
        if pre_factor:
            pre_case = self.data.get_pre_case(pre_factor)
            pre_res = self.pre_case(pre_case)
            headers = reUtils().pre_re_sub(target=headers,pre_res=pre_res)
            cookies = reUtils().pre_re_sub(target=cookies,pre_res=pre_res)

        # 执行用例
        res = self.run_api(
                url=url,
                mode=mode,
                datas=datas,
                headers=headers,
                cookies=cookies
            )

        # 获取返回数据
        code = res['code']
        body = res['body']

        # 断言
        if except_code:
            assertUtils().code_equal(code=code,except_code=except_code)
        if except_body:
            assertUtils().except_in_body(body=body,except_body=except_body)
        if mysql_name and sql:
            assertUtils().mysql_equal(mysql_name=mysql_name,sql=sql,body=body)

        # 生成测试报告
        allure.dynamic.feature(self.sheet_name)
        allure.dynamic.story(case_module)
        allure.dynamic.title(case_id +' '+ case_name)
        desc = "<font color='red'>请求URL：</font>{}<Br/>  " \
               "<font color='red'>请求类型：</font>{}<Br/>  " \
               "<font color='red'>期望结果：</font>{}<Br/>  " \
               "<font color='red'>实际结果：</font>{}<Br/>  ".format(url,mode,except_body,body)
        allure.dynamic.description(desc)