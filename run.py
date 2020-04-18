import pytest,os
from utils.subprocessUtils import subprocessUtils
from config.baseData import baseData
from common.emailMethod import emailMethod

if __name__ == '__main__':
    report_path = baseData().report_path + os.sep + 'result'
    report_html_path = baseData().report_path + os.sep + 'html'
    excel_sheet = baseData().get_excel_sheet()
    pytest.main(['-s','--alluredir',report_path])
    # subprocessUtils().allure_report(report_path=report_path,report_html_path=report_html_path)
    # emailMethod().email_api(title=excel_sheet,content=report_html_path)
