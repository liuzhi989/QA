import requests

class requestsUtils(object):

    # get
    def get(self,url,data=None,headers=None,cookies=None):
        res = requests.get(url,data=data,headers=headers,cookies=cookies)
        return res

    # post
    def post(self,url,data=None,headers=None,cookies=None):
        res = requests.post(url,data=data,headers=headers,cookies=cookies)
        return res

    # 公共方法
    def res_api(self,url,mode,**kwargs):
        if mode == 'get':
            self.res = self.get(url,**kwargs)
        elif mode == 'post':
            self.res = self.post(url,**kwargs)

        code = self.res.status_code
        try:
            body = self.res.json()
        except:
            body = self.res.text

        dic = dict()
        dic['code'] = code
        dic['body'] = body

        return dic
