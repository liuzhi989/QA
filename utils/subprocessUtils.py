import subprocess
from common.logsMethod import logsMethod

class subprocessUtils(object):

    # 初始化
    def __init__(self):
        self.log = logsMethod().log('subprocessUtils')

    # 执行allure命令
    def allure_report(self,report_path,report_html_path):
        allure_cmd = 'allure generate {} -o {} --clean'.format(report_path,report_html_path)
        try:
            subprocess.call(allure_cmd,shell=True)
        except:
            self.log.error('Subporcess Error：执行失败，请检查测试环境相关配置！')
            raise
