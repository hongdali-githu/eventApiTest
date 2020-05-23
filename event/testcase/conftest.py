#coding=utf-8
import pytest
from event.common.Mysqlhandle import Mysql_Handle
from event.config.config import LoggerConfig,MysqlConfig
from event.common.LoggerHandle import Logger_Handle
#mysql连接
@pytest.fixture()
def mysqlhandle():
    mysqlquery = Mysql_Handle(MysqlConfig.host, MysqlConfig.port, MysqlConfig.user, MysqlConfig.password,
                               MysqlConfig.database)
    yield mysqlquery
    mysqlquery.close()

#插入id为123456的事件,继承mysqlhandle
@pytest.fixture()
def mysqlhandle_insert(mysqlhandle):
    mysqlhandle.query(MysqlConfig.insertdata)
    yield mysqlhandle
    mysqlhandle.query("delete from eh_task where id=%s",(123456,))


#日志处理
@pytest.fixture(scope="class")
def loggerhandle():
    logger = Logger_Handle("root", "INFO", filename=LoggerConfig.log_path)
    yield logger




