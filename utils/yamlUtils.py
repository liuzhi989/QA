import yaml,os

class yamlUtils(object):

    # 初始化
    def __init__(self,yaml_file):
        # 判断文件
        if os.path.exists(yaml_file):
            self.yaml_file = yaml_file
        else:
            raise FileNotFoundError('Yaml Error：文件不存在！')

    # 读取单个
    def data(self):
        with open(self.yaml_file,'rb') as f:
            _data = yaml.safe_load(f)
        return _data

    # 读取多个
    def data_all(self):
        with open(self.yaml_file,'rb') as f:
            _data_all = list(yaml.safe_load_all(f))
        return _data_all