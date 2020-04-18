import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class emailUtils(object):

    # 初始化
    def __init__(self,smtp,username,password,recipient,title,content=None,file=None):

        self.smtp = smtp
        self.username = username
        self.password = password
        self.recipient = recipient
        self.title = title
        self.content = content
        self.file = file

    # 发送邮件
    def send_email(self):
        # 导入MIMEMultipart
        msg = MIMEMultipart()

        # 初始化邮件信息
        msg.attach(MIMEText(self.content,_charset='utf-8'))
        msg['Subject'] = self.title
        msg['From'] = self.username
        msg['To'] = self.recipient
        # 判断是否有附件
        if self.file:
            # 打开附件
            att = MIMEText(open(self.file).read())
            # 设置内容类型
            att['Content-Type'] = 'application/octet-stram'
            # 设置附件头
            att['Content-Disposition'] = 'attachment;filename="{}"'.format(self.file)
            # 添加到主体
            msg.attach(att)

        # 登录邮箱
        self.login_smtp = smtplib.SMTP(self.smtp,port=25)
        self.login_smtp.login(self.username,self.password)

        # 发送邮件
        self.login_smtp.sendmail(self.username,self.recipient,msg.as_string())