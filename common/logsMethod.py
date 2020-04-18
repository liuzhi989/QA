import os,datetime
from utils.loggingUtils import loggingUtils
from config.baseData import baseData

class logsMethod(object):

    # 定义数据
    def __init__(self):
        self.logs_path = baseData().logs_path
        self.logs_level = baseData().get_log_level()
        self.now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        self.logs_file = os.path.join(self.logs_path,self.now_time + '.log')

    # 公共方法
    def log(self,logs_name = __file__):
        log = loggingUtils(
                logs_name=logs_name,
                logs_level=self.logs_level,
                logs_file=self.logs_file
            ).logger
        return log