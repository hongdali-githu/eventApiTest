#coding=utf-8
import pytest
from event.common.RequestHandle import Request_Handle
from event.common.Mysqlhandle import Mysql_Handle
from event.common.LoggerHandle import Logger_Handle
from event.common.ExeclHandle import Execl_Handle_xlsx
from event.config.config import LoggerConfig,MysqlConfig,TestData



#事件基础信息接口
#TODO:根据id查询事件信息
@pytest.mark.usefixtures("loggerhandle")
class TestEventBaseInfo:
    execl_0 =Execl_Handle_xlsx(TestData.event_task_controller, 0)
    @pytest.mark.usefixtures("mysqlhandle")
    @pytest.mark.parametrize("case",execl_0.get_all())
    def test_event_query(self,mysqlhandle,loggerhandle,case):
        data = mysqlhandle.query("select * from eh_task limit 1;")
        id = data["id"]
        res = Request_Handle().query(case["url"]+id, case["method"])
        print(res)
        try:
            assert(res["data"]["id"],id)
            loggerhandle.info("{}校验成功".format(case["case_name"]))
        except Exception as e:
            loggerhandle.error("{}校验失败{}".format(case["case_name"],e))
            raise e


#TODO:根据id更新事件信息
    execl_1 = Execl_Handle_xlsx(TestData.event_task_controller, 1)
    @pytest.mark.usefixtures("mysqlhandle_insert")
    @pytest.mark.parametrize("case",execl_1.get_all())
    def test_event_update(self,mysqlhandle_insert,loggerhandle,case):
        res = Request_Handle().query(case["url"], case["method"],json=case["params"])
        print(res)
        data = mysqlhandle_insert.query("select * from eh_task where id=%s;",(123456,))
        try:
            assert(data["event_address"],"衢州交警支队")
            loggerhandle.info("{}校验成功".format(case["case_name"]))
        except Exception as e:
            loggerhandle.error("{}校验失败{}".format(case["case_name"],e))
            raise e

#TODO 更新事件状态

    execl_2 = Execl_Handle_xlsx(TestData.event_task_controller, 2)
    @pytest.mark.usefixtures("mysqlhandle_insert")
    @pytest.mark.parametrize("case",execl_2.get_all())
    @pytest.mark.demo
    def test_status_update(self,mysqlhandle_insert,loggerhandle,case):
        res = Request_Handle().query(case["url"], case["method"], data=case["params"])
        data = mysqlhandle_insert.query("select * from eh_task where id=%s;",(123456,))
        print(data["task_status"])
        try:
            assert(data["task_status"],"F")
            loggerhandle.info("{}校验成功".format(case["case_name"]))
        except Exception as e:
            loggerhandle.error("{}校验失败{}".format(case["case_name"],e))
            raise e


if __name__=="__main__":
    pytest.main(["-s","-v"])


