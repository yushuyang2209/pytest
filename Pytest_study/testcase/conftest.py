'''author: Shu YuTou Date:2022/5/9'''

import pytest
@pytest.fixture(scope='function')
def all_fixture():
	print("全局的前置")
	yield
	print("全局的后置")
