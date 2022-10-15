'''author: Shu YuTou Date:2022/5/10'''
import yaml

class YamlUtil:
	def __init__(self,yaml_file):
		"""
		通过init方法，把yaml文件传入到这个类
		:param yaml_file:
		"""
		self.yaml_file = yaml_file
	#读取yaml文件
	def read_yaml(self):
		"""
		读取yaml，对yaml反序列化，就是把我们的yaml格式转化为字典dict的格式
		:return:
		"""
		with open(self.yaml_file,encoding="UTF-8") as f:
			value = yaml.load(f, Loader=yaml.FullLoader)
			print(value,'\n',type(value))
			
if __name__ == '__main__':
    YamlUtil('test_api.yaml').read_yaml()