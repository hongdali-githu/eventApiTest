#coding=utf-8
import os
import time
class LoggerConfig:
    path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"out\log")
    if not os.path.exists(path):
        os.mkdir(path)
    now=time.strftime("%y-%m-%d %H-%M-%S",time.localtime())
    log_path=os.path.join(path,"{}log.txt".format(now))
#数据库连接
class MysqlConfig:
    host="10.45.26.99"
    port=3306
    user="root"
    password="iwhaleCloud@2018"
    database="event_handle"
    insertdata="INSERT INTO `eh_task`(`id`, `task_status`, `task_priority`, `event_id`, `interface_id`, `event_unique_code`, `event_type_code`, `event_report_seq`, `event_address`, `event_address_xy`, `event_address_xy_src`, `event_range`, `event_range_src`, `event_range_links`, `event_cross`, `event_rid`, `event_occur_time`, `event_title`, `event_content`, `event_process`, `event_level`, `event_source`, `event_source_code`, `show_id`, `show_flag`, `new_flag`, `overdue_flag`, `org_code`, `area_code`, `object_code`, `photo_code`, `video_code`, `voice_code`, `msg_content`, `sub_task_num`, `sub_task_num_cnt`, `old_id`, `report_person`, `gmt_create`, `gmt_modified`, `short_video_code`, `segment_id`, `event_end_time`, `event_address_xys`) VALUES ('123456', 'I', '4', NULL, NULL, NULL, 'EVENT_TYPE_524', '1', '衢州站', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2020-05-16 00:19:23', '骑快车道', '骑快车道', NULL, '4', '接报警平台', '3308002005080500005', NULL, '1', NULL, '0', '330800', '330800', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '{\"name\":\"王\",\"tel\":\"13957006664\"}', '2020-05-08 00:20:34.000', '2020-05-08 00:20:34.000', NULL, NULL, NULL, NULL);"


#测试数据
class TestData:
    dir=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"testdata")
    event_task_controller=os.path.join(dir,"event_task_controller.xlsx")

if __name__=="__main__":
    print(TestData.event_task_controller)





