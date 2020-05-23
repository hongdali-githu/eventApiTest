#coding=utf-8
import pytest
from event.common.ExeclHandle import Execl_Handle_xlsx
execl = Execl_Handle_xlsx(r"D:\事件感知\event\common\testdata.xlsx", 0)
@pytest.mark.parametrize("case", execl.get_all())
def test_aa(case):
     print(case["params"])

