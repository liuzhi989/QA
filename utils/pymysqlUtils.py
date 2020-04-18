import pymysql
from common.logsMethod import logsMethod

class pymysqlUtils(object):

    # 初始化
    def __init__(self,host,user,password,database,port,charset='utf8'):
        # 连接
        self.connect = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port,
                charset=charset
            )
        # 光标
        self.cursor = self.connect.cursor(cursor=pymysql.cursors.DictCursor)
        # log
        self.log = logsMethod().log('pymysqlUtils')

    # 查询单个
    def select(self,sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return data

    # 查询多个
    def select_all(self,sql):
        self.cursor.execute(sql)
        data_all = self.cursor.fetchall()
        return data_all

    # 执行
    def updata(self,sql):
        try:
            if self.connect and self.cursor:
                self.cursor.execute(sql)
                self.connect.commit()
                return True
        except Exception as ex:
            self.connect.rollback()
            self.log.error('Mysql Error：执行失败！')
            self.log.error(ex)

    # 关闭对象
    def __del__(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.connect is not None:
            self.connect.close()
