from config.baseData import baseData
from utils.emailUtils import emailUtils

class emailMethod(object):

    # 发送邮件公共方法
    def email_api(self,title=None,report_html_path=None,content=None):
        email_info = baseData().get_email_info()
        smtp = email_info['smtp']
        username = email_info['username']
        password = email_info['password']
        recipient = email_info['recipient']

        emailUtils(
                smtp=smtp,
                username=username,
                password=password,
                recipient=recipient,
                title=title,
                content=content,
                file=report_html_path
            ).send_email()