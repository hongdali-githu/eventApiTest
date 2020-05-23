#coding=utf-8
import pymysql
from pymysql.cursors import DictCursor
from event.config.config import LoggerConfig,MysqlConfig
from event.common.LoggerHandle import Logger_Handle
logger=Logger_Handle("root","INFO",filename=LoggerConfig.log_path)

class Mysql_Handle:
    #cursorclass=DictCursor设置返回的结果为字典
    def __init__(self,host,port,user,password,database,charset="utf8",cursorclass=DictCursor):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.database=database
        self.charset=charset
        self.cursorclass=cursorclass
        #建立连接
        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database,
                                    charset=self.charset,cursorclass=self.cursorclass)
        except Exception as e:
            logger.error("{}数据库连接失败".format(e))
        else:
            logger.info("数据库连接成功")

        #建立游标
        self.cursor=self.conn.cursor()
#进行sql增、删、改、查
    def query(self,sql,args=None):
        try:
            self.cursor.execute(sql,args=args)
            #TODO 提交事务
            self.conn.commit()
        except Exception as e:
            logger.error("执行失败{}".format(e))
            raise e
        else:
            one = self.cursor.fetchone()
            logger.info("数据查询结果为{}".format(one))
            return one
#关闭连接
    def close(self):
        self.cursor.close()
        self.conn.close()



if __name__=="__main__":
    mysqlhandle=Mysql_Handle("10.45.26.99",3306,"root","iwhaleCloud@2018","event_handle")
    mysqlhandle.query(MysqlConfig.insertdata)
    data=mysqlhandle.query("select * from eh_task where id=%s;",(123456,))
    print(data["event_address"])
    mysqlhandle.close()


