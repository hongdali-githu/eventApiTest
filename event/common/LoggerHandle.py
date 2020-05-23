#coding=utf-8
import logging
from event.config.config import LoggerConfig

class Logger_Handle(logging.Logger):

    def __init__(self, name, level, filename=None, format="%(asctime)s-%(name)s-%(filename)s-%(lineno)s-%(levelname)s-%(message)s"):
        self.name=name
        self.level=level
        self.filename=filename
        self.format=format
        super().__init__(name)
        #设置日志打印级别
        self.setLevel(self.level)
        #如果文件存在，及将打印到文件
        if filename:
            #使用文件打印日志
            File_handler=logging.FileHandler(filename)
            #设置文件展示日志级别
            File_handler.setLevel(self.level)
            #将输出日志与文件打印日志进行绑定
            self.addHandler(File_handler)
            #设置文件的格式
            format=logging.Formatter(self.format)
            #加载带有格式的日志
            File_handler.setFormatter(format)
        else:
            #使用控制台打印日志
            Stream_handler=logging.StreamHandler()
            #设置控制台显示日志级别
            Stream_handler.setLevel(level)
            # 将处理器与收集器绑定
            self.addHandler(Stream_handler)


if __name__=="__main__":
    Logger_Handle("root","INFO",filename=LoggerConfig.log_path).info("aa")


