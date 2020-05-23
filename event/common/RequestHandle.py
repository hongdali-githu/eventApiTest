#coding=utf-8
import requests
from event.common.LoggerHandle import Logger_Handle
from event.config.config import LoggerConfig

logger=Logger_Handle("root","INFO",filename=LoggerConfig.log_path)
class Request_Handle:
    def __init__(self):
        #一个请求的对话框
        self.session=requests.session()

    def query(self,url,method,params=None,data=None,json=None,headers=None):
        try:
            res=self.session.request(method,url,params=params,data=data,json=json,headers=headers)
        except Exception as e:
            logger.error("请求连接失败{}".format(e))
            raise e
        else:
            logger.info("请求连接成功")
            #返回的就是字典格式
            return res.json()

    def close(self):
        self.session.close()

if __name__=="__main__":
    res = Request_Handle().query( "http://10.45.26.100:18888/event/task/status","put",data={"None"})
    print(res)