import logging

class loggingUtils(object):

    # 生成log
    def __init__(self,logs_name,logs_level,logs_file):
        self.logs_name = logs_name
        self.logs_file = logs_file
        self.logs_level = logs_level
        self.logs_l = {
                'debug':logging.DEBUG,
                'info':logging.INFO,
                'warning':logging.WARNING,
                'Error':logging.ERROR
            }

        self.logger = logging.getLogger(self.logs_name)
        self.logger.setLevel(self.logs_l[self.logs_level])
        self.formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s')

        if not self.logger.handlers:
            console = logging.StreamHandler()
            console.setLevel(self.logs_l[self.logs_level])
            console.setFormatter(self.formatter)

            file = logging.FileHandler(logs_file)
            file.setLevel(self.logs_l[self.logs_level])
            file.setFormatter(self.formatter)

            self.logger.addHandler(console)
            self.logger.addHandler(file)

