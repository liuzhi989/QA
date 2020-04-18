from config.baseData import baseData
from utils.pymysqlUtils import pymysqlUtils

class mysqlMethod(object):


    def mysql_api(self,mysql_name):
        mysql_info = baseData().get_mysql_info(mysql_name)
        host = mysql_info['host']
        user = mysql_info['user']
        password = mysql_info['password']
        database = mysql_info['database']
        port = int(mysql_info['port'])

        connect = pymysqlUtils(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        return connect

