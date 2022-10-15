'''author: Shu YuTou Date:2022/5/10'''
import pytest
import requests

class TestApi:
	# @pytest.mark.parametrize('name,age',[['百里','38'],['微微','19']])
	def test_01_baili(self):
		url = 'https://192.168.11.75/ifort/usergroup/addUserGroup'
		params =  {
			"groupName": "用户组api",
			"groupDesc": "api添加",
			"deptId": 1,
			"deptName": "默认"
		}
		res = requests.post(url,params=params)
		print(res)
if __name__ == '__main__':
    pytest.main()