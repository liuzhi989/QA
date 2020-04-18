import re

class reUtils(object):

    # 查询
    def find(self,target,pattern_data='\${(.*)}\$'):
        re_res = re.compile(pattern_data).findall(target)
        return re_res[0]

    # 替换
    def sub(self,target,replace,pattern_data='\${(.*)}\$'):
        re_res = self.find(target=target,pattern_data=pattern_data)
        if re_res:
            sub_res = re.sub(pattern_data,replace,target)
            return sub_res
        return re_res

    # 前置条件替换
    def pre_re_sub(self,target,pre_res,pattern_data='\${(.*)}\$'):
        if '${' in target:
            re_res = self.find(target=target,pattern_data=pattern_data)
            if len(re_res):
                replace = pre_res['body'][re_res]
                target = self.sub(target=target,replace=replace,pattern_data=pattern_data)
        return target
