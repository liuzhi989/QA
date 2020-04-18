import json
from common.mysqlMethod import mysqlMethod
from common.logsMethod import logsMethod

class assertUtils(object):

    def __init__(self):
        self.log = logsMethod().log('assertUtils')

    # code 相等
    def code_equal(self,code,except_code):
        try:
            assert code == except_code
            return True
        except:
            self.log.error('Code Error：Code不相等，预期Code是{}，实际Code是{}。'.format(except_code,code))
            raise

    # body 相等
    def body_equal(self,body,except_body):
        try:
            assert body == except_body
            return True
        except:
            self.log.error('Body Error：Body不相等，预期Body是{}，实际Body是{}。'.format(except_body,body))
            raise

    # body包含
    def except_in_body(self,body,except_body):
        except_body_dic = json.loads(except_body)
        # 遍历赋值
        for i,j in body.items():
            if i not in except_body_dic:
                except_body_dic[i] = j

        # 对比
        try:
            assert body == except_body_dic
            return True
        except:
            self.log.error('Body Error：不包含或Body错误，预期Body是{}，实际Body是{}。'.format(except_body,body))
            raise

    # 数据库对比
    def mysql_equal(self,mysql_name,sql,body):
        mysql_res = mysqlMethod().mysql_api(mysql_name).select(sql)
        mysql_res_key = dict(mysql_res).keys()
        # 循环对比
        try:
            for i in mysql_res_key:
                body_value = body[i]
                mysql_res_value = mysql_res[i]
                assert body_value == mysql_res_value
            return True
        except Exception:
            self.log.error('Mysql Error：与数据库不一致，数据库结果是{}，实际Body是{}。'.format(mysql_res,body))
            raise

# if __name__ == '__main__':
#     a = 'meiduo'
#     b = "select id,username,mobile,email from tb_users where username = 'python'"
#     body = {'id': 2, 'username': 'python', 'mobile': '17701397029', 'email': '952673638@qq.com', 'email_active': True}
